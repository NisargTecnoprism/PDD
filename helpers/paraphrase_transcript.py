import requests
import os

GEMINI_API_KEY = "AIzaSyBdyWaRhXjfbIL7i3_c4H0Y_J3oCHrG5wI"

def paraphrase_transcript(text):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"
    prompt = f"""Paraphrase the following meeting transcript into a clear, professional action summary. 
        Avoid first-person language and describe only what is happening related to the process, keep it straight to the point,
        and only return the necessary text, no unnecessary structuring
        :\n\n
        {text}"""

    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt
                    }
                ]
            }
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()
        return result['candidates'][0]['content']['parts'][0]['text'].strip()
    except Exception as e:
        print(f"[Gemini Error]: {e}")
        return text

if __name__ == "__main__":
    sample_text = """Yesterday's meeting covered the status of the invoice processing automation.
    The team agreed to implement error handling for missing fields."""
    
    paraphrased = paraphrase_transcript(sample_text)
    print("Paraphrased Transcript:\n")
    print(paraphrased)
