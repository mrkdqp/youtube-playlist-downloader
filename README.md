# YouTube Playlist Downloader

## Description
The YouTube Playlist Downloader is a Python script that retrieves and downloads a specified number of videos from a given YouTube playlist. It uses Selenium to extract video links from the playlist and `yt-dlp` to handle the video downloads. This tool is useful for downloading a batch of videos from YouTube playlists for offline viewing or archival purposes.

## Features

- **Video Retrieval:** Extracts video links from a YouTube playlist using Selenium.
- **Download Limitation:** Allows the user to specify the number of videos to download.
- **Video Downloading:** Uses `yt-dlp` to download videos in the best available format.
- **Progress Tracking:** Displays download progress in the terminal.

## Requirements

- Python 3.x
- Selenium
- WebDriver Manager
- `yt-dlp`

## Installation

To install all the required modules, use the `install.txt` file provided:

1. **Install the required modules** using the `install.txt` file:

   ```bash
   pip install -r install.txt
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
```

With this example, the script will retrieve up to 2 video links from the playlist and download them into a `downloads` directory within the current script directory.

## Take Note

- **Public or Unlisted Links Only:** The script only works with PUBLIC or UNLISTED YouTube playlist URLs. PRIVATE playlists will not be accessible.
- **Maximum Playlist Size:** Be aware of the maximum number of videos in the playlist. If the playlist contains more videos than specified, the script might take longer to complete as it processes the entire playlist to find the required number of videos. 