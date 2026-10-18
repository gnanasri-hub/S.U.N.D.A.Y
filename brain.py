import ollama

from memory import (
    remember,
    get_memory
)

def think(prompt):

    remember(
        "user",
        prompt
    )

    messages = [
        {
            "role": "system",
            "content":
            "You are Sunday, a personal AI assistant created by Gnanasri. Never say you are Qwen or Alibaba Cloud. Act as Sunday."
        }
    ]

    messages.extend(
        get_memory()
    )

    response = ollama.chat(
        model="qwen2.5:7b",
        messages=messages
    )

    reply = response["message"]["content"]

    remember(
        "assistant",
        reply
    )

    return reply