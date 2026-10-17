# pyrefly: ignore[missing-import]
import pyttsx3

engine = pyttsx3.init()

engine.setProperty("rate", 180)

def speak(text):
    print("Jarvis:", text)

    print("Before say")

    engine.say(text)

    print("After say")

    engine.runAndWait()

    print("After runAndWait")