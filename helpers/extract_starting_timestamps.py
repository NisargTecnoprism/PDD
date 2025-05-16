import os
import re

def extract_starting_timestamps(transcript_file, keywords):
    if not transcript_file or not os.path.exists(transcript_file):
        print("❌ Error: Transcript file not found.")
        return [], {}
    
    timestamps, transcript_dict = [], {}
    with open(transcript_file, "r", encoding="utf-8") as file:
        lines = file.readlines()
    
    # Create a flattened list of all trigger words (case-insensitive)
    all_keywords = set(
        word.lower() for trigger_words in keywords.values() for word in trigger_words
    )
    
    for line in lines:
        match = re.match(r"\[(\d+\.\d+) - (\d+\.\d+)\]\s+(.*)", line)
        if match:
            start_time, _, text = match.groups()
            start_time = float(start_time)
            transcript_dict[start_time] = text.strip()
            
            # Convert text to lowercase for case-insensitive comparison
            text_lower = text.lower()
            
            # Check if any keyword is present in the text
            if any(keyword in text_lower for keyword in all_keywords):
                timestamps.append(start_time)
    
    return timestamps, transcript_dict


if __name__ == "__main__":
    # Example usage
    example_transcript = "example_transcript.txt"  # Put your transcript filename here
    example_keywords = {
        "start_process": ["start", "begin", "initiate"],
        "decision": ["if", "whether", "else"],
    }

    timestamps, transcript_dict = extract_starting_timestamps(example_transcript, example_keywords)
    print(f"Timestamps with keywords: {timestamps}")
    print("Corresponding transcript lines:")
    for ts in timestamps:
        print(f"[{ts}] {transcript_dict[ts]}")
