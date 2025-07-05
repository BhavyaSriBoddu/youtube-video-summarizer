import streamlit as st
import yt_dlp
import os
import re
import time
import webvtt
import google.generativeai as genai

# Function to extract video ID
def get_video_id(url):
    match = re.search(r"v=([^&]+)", url)
    return match.group(1) if match else None

# Function to download captions using yt-dlp
def download_captions(video_url, output_dir='captions'):
    ydl_opts = {
        'skip_download': True,
        'writesubtitles': True,
        'writeautomaticsub': True,
        'subtitleslangs': ['en'],
        'subtitlesformat': 'vtt',
        'outtmpl': os.path.join(output_dir, '%(id)s.%(ext)s')
    }

    os.makedirs(output_dir, exist_ok=True)

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url, download=True)
        video_id = info.get('id')

    vtt_path = os.path.join(output_dir, f"{video_id}.en.vtt")
    return vtt_path

# Function to convert .vtt to plain text
def vtt_to_text(vtt_path):
    captions = [caption.text.strip() for caption in webvtt.read(vtt_path)]
    return " ".join(captions)

# Gemini API call
def call_gemini_api(prompt, transcript):
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel("gemini-2.0-flash")
    time.sleep(5)  # To respect rate limits
    response = model.generate_content(f"{prompt}\n\nTranscript:\n{transcript}")
    return response.text

# Streamlit UI
st.title("🎥 YouTube Video Summarizer Using AI")

video_url = st.text_input("Enter YouTube Video URL")
user_prompt = st.text_input("Enter your prompt (e.g., 'Summarize the video')")

if st.button("Generate"):
    if video_url and user_prompt:
        with st.spinner("Downloading captions..."):
            try:
                vtt_path = download_captions(video_url)
            except Exception as e:
                st.error(f"Failed to download captions: {e}")
                st.stop()

        with st.spinner("Extracting text from captions..."):
            try:
                transcript = vtt_to_text(vtt_path)
            except Exception as e:
                st.error(f"Error reading captions: {e}")
                st.stop()

        if transcript:
            prompt = (
                "You are an expert assistant.\n"
                "Analyze the following YouTube video transcript.\n"
                f"User Request: {user_prompt}\n\n"
                "Transcript:\n"
                f"{transcript}"
            )
            with st.spinner("Generating response using Gemini..."):
                try:
                    result = call_gemini_api(prompt, transcript)
                    st.subheader("Result:")
                    st.write(result)
                except Exception as e:
                    st.error(f"Gemini error: {e}")
        else:
            st.warning("Transcript could not be extracted.")
    else:
        st.warning("Please enter both a YouTube URL and a prompt.")
