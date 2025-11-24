Video Communication Analyzer
Streamlit Cloud–Compatible Version

Created by: <Your Name>

📌 Overview

The Video Communication Analyzer is a Streamlit-based web application that allows users to:

Upload an MP4 file or paste a YouTube URL

Automatically extract the audio

Generate a transcript using a lightweight online transcription API

Measure a Clarity Score based on filler words

Identify the Main Focus Sentence

Download the transcript

This version is specially optimized to run on Streamlit Cloud (no Whisper / no heavy dependencies).

🚀 Features
✔ Extract Audio

Extracts audio directly from an uploaded MP4 video or YouTube link.

✔ Transcription

Transcribes speech using a free cloud API compatible with Streamlit Cloud.

✔ Clarity Score

Calculates clarity based on filler word density.

✔ Focus Sentence

Identifies the longest, most content-rich sentence from the transcript.

✔ Deployable on Streamlit Cloud

Designed to avoid heavy libraries (whisper, torch, moviepy, scipy) that Streamlit cannot install.
