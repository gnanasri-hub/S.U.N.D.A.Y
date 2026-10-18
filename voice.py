import asyncio
import edge_tts
# pyrefly: ignore[missing-import]
from playsound3 import playsound
import os


VOICE = "en-US-AriaNeural"

def speak(text):

    print("Sunday:", text)

    async def generate():

        communicate = edge_tts.Communicate(
            text,
            VOICE
        )

        await communicate.save("voice.mp3")

    asyncio.run(generate())

    playsound("voice.mp3")

    if os.path.exists("voice.mp3"):
        os.remove("voice.mp3")