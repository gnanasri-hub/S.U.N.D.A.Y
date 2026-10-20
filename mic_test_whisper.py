import sounddevice as sd
import soundfile as sf

from faster_whisper import WhisperModel

model = WhisperModel(
    "medium",
    device="cpu"
)

duration = 8
sample_rate = 16000

print("🎤 Speak after 3 seconds...")

import time
time.sleep(3)

print("🎙️ RECORDING")

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

print("✅ Saved")

segments, info = model.transcribe(
    "voice.wav",
    language="en",
    beam_size=5
)

text = ""

for segment in segments:
    text += segment.text

print("\nTRANSCRIPT:")
print(text)