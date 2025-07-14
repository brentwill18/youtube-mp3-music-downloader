import os
import re
import requests
import urllib.parse as urlparse
from dotenv import load_dotenv
from yt_dlp import YoutubeDL
from googleapiclient.discovery import build

load_dotenv()

API_KEY = os.getenv("YOUTUBE_API_KEY")

youtube = build("youtube", "v3", developerKey = API_KEY)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data", "songs")

ydl_opts = {
    "format": "bestaudio/best",
    "outtmpl": os.path.join(DATA_DIR, "%(title)s.%(ext)s"),
    "noplaylist": True,
    "quiet": True,
    "postprocessors": [{
        "key": "FFmpegExtractAudio",
        "preferredcodec": "mp3",
        "preferredquality": "256",
    }]
}

def is_music_video(video_id):
    request = youtube.videos().list(
        part = "snippet",
        id = video_id
    )

    response = request.execute()

    if "items" not in response or len(response["items"]) == 0:
        print("Video not found!")
        return False
    
    video = response["items"][0]
    category_id = video["snippet"]["categoryId"]

    if category_id != "10":
        print(f"Video category ID: {category_id}")

    return category_id == "10"

def get_video_id(video_url):
    parsed = urlparse.urlparse(video_url)
    if parsed.hostname.lower() == "youtu.be":
        return parsed.path[1:]
    
    if parsed.hostname.lower() in ("www.youtube.com", "youtube.com"):
        query = urlparse.parse_qs(parsed.query)
        return query.get("v", [None])[0]
    
    return None

def is_yt_link(text):
    return re.match(r"https?://(www\.)?(youtube\.com|youtu\.be)/", text)

def remove_videos():
    song_files = os.listdir(DATA_DIR)
    for f in song_files:
        file_path = os.path.join(DATA_DIR, f)
        if os.path.isfile(file_path) and f.endswith(".mp3"):
            os.remove(file_path)
            print(f"Removed {len(song_files)} videos from the songlist!")

with YoutubeDL(ydl_opts) as ydl:
    print("Input 'quit' or 'exit' to stop program from running")
    print("Input 'clear' to remove all the files within the music folder")
    while True:
        video_url = input("Enter music video: ").strip()

        if video_url in ("quit", "exit"):
            break

        if video_url in ("clear"):
            remove_videos()
            continue

        if is_yt_link(video_url):
            video_id = get_video_id(video_url)
            if video_id is None:
                print("Could not extract video ID from video!")
                continue

            if is_music_video(video_id):
                ydl.download([video_url])

            else:
                print("This video is not categorized as music!")
            
        else:
            print("Invalid Youtube link!\n")
                       

