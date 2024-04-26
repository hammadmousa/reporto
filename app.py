import os
import streamlit as st
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
import google.generativeai as genai
from pydub import AudioSegment
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TIT2, TPE1, TRCK, TALB
import warnings

# Ignore specific warnings from pydub
warnings.filterwarnings("ignore", message="Couldn't find ffmpeg or avconv - defaulting to ffmpeg, but may not work", category=RuntimeWarning, module='pydub.utils')

def generate_content(img=None):
    load_dotenv()
    gemini_api_key = os.getenv('GEMINI_API_KEY')
    genai.configure(api_key=gemini_api_key)
    model = genai.GenerativeModel('gemini-1.0-pro-vision-latest')
    try:
        genai_client = genai.GenerativeModel('gemini-1.0-pro-vision-latest')
        text_prompt = '''
        You are an expert in interpreting medical examinations and providing optimal recommendations. 
        You will analyze images containing medical examination data. 
        Initially, explain the significance of the data presented. 
        It is important to maintain a positive outlook throughout your analysis and mention the name (if it exists) to personalize and make it kind. 
        Always ensure to include the advice of a specialist doctor for more detailed information and a comprehensive understanding. 
        Please respond in simple, direct Arabic without using complex terms.
        Finally say "مع خالص التقدير روبرتو"'''
        response = model.generate_content([text_prompt, img])
        return response.text
    except Exception as e:
        st.error("Failed to generate content: {}".format(e))
        return None

def generate_audio(text, voice="Rachel", model="eleven_multilingual_v2"):
    load_dotenv()
    elevenlabs_api_key = os.getenv('ELEVENLABS_API_KEY')
    elevenlabs_client = ElevenLabs(api_key=elevenlabs_api_key)
    
    try:
        audio_generator = elevenlabs_client.generate(text=text, voice=voice, model=model)
        audio_data = b"".join(audio_generator)
        return audio_data
    except Exception as e:
        print(f"Error generating audio: {e}")
        return None

def process_and_save_audio(input_text, output_directory):
    segments = input_text.split('\n\n')
    os.makedirs(output_directory, exist_ok=True)
    for i, segment in enumerate(segments):
        if segment.strip():
            audio = generate_audio(segment)
            if audio is None:
                continue
            file_name = f"{i+1:02}.mp3"
            file_path = os.path.join(output_directory, file_name)
            with open(file_path, "wb") as file:
                file.write(audio)

def combine_mp3_files(directory, output_filename):
    files = sorted([f for f in os.listdir(directory) if f.endswith('.mp3')])
    output_path = os.path.join(directory, output_filename)
    with open(output_path, 'wb') as outfile:
        for filename in files:
            file_path = os.path.join(directory, filename)
            with open(file_path, 'rb') as infile:
                outfile.write(infile.read())
    print("Files combined into:", output_path)

# Streamlit app setup

import streamlit as st
from PIL import Image
import io

def main():
    logo_path = "C:\\Users\\Motasem-PC\\Desktop\\reporto\\Data\\reporto.png"  # Replace with the actual path to your logo
    logo = st.image(logo_path, width=100)  # Adjust width as needed
    st.title("Reporto")
    st.markdown("##### Skip the Wait, Not the Detail: Fast AI Lab Analysis")
    st.markdown("### Overview")
    st.markdown("""
    In many regions, the manual analysis of lab reports is slow, error-prone, and often hindered by the scarcity of healthcare providers. 
    This project addresses these challenges by introducing an AI-powered application designed to automate and enhance the analysis and interpretation of lab reports, reducing wait times and the anxiety associated with them.
    """)

    img_file_buffer = st.file_uploader("Upload an image (jpg, png):", type=["jpg", "png"])
    img = None
    if img_file_buffer is not None:
        # Convert the file buffer to an image object
        img = Image.open(io.BytesIO(img_file_buffer.getvalue()))

    if st.button("Generate Report"):
        if img:
            # Generate content based on text and image
            processed_text = generate_content(img)
            st.markdown(f"<div style='direction: rtl; text-align: right;'>{processed_text}</div>", unsafe_allow_html=True)  # Display the result from generate_content

            # Process audio and combine files
            output_dir = "./audio_reports"
            process_and_save_audio(processed_text, output_dir)
            combine_mp3_files(output_dir, "final_report.mp3")
            st.success("Audio report generated! Check the './audio_reports' folder for the output.")
        else:
            st.error("Please provide both text and an image.")
        
        # Assuming the audio processing functions create a final audio file called 'final_report.mp3' in the './audio_reports' folder
        output_dir = "./audio_reports"
        process_and_save_audio(processed_text, output_dir)
        combine_mp3_files(output_dir, "final_report.mp3")
        st.success("Audio report generated! Check the './audio_reports' folder for the output.")

        # Display the audio player
        audio_file_path = os.path.join(output_dir, "final_report.mp3")
        if os.path.isfile(audio_file_path):
            audio_file = open(audio_file_path, "rb")
            st.audio(audio_file.read(), format="audio/mp3")
            audio_file.close()
        else:
            st.error("Audio file not found. Please ensure the audio generation process is correct.")
    else:
        st.error("Please upload an image to generate the report.")


if __name__ == "__main__":
    load_dotenv()
    gemini_api_key = os.getenv('GEMINI_API_KEY')
    main()

