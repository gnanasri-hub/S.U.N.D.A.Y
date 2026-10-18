from listen import listen
from voice import speak
from brain import think
from wakeword import is_awake

speak("Sunday is online.")

while True:

    command = listen()
    print("RAW COMMAND:", command)

    if command is None:
        continue

    print("You:", command)

    if "stop" in command.lower():
        speak("Goodbye ma'am")
        break

    if not is_awake(command):
        continue

    command = command.replace(
        "sunday",
        ""
    ).strip()

    response = think(command)

    print("Sunday:", response)

    speak(response)