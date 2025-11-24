from pytube import YouTube
from pydub import AudioSegment
import tempfile
import os

def download_video_then_extract_audio(source: str, is_local=False):
    if is_local:
        video_path = source
    else:
        yt = YouTube(source)
        stream = yt.streams.filter(file_extension="mp4").first()
        video_path = stream.download()

    audio = AudioSegment.from_file(video_path)
    temp_audio = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    audio.export(temp_audio.name, format="wav")
    return temp_audio.name
