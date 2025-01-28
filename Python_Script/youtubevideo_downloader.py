import subprocess

def download_youtube_video():
    # Prompt the user for the YouTube URL
    youtube_url = input("Enter the YouTube URL: ").strip()

    # yt-dlp command
    command = [
        "yt-dlp",
        "-f",
        "bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4",
        youtube_url
    ]

    try:
        # Execute the yt-dlp command
        subprocess.run(command, check=True)
        print("Download completed successfully!")
    except subprocess.CalledProcessError as e:
        print("An error occurred while downloading the video.")
        print(f"Error: {e}")

if __name__ == "__main__":
    download_youtube_video()

