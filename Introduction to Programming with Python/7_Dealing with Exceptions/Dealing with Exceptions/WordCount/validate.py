"""Input validation functions."""


def input_yesno(message):
    """
    Displays an input prompt, showing the specified message.
    Keeps prompting until the user enters y, n, yes, or no in any case text.
    Returns the response as "yes" or "no".
    """
    while True:
        user_input = input("\n" + message + " (Y/N) ").lower()
        if user_input in ["y", "yes", "n", "no"]:
            if user_input in ["y", "yes"]:
                return "yes"
            else:
                return "no"
