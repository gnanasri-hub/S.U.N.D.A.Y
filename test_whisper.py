from faster_whisper import WhisperModel

model = WhisperModel(
    "base",
    device="cpu"
)

segments, info = model.transcribe(
    "voice.wav"
)

for segment in segments:
    print(segment.text)