def read_transcript(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read().strip()
    except FileNotFoundError:
        print("Error: File not found.")
        return ""

if __name__ == "__main__":
    # Example usage
    example_path = "output_audio/example_video_transcript.txt"  # Replace with your actual path
    content = read_transcript(example_path)
    print("\nTranscript Content:\n")
    print(content)
