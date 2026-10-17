from voice import speak
from listen import listen
from commands import execute

speak("Hello ma'am. Jarvis is online.")

command = listen()

print("Command received:", command)

if command is not None:

    response = execute(command)

    if response:
        speak(response)