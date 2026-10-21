from listen import listen
from voice import speak
from brain import think
from wakeword import is_awake
from tools import execute


speak("Sunday is online.")

while True:

    command = listen()
    if not command:
        continue
    print("RAW COMMAND:", command)

    if command is None:
        continue

    print("You:", command)

    if "stop" in command.lower():
        speak("Goodbye ma'am")
        break

    # if not is_awake(command):
    #     continue

    # command = command.replace(
    #     "sunday",
    #     ""
    # ).strip()
    if command in ["hello", "hi"]:
        speak("Hello ma'am.")
        continue
    tool_response = execute(command)

    if tool_response:

        speak(tool_response)

        continue

    response = think(command)


    speak(response)