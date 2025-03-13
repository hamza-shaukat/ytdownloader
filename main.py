import yt_dlp

def download_video(video_url, output_path='downloads/%(title)s.%(ext)s'):
    ydl_opts = {
        'outtmpl': output_path,  # Set output file name pattern
        'format': 'bestvideo+bestaudio/best',  # Download best video and audio
        'merge_output_format': 'mp4',  # Ensure output is in MP4 format
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

if __name__ == "__main__":
    video_url = input("Enter YouTube video URL: ")
    download_video(video_url)
    print("Download complete!")
