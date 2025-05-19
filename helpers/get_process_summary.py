import requests
import json
import os

GEMINI_API_KEY = "AIzaSyBdyWaRhXjfbIL7i3_c4H0Y_J3oCHrG5wI"

def get_process_summary(transcript):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"

    payload = {
        "contents": [{
            "parts": [{
                "text": f"""Analyze the following meeting transcript and generate a summary. The summary should only strictly
include the business process summary, not the meeting summary. 
Instructions:
- Don't add asterisks or any text structuring.

{transcript}"""
            }]
        }]
    }

    try:
        response = requests.post(
            url,
            headers={"Content-Type": "application/json"},
            data=json.dumps(payload)
        )
        response_data = response.json()
        print("API Response:", response_data)  # Debugging output

        return response_data.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return ""

if __name__ == "__main__":
    # Example usage (You can replace this with your actual transcript)
    dummy_transcript = "User logs in to SAP. Checks sales order status. Exports report to Excel. Emails it to client."
    summary = get_process_summary(dummy_transcript)
    print("\nBusiness Process Summary:\n", summary)
