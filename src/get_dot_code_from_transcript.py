import requests
import json
import re

def get_dot_code_from_transcript(transcript, api_key):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"

    prompt = f"""
You are an expert in analyzing work transcripts to extract meaningful process flows for automation and software development.

Objective:
- Identify only the core functional steps and decisions required to complete the task described in the transcript below.
- Ignore all non-functional, conversational, environmental, or observational statements (e.g., greetings, screen sharing, system visibility checks).
- Focus only on actions that lead to meaningful data processing or user input/output.

- Output the result strictly as a valid Graphviz DOT code block inside triple backticks using ```dot.
- First, define each node separately using `shape` and `label`.
- Then, define all edges between nodes.
- For decision points, use shape=diamond and ensure every decision has two labeled outgoing edges (e.g., Yes/No).
- Do NOT include shapes or labels in edge definitions — only in node declarations.
- Ensure there is one clear Start and End node (both shape=oval).
- Avoid duplicate edges or nodes.
- Maintain indentation and valid DOT syntax.

Transcript:
{transcript}
"""

    payload = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }

    try:
        response = requests.post(
            url,
            headers={"Content-Type": "application/json"},
            data=json.dumps(payload)
        )

        response_data = response.json()
        raw_text = response_data.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "")
        print("Raw Gemini Output:\n", raw_text)

        # Try extracting DOT code if it's inside ```dot ... ```
        match = re.search(r'```dot\n(.*?)```', raw_text, re.DOTALL)
        if match:
            return match.group(1).strip()
        
        # Else try getting anything that looks like a DOT graph
        match = re.search(r'digraph\s+\w*\s*{.*?}', raw_text, re.DOTALL)
        if match:
            return match.group(0).strip()
        
        print("No DOT content found in Gemini response.")
        return None

    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")
        return None

if __name__ == "__main__":
    # Example usage
    dummy_transcript = "User logs into the system. User clicks 'Generate Report'. System processes data. User downloads report."
    dummy_api_key = "YOUR_API_KEY_HERE"
    dot_code = get_dot_code_from_transcript(dummy_transcript, dummy_api_key)
    
    if dot_code:
        print("\nExtracted DOT Code:\n")
        print(dot_code)
    else:
        print("DOT code could not be extracted.")
