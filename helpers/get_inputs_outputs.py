import requests
import json
import os

GEMINI_API_KEY = "AIzaSyBdyWaRhXjfbIL7i3_c4H0Y_J3oCHrG5wI"
def get_inputs_outputs_from_transcript(transcript):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"

    payload = {
        "contents": [{
            "parts": [{
                "text": f"""From the following transcript, extract the 'Inputs' and 'Outputs' involved in the process.
Return them clearly formatted in this structure:

Inputs:
  ➤ [input 1]  
  ➤ [input 2]  
  ...

Output:
  ➤ [output 1]  
  ➤ [output 2]  
  ...

Do not include any introductory or extra explanation. Just return the clean formatted section.
Transcript:
{transcript}
"""
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
        print("API Response:", response_data)  # Optional: for debugging

        return response_data.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "").strip()

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return ""

if __name__ == "__main__":
    # Example usage
    sample_transcript = """
    So first the user uploads a CSV file containing invoice data. 
    Then the system verifies the entries against the SAP database. 
    Finally, a report is generated showing the matched and unmatched records.
    """
    result = get_inputs_outputs_from_transcript(sample_transcript)
    print("\nExtracted Inputs and Outputs:\n")
    print(result)
