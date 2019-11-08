from pyfiglet import figlet_format
from termcolor import colored


def print_art(message, color):
    available_colors = ["red", "green", "yellow", "blue", "magenta", "cyan", "white"]

    if color not in available_colors:
        print("We don't have that color, so I gave you magenta.")
        color = "magenta"
        
    ascii_art = figlet_format(message)
    colored_ascii = colored(ascii_art, color=color)
    print(colored_ascii)

message = input("What message do you want to print?: ")
color = input("Ok! What color?: ")
print_art(message, color)