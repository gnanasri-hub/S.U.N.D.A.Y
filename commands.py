from datetime import datetime

def execute(command):

    if "time" in command:

        return f"The time is {datetime.now().strftime('%I:%M %p')}"

    elif "hello" in command:

        return "Hello ma'am"

    elif "how are you" in command:

        return "I am functioning perfectly."

    return None