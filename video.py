from yt_dlp import YoutubeDL
import whisper
import argparse


def download_video(url, output_path="/output/video.mp4", max_filesize="500MB"):
    options = {
        "format": "bestvideo+bestaudio/best",
        "outtmpl": output_path,
        "filesize_limit": max_filesize,
    }
    with YoutubeDL(options) as ydl:
        ydl.download([url])


def transcribe_video(video_path, output_path="/output/output_subtitles.srt"):
    # Load the Whisper model
    model = whisper.load_model("large")  # Use "large" for the best accuracy

    # Transcribe the video
    result = model.transcribe(video_path, task="translate", language=None)

    # Save as SRT

    with open(output_path, "w", encoding="utf-8") as file:
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


def main():
    # Create the argument parser
    parser = argparse.ArgumentParser(description="Video Transcriber Tool")

    # Add arguments
    parser.add_argument(
        "--youtube-url",
        type=str,
        help="URL of the YouTube video to transcribe",
        required=False,
    )
    parser.add_argument(
        "--language",
        type=str,
        help="Language code for transcription (e.g., en for English)",
        required=True,
    )
    parser.add_argument(
        "--input",
        type=str,
        help="Path to the local video file to transcribe",
        required=False,
    )
    parser.add_argument(
        "--output", type=str, help="Custom output file path (optional)", required=False
    )

    # Parse the arguments
    args = parser.parse_args()

    # Print or use the arguments
    if args.youtube_url:
        print(
            f"Transcribing YouTube URL: {args.youtube_url} in {args.language} language."
        )
        download_video(args.youtube_url, "downloaded_video.mp4")
        transcribe_video("downloaded_video.mp4.webm")
    elif args.input:
        print(f"Transcribing local file: {args.input} in {args.language} language.")
        download_video(args.input, "downloaded_video.mp4")
        transcribe_video("downloaded_video.mp4")
    else:
        print("No input provided. Please specify either --youtube-url or --input.")

    if args.output:
        print(f"Output will be saved to: {args.output}")
    else:
        print("Using default output location.")


if __name__ == "__main__":
    main()

# Main execution
