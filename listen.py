# pyrefly: ignore[missing-import]
import speech_recognition as sr

r = sr.Recognizer()

r.energy_threshold = 300
r.dynamic_energy_threshold = True

def listen():

    with sr.Microphone(device_index = 1) as source:


       # r.adjust_for_ambient_noise(source, duration=1)
        print("Get Ready...")

        import time
        time.sleep(2)

        print("🎤 SPEAK NOW")

        audio = r.record(
            source,
            duration=4
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
