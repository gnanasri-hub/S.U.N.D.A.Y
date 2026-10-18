from listen import listen
from voice import speak
from brain import think

speak("Hello ma'am. Sunday is online.")

while True:

    command = listen()

    if command is None:
        continue

    print("You:", command)

    if command.lower() == "stop":
        speak("Goodbye ma'am")
        break

    response = think(command)

    print("Sunday:", response)

    speak(response)
