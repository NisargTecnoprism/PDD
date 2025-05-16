import os
import subprocess
import whisper

# Function to convert video to audio and transcribe it
def video_to_text(video_file, audio_output_dir, model_name="base"):
    base_name = os.path.splitext(os.path.basename(video_file))[0]
    audio_file = os.path.join(audio_output_dir, f"{base_name}.mp3")
    transcript_file = os.path.join(audio_output_dir, f"{base_name}_transcript.txt")

    if os.path.exists(transcript_file):
        print(f"Transcript already exists: {transcript_file}")
        return transcript_file

    if not os.path.exists(audio_output_dir):
        os.makedirs(audio_output_dir)

    # Convert video to audio using FFmpeg
    ffmpeg_cmd = [
        "ffmpeg", "-i", video_file, "-vn", "-acodec", "libmp3lame", "-ab", "192k", "-ar", "44100", "-y", audio_file
    ]
    try:
        print("Converting video to audio...")
        subprocess.run(ffmpeg_cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"FFmpeg error: {e}")
        return None

    # Load Whisper model and transcribe
    try:
        print("Loading Whisper model...")
        model = whisper.load_model(model_name)
        print("Transcribing...")
        result = model.transcribe(audio_file, word_timestamps=False, task="translate", language="hi")
        with open(transcript_file, "w", encoding="utf-8") as f:
            for segment in result["segments"]:
                start_time, end_time, text = segment["start"], segment["end"], segment["text"]
                f.write(f"[{start_time:.2f} - {end_time:.2f}] {text}\n")
        print(f"Transcription saved to: {transcript_file}")
        return transcript_file
    except Exception as e:
        print(f"Whisper error: {e}")
        return None

if __name__ == "__main__":
    # Example usage
    video_path = "example_video.mp4"  # Replace with your actual video file
    output_dir = "output_audio"
    video_to_text(video_path, output_dir)
