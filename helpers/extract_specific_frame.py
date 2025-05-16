import os
import cv2

def extract_specific_frame(video_path, target_timestamp, new_output_folder):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Could not open video at {video_path}")
        return None
    
    fps = cap.get(cv2.CAP_PROP_FPS)
    target_frame_number = int(target_timestamp * fps)
    cap.set(cv2.CAP_PROP_POS_MSEC, target_timestamp * 1000)
    ret, frame = cap.read()
    cap.release()
    
    if ret:
        os.makedirs(new_output_folder, exist_ok=True)
        frame_filename = os.path.join(new_output_folder, f"frame_{target_frame_number}_{target_timestamp:.2f}.jpg")
        cv2.imwrite(frame_filename, frame)
        print(f"Extracted frame saved to: {frame_filename}")
        return frame_filename
    else:
        print("Failed to read frame at the specified timestamp.")
        return None


if __name__ == "__main__":
    # Example usage
    video_file = "example_video.mp4"          # Replace with your video file path
    timestamp = 10.5                          # Time in seconds to extract frame
    output_folder = "extracted_frames"       # Folder to save extracted frame

    result = extract_specific_frame(video_file, timestamp, output_folder)
    if result:
        print(f"Frame extracted successfully: {result}")
    else:
        print("No frame extracted.")
