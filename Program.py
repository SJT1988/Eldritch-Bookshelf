import os
from Library import *
from Content import *
import rich
from rich.console import Console
from rich.layout import Layout
from State import State
#-------------------------------
#These are just to make the console window full-size
import ctypes
import msvcrt
import subprocess
from ctypes import wintypes
#-------------------------------
console = Console()
layout = Layout()
script = Script()

#=========================================================
kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
user32 = ctypes.WinDLL('user32', use_last_error=True)

SW_MAXIMIZE = 3

kernel32.GetConsoleWindow.restype = wintypes.HWND
kernel32.GetLargestConsoleWindowSize.restype = wintypes._COORD
kernel32.GetLargestConsoleWindowSize.argtypes = (wintypes.HANDLE,)
user32.ShowWindow.argtypes = (wintypes.HWND, ctypes.c_int)

def maximize_console(lines=None):
    fd = os.open('CONOUT$', os.O_RDWR)
    try:
        hCon = msvcrt.get_osfhandle(fd)
        max_size = kernel32.GetLargestConsoleWindowSize(hCon)
        if max_size.X == 0 and max_size.Y == 0:
            raise ctypes.WinError(ctypes.get_last_error())
    finally:
        os.close(fd)
    cols = max_size.X
    hWnd = kernel32.GetConsoleWindow()
    if cols and hWnd:
        if lines is None:
            lines = max_size.Y
        else:
            lines = max(min(lines, 9999), max_size.Y)
        subprocess.check_call('mode.com con cols={} lines={}'.format(
                                cols, lines))
        user32.ShowWindow(hWnd, SW_MAXIMIZE)

#=========================================================

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def intro():
    clearScreen()
    maximize_console()

    # carcosa = EldritchImage("carcosa.png")
    # carcosa.draw(60)

    time.sleep(1)
    #poems, ascii art
    
    script.print_stanza(0)
    skulldrip = AsciiArt("skull-drip_50x25.txt", 50, 25)
    time.sleep(0.5)
    skulldrip.draw("red")
    time.sleep(0.25)
    
    script.print_stanza(1)
    eyeOfRa = AsciiArt("eye-of-ra_50x20.txt", 50, 20)
    time.sleep(0.5)
    eyeOfRa.draw("purple")
    time.sleep(0.25)

    script.print_stanza(2)
    yellowSign = AsciiArt("yellow-sign_50x24.txt", 50, 24)
    time.sleep(0.5)
    yellowSign.draw("yellow")
    time.sleep(0.25)
    
    script.print_stanza(3)
    mystring = input()

    time.sleep(2)
    input()
    clearScreen()
#=========================================================

if __name__ == "__main__":
    #intro()
    
    bookShelf = BookShelf()
    mngr = State()
    state = mngr.states['main menu']

    while True:

        mngr.progress_update(state)
        # this makes us print the regular way if we are
        # drawing a table.
        if mngr._current_state not in [
            "sort title",
            "sort auth first",
            "sort auth last",
            "sort color",
            "sort length"
        ]:
            for line in state['message']:
                Script.typewriter([line],"yellow italic", 0.01)
        else:
            print(state['message'])
        print("\n\n")
        if state is mngr.states['quit']:
            break

        for i, opt in enumerate(state['options']):
            print(f"{i+1}. {opt[0]}")
        
        while True:
            answer = input(">>> ")
            if mngr.validate(answer, state['options']):
                state = mngr.states[state['options'][int(answer)-1][1]]
                time.sleep(1.0)
                clearScreen()
                break
            else:
                print('\n'.join(["Type the number for one of the given options",
                "and press 'ENTER'."]))

    #images
    """
    carcosa = EldritchImage("carcosa.png")
    print(carcosa)
    carcosa.draw(60)
    input()
    portrait = EldritchImage("theYellowPortrait.png")
    print(portrait)
    portrait.draw(60)
    """
    
    #poems, ascii art
    
    # script.print_stanza(0)
    # skulldrip = AsciiArt("skull-drip_50x25.txt", 50, 25)
    # time.sleep(0.5)
    # skulldrip.draw("red")
    # time.sleep(0.25)
    
    # script.print_stanza(1)
    # eyeOfRa = AsciiArt("eye-of-ra_50x20.txt", 50, 20)
    # time.sleep(0.5)
    # eyeOfRa.draw("purple")
    # time.sleep(0.25)

    # script.print_stanza(2)
    # yellowSign = AsciiArt("yellow-sign_50x24.txt", 50, 24)
    # time.sleep(0.5)
    # yellowSign.draw("yellow")
    # time.sleep(0.25)
    
    # script.print_stanza(3)
    # mystring = input()
    exit(0)