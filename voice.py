import asyncio
import edge_tts
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

    # pyrefly: ignore[deprecated]
    os.system("start voice.mp3")