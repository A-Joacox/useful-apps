from pytube import YouTube #in console: pip install pytube

def download_video_youtube(url, path='.'):
    try:
        yt = YouTube(url)
        
        stream = yt.streams.get_highest_resolution() #you can set the resolution
        
        print(f"Downloading {yt.title}...")
        stream.download(output_path=path)
        print("\ndownload complete")
        
    except Exception as e:
        print(f"An error occurred: {e}")


url = 'https://www.youtube.com/watch?v=YOUR_VIDEO_ID'
path = 'path_to_save_video'  # e.g., '/path/to/download/folder'
download_video_youtube(url, path)