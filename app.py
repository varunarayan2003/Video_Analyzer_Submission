import streamlit as st
from utils import download_video_then_extract_audio
import requests
import tempfile
import re

st.set_page_config(page_title="Video Communication Analyzer", layout="centered")
st.title("🎤 Video Communication Analyzer (Streamlit Cloud Version)")

url_input = st.text_input("YouTube URL:")
uploaded_file = st.file_uploader("Upload MP4:", type=["mp4"])
analyze_btn = st.button("Analyze")

TRANSCRIBE_API = "https://api.groq.com/open-source/whisper-small"
sentence_split = re.compile(r'(?<=[.!?])\s+')

def calc_clarity(text):
    words = text.lower().split()
    fillers = ["um","uh","like","you","know","i","mean","so","actually","basically"]
    filler_count = sum(w in fillers for w in words)
    score = 100 - min(50, filler_count)
    return max(0, score)

def calc_focus(text):
    sentences = sentence_split.split(text)
    return max(sentences, key=len).strip()

def transcribe(audio_path):
    with open(audio_path, "rb") as f:
        resp = requests.post(
            TRANSCRIBE_API,
            files={"file": ("audio.wav", f, "audio/wav")}
        )
    return resp.json().get("text", "")

if analyze_btn:
    if not url_input and not uploaded_file:
        st.error("Enter URL or upload file.")
        st.stop()

    with st.spinner("Extracting audio..."):
        if uploaded_file:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as tmp:
                tmp.write(uploaded_file.read())
                video = tmp.name
            audio = download_video_then_extract_audio(video, True)
        else:
            audio = download_video_then_extract_audio(url_input, False)

    with st.spinner("Transcribing..."):
        text = transcribe(audio)

    st.subheader("Transcript")
    st.write(text)

    clarity = calc_clarity(text)
    focus = calc_focus(text)

    st.metric("Clarity Score", f"{clarity}%")
    st.subheader("Focus Sentence")
    st.write(focus)
