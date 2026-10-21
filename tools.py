import webbrowser
import urllib.parse
import subprocess


def execute(command):

    command = command.lower().strip()

    # Open websites

    if "open youtube" in command:

        webbrowser.open(
            "https://youtube.com"
        )

        return "Opening YouTube, ma'am."

    if "open google" in command:

        webbrowser.open(
            "https://google.com"
        )

        return "Opening Google, ma'am."

    # Search YouTube

    if "search for" in command and "youtube" in command:

        query = command.replace(
            "search for",
            ""
        )

        query = query.replace(
            "in youtube",
            ""
        )

        query = query.strip()

        webbrowser.open(
            "https://www.youtube.com/results?search_query="
            + urllib.parse.quote(query)
        )

        return f"Searching YouTube for {query}, ma'am."

    # Search Google

    if command.startswith("search"):

        query = command.replace(
            "search",
            "",
            1
        ).strip()

        webbrowser.open(
            "https://www.google.com/search?q="
            + urllib.parse.quote(query)
        )

        return f"Searching Google for {query}, ma'am."

    # Open applications

    if "open notepad" in command:

        subprocess.Popen("notepad.exe")

        return "Opening Notepad, ma'am."

    if "open calculator" in command:

        subprocess.Popen("calc.exe")

        return "Opening Calculator, ma'am."

    return None