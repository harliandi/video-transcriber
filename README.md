# Video Transcriber

A Python-based tool that transcribes video files into text with support for multiple languages. It processes video files, extracts audio, and generates accurate transcriptions using advanced AI models.

## Features

- Supports video transcription from local files and YouTube URLs.
- Processes video files under 1GB.
- Provides transcriptions in the desired language while preserving context and nuance.
- Utilizes advanced AI models for high accuracy.

## Prerequisites

- Python 3.8 or higher
- FFmpeg (for audio extraction)
- Whisper (OpenAI's speech-to-text model)
- Required Python packages (specified in `requirements.txt`)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/harliandi/video-transcriber.git
   cd video-transcriber
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure FFmpeg is installed on your system. For installation:
   - **Linux:**
     ```bash
     sudo apt install ffmpeg
     ```
   - **MacOS:**
     ```bash
     brew install ffmpeg
     ```
   - **Windows:** Download and install FFmpeg from [https://ffmpeg.org](https://ffmpeg.org).

## Usage

### Transcribing a Local Video File

1. Place your video file in the `videos` directory.
2. Run the transcriber:
   ```bash
   python transcriber.py --input videos/example.mp4 --language en
   ```
3. The transcription will be saved as a text file in the `output` directory.

### Transcribing a YouTube Video

1. Run the transcriber with the YouTube URL:
   ```bash
   python transcriber.py --youtube-url "https://www.youtube.com/watch?v=example" --language en
   ```
2. The video will be downloaded, processed, and transcribed. The text file will be saved in the `output` directory.

## Arguments

| Argument         | Description                                                   |
|------------------|---------------------------------------------------------------|
| `--input`        | Path to the local video file to transcribe.                   |
| `--youtube-url`  | URL of the YouTube video to transcribe.                       |
| `--language`     | Language code for transcription (e.g., `en` for English).     |
| `--output`       | Custom output file path (optional).                           |

## Examples

### Example 1: Transcribe Local Video
```bash
python transcriber.py --input videos/sample.mp4 --language en
```

### Example 2: Transcribe YouTube Video
```bash
python transcriber.py --youtube-url "https://youtu.be/xyz123" --language es
```

## Output
- Transcriptions are saved as `.txt` files in the `output` directory by default.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## Acknowledgments

- [OpenAI Whisper](https://github.com/openai/whisper) for the transcription model.
- [FFmpeg](https://ffmpeg.org) for audio processing.
