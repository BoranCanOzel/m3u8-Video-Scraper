import os
import subprocess


def main():
    # Get user inputs
    video_name = input(
        "Enter the video name (e.g., 4 How to create a database.mp4): ")
    if not video_name.endswith(".mp4"):
        video_name += ".mp4"

    video_url = input(
        "Enter the video URL (e.g., https://fast.wistia.com/embed/medias/zqa45345j.m3u8): ")

    print("Enter the prompt text (type 'END' on a new line to finish):")
    prompt_lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        prompt_lines.append(line)
    prompt_text = "\n".join(prompt_lines)

    # Run the yt-dlp command
    command = f'yt-dlp --cookies-from-browser=firefox -o "{video_name}" {video_url}'
    subprocess.run(command, shell=True)

    # Create a text file with the same name as the video
    text_file_name = video_name.rsplit('.', 1)[0] + ".txt"
    with open(text_file_name, 'w') as text_file:
        text_file.write(prompt_text)

    print(f"Video downloaded and text file '{text_file_name}' created.")


if __name__ == "__main__":
    main()
