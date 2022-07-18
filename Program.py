import os
from Library import Book
from Content import AsciiArt, Script
import rich
from rich.console import Console
from rich.layout import Layout


console = Console()
layout = Layout()
script = Script()


def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":

    consoleSize = "mode 51,50"
    os.system(consoleSize)
    clearScreen()

    """
    skulldrip = AsciiArt("skull-drip_50x25.txt", 50, 25)
    skulldrip.draw("red")

    username = os.getlogin()
    console.print(username + ", your time has come.\n", style="bold red", justify="center")

    eyeOfRa = AsciiArt("eye-of-ra_50x20.txt", 50, 20)
    eyeOfRa.draw("purple")

    yellowSign = AsciiArt("yellow-sign_50x24.txt", 50, 24)
    yellowSign.draw("yellow")
    mystring = input()
    """
    script.print_stanza(0)
    skulldrip = AsciiArt("skull-drip_50x25.txt", 50, 25)
    skulldrip.draw("red")

    script.print_stanza(1)
    eyeOfRa = AsciiArt("eye-of-ra_50x20.txt", 50, 20)
    eyeOfRa.draw("purple")

    script.print_stanza(2)
    yellowSign = AsciiArt("yellow-sign_50x24.txt", 50, 24)
    yellowSign.draw("yellow")
    
    script.print_stanza(3)
    mystring = input()