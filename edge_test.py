import asyncio
# pyrefly: ignore[missing-import]
import edge_tts

TEXT = "Hello ma'am. Jarvis is online."

async def main():
    communicate = edge_tts.Communicate(
        TEXT,
        "en-US-AriaNeural"
    )

    await communicate.save("voice.mp3")

asyncio.run(main())

print("Done")