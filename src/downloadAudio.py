import os
import yt_dlp
from collections import deque

from helper import ensure_https, format_query

cur_dir= os.path.dirname(os.path.abspath(__file__))

song_queue = deque()

def main(url_or_query):
    allocate_queue(format_query(url_or_query))
        

def download_audio(url_or_query):

    ydl_opts = {
        'format': 'bestaudio/best',  # Best audio format
        'prefer_insecure': False,  # Force https
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'm4a',  # Change to 'mp4' if needed
            'preferredquality': '128',
        }],
        'outtmpl': f"{cur_dir}/output/audio.%(ext)s",  # Output filename
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([ensure_https(url_or_query)])


def allocate_queue(url_array):
    for entry in extract_entries(url_array):
        song_queue.append({
            'title': entry['title'],
            'url': f"https://www.youtube.com/watch?v={entry['id']}"
    })

def extract_entries(query_or_url):
    ydl_opts = {
        'quiet': True,
        'extract_flat': True,
        'skip_download': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(query_or_url, download=False)

        # If it's a playlist or search, it'll have 'entries'
        if 'entries' in info:
            return info['entries']
        else:
            # Single video URL (not a playlist)
            return [info]






# Example usage
download_audio("https://www.youtube.com/watch?v=jXwgShqzVas")
# download_audio("http://www.youtube.com/watch?v=o9UQSUHHdtA")
