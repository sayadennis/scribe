# scribe: transcribing interviews using pre-trained models

Testing out audio transcription using pre-trained models downloaded via Huggingface for interviews.

## Workflow memo

1. Record audio interview
2. Convert `m4a` format to `mp3` format using `ffmpeg`
3. Auto-transcribe `mp3` file with pre-trained model and write to `txt` format
4. Listen to audio and manually check/fix transcription
5. Write up summary based on corrected transcript

