
# 📹 M3U8 Video Scraper

This is a Python script to download M3U8 videos and create a corresponding text file with user-provided prompts. The video is downloaded using `yt-dlp` and requires Firefox cookies for authentication.

## ✨ Features

- 📥 Downloads M3U8 videos using the video URL.
- 💾 Saves the video with a user-defined name.
- 📝 Creates a text file with user-provided prompts and names it after the video (I added this for video descriptions).

## 📋 Requirements

- 🐍 Python 3.x
- `yt-dlp`
- 🌐 Firefox browser (for cookies)

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/BoranCanOzel/m3u8-Video-Scraper.git
   cd m3u8-video-scraper
   ```

2. Install `yt-dlp`:
   ```bash
   pip install yt-dlp
   ```

## 🍪 Firefox Cookies

The program automatically uses your Firefox cookies. This means that if the website you are downloading from requires authentication, the script will still be able to download the video without any additional steps from you. Ensure you are logged into the website in Firefox before running the script.

## 🚀 Usage

1. Ensure you have the necessary cookies from Firefox.
2. Run the script:
   ```bash
   python d.py
   ```

3. Follow the prompts:
   - Enter the video name (e.g., `4 HOW TO CREATE A DATABASE.mp4`).
   - Enter the video URL (e.g., `https://fast.wistia.com/embed/medias/zqa31qweoyj.m3u8`).
   - Enter the prompt text (type `END` on a new line to finish).

4. The video will be downloaded, and a text file with the same name as the video will be created containing your prompts.

## 🛠️ Example

```bash
$ python scraper.py
Enter the video name: example_video.mp4
Enter the video URL: https://fast.wistia.com/embed/medias/zqa31qweoyj.m3u8
Enter the prompt text (type 'END' on a new line to finish):
This is an example prompt.
It can be multiple lines.
END
Video downloaded and text file 'example_video.txt' created.
```

