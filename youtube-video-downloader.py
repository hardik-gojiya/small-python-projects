from pytube import YouTube
import os

def download_video():
    url = input("Enter the YouTube video URL: ")
    if not url.startswith(('https://www.youtube.com', 'https://youtu.be')):
        print("Invalid URL! Please enter a valid YouTube URL.")
        return
    try:
        yt = YouTube(url)
        print(f"Title: {yt.title}")
        
        print("Available Video Streams:")
        for stream in yt.streams.filter(progressive=True, file_extension="mp4"):
            print(f"{stream.itag}: {stream.resolution} - {stream.mime_type}")
        
        print("Available Audio Streams:")
        for stream in yt.streams.filter(only_audio=True):
            print(f"{stream.itag}: Audio - {stream.mime_type}")
        
        itag = input("Enter the itag of the stream you want to download: ")
        stream = yt.streams.get_by_itag(itag)
        
        if stream:
            path = input("Enter the download path (leave empty for current directory): ")
            path = path if path else os.getcwd()
            
            print("Downloading...")
            stream.download(output_path=path)
            print(f"Download complete! File saved in: {path}")
        else:
            print("Invalid itag. Please try again.")
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    download_video()
