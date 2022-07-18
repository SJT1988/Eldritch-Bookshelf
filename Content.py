from sre_parse import SPECIAL_CHARS
from typing import ClassVar
from Library import Book
from rich.console import Console
from rich.layout import Layout
from abc import ABC, abstractmethod
import re
from abc import ABC
import time, sys
import image2console
from PIL import Image

console = Console()
layout = Layout()

class Content(Book):
    def __init__(self, thisBook, nextBook):
        self._thisBook = thisBook
        self._nextBook = nextBook

#======================================================================
#======================================================================
'''
CLASS ART
Abstract class for artistic elements, including AsciiArt and images.
'''

class Art(ABC):

    def __init__(self, filename):

        if not str(filename):
            print("!!!'filename' is not a string type!!!")
            return
        if not re.search("\.[a-zA-Z]+$", filename):
            print("!!!filename is missing extension!!!")
            return
        self._filename = str(filename)
        name_extension = re.split("\.", filename) #split the string at the last dot
        self._name = name_extension[0] #first part is the name
        self._extension = name_extension[1] # last part is the extenion
    
    #stringify parameters for logging
    @abstractmethod
    def __str__(self) -> str:
        output = (
            "NAME: " + self._name + "\n" +
            "FILENAME: " + self._filename + "\n" +
            "EXTENSION: " + self._extension + "\n"
        )
        return output

#======================================================================
#======================================================================

"""
CLASS ELDRITCHIMAGE
This is a wrapper for the image2console class.
https://github.com/gaba5/Image2Console
Image2console can print colored images to the screen using pixel glyphs.
Original repo only accepts jpg, I updated to accept png.
The module itself is very short but it leans on several complex packages,
including NumPy and colr, to match ascii glyphs to pixel hues and values.
This wrapper will let me assign other attributes to the image that
are unique to my program (not yet implemented)
"""

class EldritchImage(Art):
    
    _path = ".\\images\\" # static variable for filepath
    
    def __init__(self, filename):
        super().__init__(filename)
        self._filepath = EldritchImage._path + str(filename)
        # ._image is a string of colored ascii glyphs
        img = Image.open(self._filepath)
        self._dimX, self._dimY = img.size
        img.close()

    def draw(self, numColumns=-1):
        colWidth = self._dimX
        if numColumns == -1:
            pass
        else:
            if int(numColumns) > 0 and int(numColumns) < 65:
                colWidth = numColumns
        print(image2console.string_image(self._filepath, size=colWidth))

    
    def __str__(self) -> str:
        output = (
            super().__str__() +
            "DIM X: " + str(self._dimX) + "\n" +
            "DIM Y: " + str(self._dimY) + "\n" +
            "FILEPATH: " + self._filepath + "\n" +
            "PATH: " + EldritchImage._path + "\n"
        )
        return output
    


#======================================================================
#======================================================================

'''
CLASS ASCIIART
ASCII art was generated using https://www.ascii-art-generator.org/.
Every generated text file contained some special characters that the
'rich' library could not resolve easily. After several experiements,
I decided it was easiest to replace these characters manually with
similar-looking characters in the text files they were read from.
'''

class AsciiArt(Art):
    
    _path = ".\\ascii-art\\" # static variable for filepath

    def __init__(self, filename, cols, rows):
        super().__init__(filename)
        self._filepath = AsciiArt._path + self._filename
        self._cols = int(cols)
        self._rows = int(rows)

    def draw(self, color=""):
        lst = []
        with open(self._filepath, "r") as f:
            for line in f:
                console.print(line, style=f"{color}", end='')
                # each line already ends with \n so we change
                # the end character of print() from default \n to ''.
        print("\n")

    #stringify parameters for logging
    def __str__(self) -> str:
        output = (
            super().__str__() +
            "COLUMNS: " + str(self._cols) + "\n" +
            "ROWS: " + str(self._rows) + "\n"
            "PATH: " + AsciiArt._path + "\n"
        )
        return output

#======================================================================
#======================================================================

class Script(ABC):

    def __init__(self):
        self.cassildas_song = [
            [
                "Along the shore the cloud waves break,",
                "\nThe twin suns sink behind the lake,",
                "\nThe shadows lengthen",
                "\n\tIn Carcosa.\n\n"
            ],
            [
                "Strange is the night where black stars rise,",
                "\nAnd strange moons circle through the skies",
                "\nBut stranger still is",
                "\n\tLost Carcosa.\n\n"
            ],
            [
                "Songs that the Hyades shall sing,",
                "\nWhere flap the tatters of the King,",
                "\nMust die unheard in",
                "\n\tDim Carcosa.\n\n"
            ],
            [
                "Song of my soul, my voice is dead;",
                "\nDie thou, unsung, as tears unshed",
                "\nShall dry and die in",
                "\n\tLost Carcosa.\n\n"
            ]
        ]
    

    """
    PRINT_STANZA(self, INT stanza)
        Function designed specifically for printing
        Cassilda's Song. The song contains 4 stanzas
        and 4 lines per stanza. The song is "typed"
        in real-time in the console. This function
        controls the pauses between lines.
    """
    def print_stanza(self,stanza):
        s = self.cassildas_song
        for i in range(len(s[stanza])-1):
            time.sleep(0.8)
            Script.typingPrint(s[stanza][i],"italic blue")
            sys.stdout.flush()
        time.sleep(0.4)
        Script.typingPrint(s[stanza][-1],"italic blue")


    """
    TYPINGPRINT(STR text, STR textstyle, FLOAT pause)
        Function for making strings print in real time
        as if it were typed by a type writer.
        The 'textstyle' parameter is any string that
        can be interpreted by the 'Rich' (rich text)
        module. The pause between characters is 0.05
        seconds, by default.
    """
    def typingPrint(text, textstyle, pause=0.05):
        for character in text:
            console.print(character, style=f"{textstyle}", end='')
            sys.stdout.flush()
            time.sleep(pause)