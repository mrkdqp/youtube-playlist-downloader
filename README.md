# YouTube Playlist Downloader

## Description
The YouTube Playlist Downloader is a Python script that retrieves and downloads a specified number of videos from a given YouTube playlist. It uses Selenium to extract video links from the playlist and `yt-dlp` to handle the video downloads. This tool is useful for downloading a batch of videos from YouTube playlists for offline viewing or archival purposes.

## Release Notes

### Version 2.0

- **Enhanced Resolution Options:** Users can now choose to download videos in 360p or all resolutions up to 1080p that the youtube video has. This provides greater flexibility in selecting video quality based on user preferences or available storage space.
- **MP3 Option:** Users can now choose to download videos in .mp3 format. This provides greater flexibility, especially when downloading music videos.
- **Improved Error Handling:** Enhanced mechanisms for handling errors and providing more informative feedback if something goes wrong during video retrieval or downloading.
- **User Interface Enhancements:** Updated prompts and user interactions for a smoother experience when specifying download options.

## Features

- **Video Retrieval:** Extracts video links from a YouTube playlist using Selenium.
- **Download Limitation:** Allows the user to specify the number of videos to download.
- **Video Downloading:** Uses `yt-dlp` to download videos in the best available format.
- **Progress Tracking:** Displays download progress in the terminal.
- **Resolution Selection:** Choose to download videos in 360p or all resolutions up to 1080p.

## Requirements

- Python 3.x
- Selenium
- WebDriver Manager
- `yt-dlp`
- **`ffmpeg` (Optional)**: Required if you choose to download videos in a resolution higher than 360p.

## Installation

To install all the required modules, use the `install.txt` file provided:

1. **Install the required modules** using the `install.txt` file:

   ```bash
   pip install -r install.txt
   ```

2. **Install `ffmpeg`** (only if downloading videos in higher resolutions):
   - **For Windows**: Download the `ffmpeg` executable from the [official website](https://ffmpeg.org/download.html) and add it to your system PATH.
   - **For macOS**: Install `ffmpeg` using Homebrew:
     ```bash
     brew install ffmpeg
     ```
   - **For Linux**: Install `ffmpeg` using your package manager:
     ```bash
     sudo apt-get install ffmpeg  # For Debian-based distributions
     sudo yum install ffmpeg      # For Red Hat-based distributions
     ```

Make sure you also have a compatible version of Chrome installed, as the script uses Chrome WebDriver.

## Running the Script
To execute the script, follow these steps:

1. **Clone or Download the Repository**: Ensure you have the script file (`app.py`) in your working directory.

2. **Navigate to the Script Directory**: Open your terminal and change to the directory containing the script.

3. **Run the Script**: Execute the script by running:
   ```bash
   python app.py
   ```

4. **Follow the Prompts**: Enter a PUBLIC or UNLISTED YouTube playlist URL and the maximum number of videos you want to retrieve when prompted.

5. **View Download Progress**: The script will display the progress of the video retrieval and downloading process in the terminal.

## Example
```bash
Enter a Public or Unlisted YouTube playlist URL: https://www.youtube.com/playlist?list=PL0vfts4VzfNjdPuyk9SJDIvpsOjNgU1bs
Enter the maximum number of videos to retrieve: 2
Choose Resolution:
1) 360p
2) up to 1080p
3) .mp3
Choose Number: 2
```

With this example, the script will retrieve up to 2 video links from the playlist and download them into a `downloads` directory within the current script directory.

## Take Note

- **Public or Unlisted Links Only:** The script only works with PUBLIC or UNLISTED YouTube playlist URLs. PRIVATE playlists will not be accessible.
- **Maximum Playlist Size:** Be aware of the maximum number of videos in the playlist. If the playlist contains more videos than specified, the script might take longer to complete as it processes the entire playlist to find the required number of videos.
- **Resolution and `ffmpeg`:** If you select a video resolution higher than 360p, make sure `ffmpeg` is installed. Without `ffmpeg`, the script may not be able to process higher-resolution downloads.
