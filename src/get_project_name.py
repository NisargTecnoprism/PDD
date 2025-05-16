import requests
import json
import os

# You should set your API key as an environment variable for security
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def get_project_name_from_transcript(transcript):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"

    payload = {
        "contents": [{
            "parts": [{
                "text": f"""Analyze the following transcript and extract the project name being discussed.
If no project name is clearly mentioned, generate a meaningful and relevant project name based on the context.
Instructions:
- Return only the project name as plain text
- Do not add any extra explanation, formatting, or punctuation

Transcript:
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
        print("API Response:", response_data)  # Optional debug output

        return response_data.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "").strip()

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return ""

if __name__ == "__main__":
    # Sample usage
    dummy_transcript = "Today we're automating the invoice reconciliation process for the finance team using SAP and Excel macros."
    project_name = get_project_name_from_transcript(dummy_transcript)
    print("\nDetected Project Name:\n", project_name)
