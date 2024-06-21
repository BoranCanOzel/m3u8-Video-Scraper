
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
   git clone https://github.com/yourusername/m3u8-video-scraper.git
   cd m3u8-video-scraper
   ```

2. Install `yt-dlp`:
   ```bash
   pip install yt-dlp
   ```

## 🍪 Obtaining Firefox Cookies

To download videos that require authentication, you need to provide cookies from your Firefox browser:

1. Install the `Get cookies.txt` extension for Firefox.
2. Navigate to the website and log in.
3. Click the extension icon and download the cookies as `cookies.txt`.
4. Ensure the `cookies.txt` file is in the same directory as your script.

## 🚀 Usage

1. Ensure you have the necessary cookies from Firefox.
2. Run the script:
   ```bash
   python d.py
   ```

3. Follow the prompts:
   - Enter the video name (e.g., `4 Don't Try to imitate HOW I SPEAK.mp4`).
   - Enter the video URL (e.g., `https://fast.wistia.com/embed/medias/zqa96s9oyj.m3u8`).
   - Enter the prompt text (type `END` on a new line to finish).

4. The video will be downloaded, and a text file with the same name as the video will be created containing your prompts.

## 🛠️ Example

```bash
$ python scraper.py
Enter the video name: example_video.mp4
Enter the video URL: https://fast.wistia.com/embed/medias/zqa56hfyj.m3u8
Enter the prompt text (type 'END' on a new line to finish):
This is an example prompt.
It can be multiple lines.
END
Video downloaded and text file 'example_video.txt' created.
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📜 License

This project is licensed under the MIT License.
