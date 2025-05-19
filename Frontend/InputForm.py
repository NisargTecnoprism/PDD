import streamlit as st
import os
import main

st.title("Project Name and Video File Input")

project_name = st.text_input("Enter the project name:")
video_file = st.file_uploader("Upload a video file:", type=["mp4", "avi", "mov", "mkv"])

if st.button("Generate Document"):
    if project_name and video_file:
        with st.spinner("Processing..."):
            # Save uploaded video temporarily
            video_path = f"{project_name}_uploaded_video.mp4"
            with open(video_path, "wb") as f:
                f.write(video_file.read())

            # Run your model processing code
            output_path = main(project_name, video_path)

            # Show download button if successful
            if os.path.exists(output_path):
                with open(output_path, "rb") as f:
                    st.success("Document generated successfully!")
                    st.download_button(
                        label="Download Generated Document",
                        data=f,
                        file_name=os.path.basename(output_path),
                        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                    )
            else:
                st.error("Failed to generate the document.")
    else:
        st.warning("Please provide both project name and video file.")
