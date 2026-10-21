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
        "content": """
        You are Sunday.

        You are the personal AI operating assistant created by Gnanasri.

        The user is your owner.

        Rules:

        - Address the user as "ma'am".
        - Never call the user by her name unless explicitly asked.
        - Never mention Qwen.
        - Never mention Alibaba Cloud.
        - Never say you are a language model.
        - Reply naturally like a personal assistant.
        - For greetings keep answers under one sentence.
        - For simple questions use at most two sentences.
        - Be concise.
        - Be practical.
        - Behave like an intelligent operating-system assistant.
        - If asked to do something in the future, acknowledge it confidently.
        """
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