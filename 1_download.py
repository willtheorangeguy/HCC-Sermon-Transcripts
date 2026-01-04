"""
This script uses yt-dlp to download videos, by year, from the HCC
YouTube Channel sermon playlist.
"""

import yt_dlp

def download_playlist(playlist_url):
    """
    Downloads all videos from a YouTube playlist.
    """
    ydl_opts = {
        "format": "bestaudio",
        "noplaylist": False,
        "ignoreerrors": True,
        "download_archive": "downloaded.log",
        "outtmpl": "%(upload_date>%Y)s/%(title)s.%(ext)s",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "0",
            }
        ],
        "keepvideo": False,
        "remote_components": "ejs:github"
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])


if __name__ == "__main__":
    playlist = "https://www.youtube.com/playlist?list=PLvQNIIJjMEtotz4aW1lpSwLzqOXGvZpoG"
    download_playlist(playlist)
    print("Downloaded all videos from the HCC YouTube channel.")
