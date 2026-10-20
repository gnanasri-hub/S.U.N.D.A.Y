import sounddevice as sd
import soundfile as sf

from faster_whisper import WhisperModel

model = WhisperModel(
    "medium",
    device="cpu"
)

def listen():

    duration = 4
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

    segments, info = model.transcribe(
        "voice.wav",
        language="en",
        beam_size=5
    )

    text = ""

    for segment in segments:
        text += segment.text

    text = text.strip()

    if text:

        print("🗣️ You:", text)

        return text.lower()

    return None