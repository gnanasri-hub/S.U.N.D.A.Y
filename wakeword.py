WAKE_WORDS = [
    "sunday",
    "sun day",
    "sunda"
]

def is_awake(command):

    if command is None:
        return False

    command = command.lower()

    return any(
        word in command
        for word in WAKE_WORDS
    )