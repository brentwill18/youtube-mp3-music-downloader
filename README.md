<h2 align = "center">Youtube MP3 Music Downloader</h2>
---

A Python-based tool that allows you to download **specifically** Youtube music videos and **converts** the file to a **mp3** file.

**Must have FFMPEG installed (https://ffmpeg.org/download.html) in your system PATH** <br />
**Must have your own Youtube API key**

---

## Features

- Download **Youtube music videos**
- Converts file into `.mp3` files
- Option to clear all downloaded music videos from a list

---

## Requirements

- Python **3.8+**
- Libraries:
  - `ffmpeg` for audio file handling
  - `yt-dlp` for downloading Youtube videos/audio
  - `google-api-python-client` for interacting with the Youtube API
  - `python-dotenv` for API key information
  - `requests` (used for URL checking)  
  
---

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/brentwill18/youtube-mp3-music-downloader.git
   cd "Youtube MP3 Music Downloader"

2. Install the required libraries first:
   ```bash
   pip install -r requirements.txt

3. Put your youtube API key in the .env file:
    ```bash
   YOUTUBE_API_KEY = "YOUR_API_KEY"

4. Run the `download_osts.py` file
