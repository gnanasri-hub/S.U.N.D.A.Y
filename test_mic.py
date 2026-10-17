# pyrefly: ignore[missing-import]
import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone(device_index=1) as source:

    print("Wait...")

    r.adjust_for_ambient_noise(source, duration=2)

    print("Speak now!")

    audio = r.record(source, duration=5)

print("Finished recording")

try:
    text = r.recognize_google(audio)

    print("You said:", text)

except Exception as e:

    print(type(e).__name__)