def print_separator():
    """Prints a line of 30 asterisks to the terminal."""
    print("*" * 30)

def print_char_separator(char):
    """Print a separator using the chosen character."""
    if not char:
        char = "*"

    char = char[0]  # ensure only one character
    print(char * 30)

def print_custom_separator(char, length):
    """Print a separator using a custom character and length."""
    if length <= 0:
        print("")
        return

    if not char:
        char = "*"

    char = char[0]
    print(char * length)

def print_labeled_separator(label, char="*", width=30):
    """Print a separator with a centered label."""
    if not char:
        char = "*"

    char = char[0]

    print(label.center(width, char))

def print_box(message, char="*"):
    """Print a message inside a border box."""
    if not char:
        char = "*"

    char = char[0]

    width = len(message) + 4
    border = char * width

    print(border)
    print(f"{char} {message} {char}")
    print(border)