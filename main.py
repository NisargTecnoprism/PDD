import os
import time

from docx import Document

import helpers.video_to_text
import helpers.paraphrase_transcript
import helpers.get_inputs_outputs
import helpers.extract_starting_timestamps
import helpers.extract_specific_frame
import helpers.append_frames_to_doc
import helpers.docx_builder

from config import (
    video_path, audio_output_dir, model_name, doc_path,
    keywords, GEMINI_API_KEY
)

def main():
    print("🔁 Starting Process Design Document (PDD) Generation...\n")

    # STEP 1: Transcribe Video
    print("🎤 Transcribing video...")
    transcript_path = helpers.video_to_text(video_path, audio_output_dir, model_name)
    if not transcript_path:
        print("❌ Transcription failed.")
        return
    print(f"✅ Transcript saved at: {transcript_path}\n")

    # STEP 2: Read Transcript
    with open(transcript_path, "r", encoding="utf-8") as file:
        transcript_text = file.read()

    # STEP 3: Get Process Summary from Gemini
    print("🧠 Generating process summary...")
    process_summary = helpers.paraphrase_transcript(transcript_text)

    # STEP 4: Extract Inputs and Outputs
    print("📥📤 Extracting inputs and outputs...")
    input_and_output = helpers.get_inputs_outputs_from_transcript(transcript_text)

    # STEP 5: Generate Base Word Document
    print("📄 Creating initial PDD structure...")
    project_name = "Automated Process Documentation"
    doc = helpers.create_base_doc(project_name, process_summary, input_and_output)
    doc.save(doc_path)

    # STEP 6: Extract Action Timestamps
    print("⏱️ Identifying timestamps with actions...")
    timestamps, transcript_dict = helpers.extract_starting_timestamps(transcript_path, keywords)
    if not timestamps:
        print("⚠️ No action-based timestamps found.")
    else:
        print(f"✅ Found {len(timestamps)} action points.")

    # STEP 7: Extract Frames for Each Timestamp
    print("🖼️ Extracting frames from video...")
    frame_transcript_pairs = []
    frame_output_dir = os.path.join(audio_output_dir, "frames")
    for timestamp in timestamps:
        frame_path = helpers.extract_specific_frame(video_path, timestamp, frame_output_dir)
        if frame_path:
            frame_transcript_pairs.append((frame_path, transcript_dict[timestamp]))

    if not frame_transcript_pairs:
        print("⚠️ No frames were extracted.")
    else:
        print(f"✅ Extracted {len(frame_transcript_pairs)} frames.\n")

    # STEP 8: Append Frames & Descriptions to Doc
    print("📎 Appending frames with summarized steps to document...")
    helpers.append_frame_to_doc(frame_transcript_pairs, doc_path)

    print("\n🎉 PDD Document Generated Successfully!")
    print(f"📁 File saved at: {doc_path}")

if __name__ == "__main__":
    main()
