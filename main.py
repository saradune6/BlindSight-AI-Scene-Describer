## source myenv/bin/activate

import cv2
import google.generativeai as genai
from PIL import Image
from google.generativeai.types import content_types
import streamlit as st
# from dotenv import load_dotenv
# import os

# load_dotenv()
# API_KEY = os.getenv("GOOGLE_API_KEY")

API_KEY='AIzaSyDMth0Boy5y-bMnPlZ5SiUWxneKRdsSBdg'
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-pro-001")

def get_gemini_pro_vision_response(model, prompt, frames, generation_config={}, stream: bool = True):
    content = []
    content.append(prompt)
    for frame in frames:
        encoded_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        encoded_image = content_types.pil_to_blob(encoded_image)
        content.append(encoded_image)

    generation_config = {"temperature": 0.1, "max_output_tokens": 2048,}
    responses = model.generate_content(
        content, generation_config = generation_config, stream = stream
    )
    responses.resolve()
    return responses.text


def process_video_chunk(frames, user_prompt):
    prompt = user_prompt if user_prompt else (
        "Describe the scene in each image in detail for a blind person. "
        "Include the number of people, their activities, objects, and any significant surroundings."
    )
    response = get_gemini_pro_vision_response(model, prompt, frames)
    return response



####################### to fix here 
def feed_video_to_gemini(video_stream, user_prompt):
    chunk_size = 30  # Increased chunk size to send fewer requests
    frame_skip = 3  # Skip every 3 frames to reduce API calls
    frames = []
    image_counter = 0 

    stop_button = st.button("Stop", key="stop_button")

    while not stop_button:
        ret, video_chunk = video_stream.read()
        if not ret:
            break

        if image_counter % frame_skip == 0:  # Capture only every 3rd frame
            frames.append(video_chunk)

        if len(frames) == chunk_size:
            with st.spinner("Analyzing video chunk..."):
                try:
                    result = process_video_chunk(frames, user_prompt)
                    st.write("**Analysis Results:**")
                    st.write(result)
                except Exception as e:
                    st.error(f"An error occurred: {e}")
            frames = []

        if image_counter % (chunk_size * 2) == 0:  # Display fewer images
            st.image(video_chunk, channels="BGR", use_column_width=True)

        image_counter += 1

    video_stream.release()

############################

st.title("Video Analysis with Gemini")

default_prompt = "Describe the scene in each image in detail for a blind person. Include the number of people, their activities, objects, and any significant surroundings."
# user_prompt = st.text_input("Enter your prompt:", value=default_prompt, height=100)
user_prompt = st.text_area("Enter your prompt:", value=default_prompt) 


if st.button("Start Video Analysis"):
    video_stream = cv2.VideoCapture(1)
    feed_video_to_gemini(video_stream, user_prompt)




