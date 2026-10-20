# test_whisper_record.py

import sounddevice as sd
import soundfile as sf
from faster_whisper import WhisperModel

duration = 5
sample_rate = 16000

print("🎤 Speak now...")

audio = sd.rec(
    int(duration * sample_rate),
    samplerate=sample_rate,
    channels=1
)

sd.wait()

sf.write(
    "voice.wav",
    audio,
    sample_rate
)

print("✅ Recording saved")

model = WhisperModel(
    "medium",
    device="cpu"
)

segments, info = model.transcribe(
    "voice.wav",
    language="en"
)

print("\nTRANSCRIPT:")

for segment in segments:
    print(segment.text)