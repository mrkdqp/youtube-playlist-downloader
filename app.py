import concurrent.futures
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import sys
import os
import re
import yt_dlp as youtube_dl

RESET = "\033[0m"
PURPLE = "\033[34m"
GREEN = "\033[32m"

def clean_url(url):
    # Remove extra parameters for a clean URL
    return re.sub(r'&pp=[^&]*', '', url)

def get_video_links(url, max_videos):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration
    chrome_options.add_argument("--window-size=1920x1080")  # Set a default window size
    chrome_options.add_argument("--no-sandbox") 
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    driver.get(url)

    time.sleep(5)  # Wait for the page to load

    video_links = set()
    last_count = 0

    # Check if URL is for a YouTube Channel (videos section)
    if '/videos' in url:
        print(f"\n{PURPLE}Detected a YouTube channel URL. Scraping video links...{RESET}")
        
        while len(video_links) < max_videos:
            elements = driver.find_elements(By.XPATH, '//a[contains(@href, "/watch?v=")]')
            for element in elements:
                href = element.get_attribute('href')
                if href:
                    clean_href = clean_url(href)
                    if clean_href.startswith("https://www.youtube.com/watch?v="):
                        video_links.add(clean_href)
                        if len(video_links) >= max_videos:
                            break
            
            current_count = len(video_links)
            if current_count > last_count:
                percentage = (current_count / max_videos) * 100
                sys.stdout.write(f"\rProgress: {current_count}/{max_videos} ({percentage:.2f}%)")
                sys.stdout.flush()
                last_count = current_count
            
            if len(video_links) < max_videos:
                driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
                time.sleep(5)  # Wait for more videos to load

    else:
        # Handle Playlist URL (same as before)
        print(f"\n{PURPLE}Detected a YouTube playlist URL. Scraping video links...{RESET}")
        while len(video_links) < max_videos:
            elements = driver.find_elements(By.XPATH, '//a[contains(@href, "/watch?v=") or contains(@href, "/shorts/")]')
            for element in elements:
                href = element.get_attribute('href')
                if href:
                    clean_href = clean_url(href)
                    # Ensure it matches a YouTube video or Shorts URL
                    if (clean_href.startswith("https://www.youtube.com/watch?v=") and 'index=' in clean_href) or \
                       (clean_href.startswith("https://www.youtube.com/shorts/")):
                        video_links.add(clean_href)
                        if len(video_links) >= max_videos:
                            break

            current_count = len(video_links)
            if current_count > last_count:
                percentage = (current_count / max_videos) * 100
                sys.stdout.write(f"\rProgress: {current_count}/{max_videos} ({percentage:.2f}%)")
                sys.stdout.flush()
                last_count = current_count

            if len(video_links) < max_videos:
                driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
                time.sleep(5)  # Wait for more videos to load

    driver.quit()

    limited_video_links = list(video_links)[:max_videos]
    print(f"\nCollected {len(limited_video_links)} video links.")
    return limited_video_links

def download_link(link, download_dir, format, merge_output_format, i, total):
    try:
        ydl_opts = {
            'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),
            'format': format,
            'noplaylist': True,
        }

        if merge_output_format == 'mp3':
            ydl_opts['postprocessors'] = [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        elif merge_output_format == 'mp4':
            ydl_opts['format'] = 'bestvideo+bestaudio[ext=mp4]/best[ext=mp4]'

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            print(f"{PURPLE}Downloading video {i}/{total}: {link}{RESET}")
            ydl.download([link])
            print(f"{GREEN}Downloaded {i}/{total}: {link}{RESET}")
    except Exception as e:
        print(f"Failed to download video {i}/{total}: {link}\nError: {e}")

def download(video_links, download_dir, format, merge_output_format):
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    print(f"\n{PURPLE}Number of videos to download: {len(video_links)}{RESET}")

    total = len(video_links)
    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
        futures = [
            executor.submit(download_link, link, download_dir, format, merge_output_format, i+1, total)
            for i, link in enumerate(video_links)
        ]
        for future in concurrent.futures.as_completed(futures):
            future.result()

if __name__ == "__main__":
    url = input("Enter the YouTube playlist or channel URL: ")
    max_videos = int(input("Enter the maximum number of videos to retrieve: "))

    script_dir = os.path.dirname(os.path.abspath(__file__))
    download_dir = os.path.join(script_dir, "downloads")
    
    video_links = get_video_links(url, max_videos)
    
    if len(video_links) < max_videos:
        print(f"\nWarning: Only {len(video_links)} video(s) found, which is less than the requested {max_videos}.")
    
    print(f"\nVideo links (up to {len(video_links)}):")
    
    for i, link in enumerate(video_links, start=1):
        print(f"{i}. {link}")

    print("\nChoose Resolution:")
    print("1) 360p \n2) up to 1080p\n3) .mp3\n")
    choice = int(input("Choose Number: "))
    
    if choice == 1:
        download(video_links, download_dir, format='best', merge_output_format=None)
    elif choice == 2:
        download(video_links, download_dir, format='bestvideo+bestaudio/best', merge_output_format='mp4')
    elif choice == 3:
        download(video_links, download_dir, format='bestaudio/best', merge_output_format='mp3')
    else:
        print("Incorrect Choice!")
