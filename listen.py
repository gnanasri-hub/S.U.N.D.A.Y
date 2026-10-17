# pyrefly: ignore[missing-import]
import speech_recognition as sr

r = sr.Recognizer()

r.energy_threshold = 1000
r.dynamic_energy_threshold = True

def listen():

    with sr.Microphone(device_index = 1) as source:


        r.adjust_for_ambient_noise(source, duration=5)
        print("Speak Now")
        audio = r.record(
            source,
            duration=5
        )
        print("Recording finished")

    try:

        text = r.recognize_google(
            audio,
            language="en-US"
        )

        print("🗣️ You:", text)

        return text.lower()

    except Exception as e:
        print("Error:", type(e).__name__)
        return None
