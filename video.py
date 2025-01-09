from yt_dlp import YoutubeDL
import whisper


def download_video(url, output_path="video.mp4", max_filesize="500MB"):
    options = {
        "format": "bestvideo+bestaudio/best",
        "outtmpl": output_path,
        "filesize_limit": max_filesize,
    }
    with YoutubeDL(options) as ydl:
        ydl.download([url])


def transcribe_video(video_path):
    # Load the Whisper model
    model = whisper.load_model("large")  # Use "large" for the best accuracy

    # Transcribe the video
    result = model.transcribe(video_path, task="translate", language=None)

    # Save as SRT

    with open("output_subtitles.srt", "w", encoding="utf-8") as file:
        for segment in result["segments"]:
            start = segment["start"]
            end = segment["end"]
            text = segment["text"]

            # Write in SRT format
            file.write(f"{segment['id'] + 1}\n")
            file.write(f"{format_time(start)} --> {format_time(end)}\n")
            file.write(f"{text}\n\n")

    print("Subtitles saved as output_subtitles.srt")


def format_time(seconds):
    milliseconds = int((seconds % 1) * 1000)
    seconds = int(seconds)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"


# Main execution
video_url = "https://www.youtube.com/watch?v=PLwd4pcGcIw"
download_video(video_url, "downloaded_video.mp4")
transcribe_video("downloaded_video.mp4.webm")
