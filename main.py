from voice import speak
from listen import listen
from commands import execute

speak("Hello ma'am. Sunday is online.")

while True:

    command = listen()

    if command is None:
        continue

    print("Command received:", command)

    response = execute(command)

    if response:
        speak(response)

    if "stop" in command:
        speak("Goodbye ma'am")
        break