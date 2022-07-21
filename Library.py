import random
import csv

#======================================================================
#======================================================================

class Bookshelf:
    
    _titlesFile = "randTitles.txt"
    _authorsFile = "randNames.txt"
    _books = []
    
    #======================================================================

    def __init__(self):
        
        _randTitles = Bookshelf.rand_list_from_file(Bookshelf._titlesFile)
        _randAuthors = Bookshelf.rand_list_from_file(Bookshelf._authorsFile)
        _randColors = Bookshelf.rand_list_from_list(["red,","green","blue","yellow","orange","purple","black","white"],100)
        _randPages = Bookshelf.rand_list_of_pagenums(1,199,100)

        
        # Generate 100 random books!
        for i in range(100):
            book = Book(
                _randTitles[i],
                _randAuthors[i],
                _randColors[i],
                _randPages[i],
                _randPages[i] + random.randint(10,50),
                i
            )
            Bookshelf._books.append(book)
        for x in Bookshelf._books:
            print(x)
    
    #======================================================================
    # RAND_LIST_FROM_FILE(str file) -> str[]
    # takes in the filename of a list of strings (titles, authors, etc.)
    # and returns a shuffled version of that list.
 
    @staticmethod
    def rand_list_from_file(file):
        
        lst = []
        with open(file, "r") as f:
            for line in f:
                clean = line[0:-1] #remove newline char
                lst.append(clean)
        random.shuffle(lst)
        #IMPORTANT: shuffle returns tupple (0,<shuffledList>).
        #Must never return the statement if we just want list.
        return lst

    #======================================================================
    # RAND_LIST_FROM_LIST(var[] lst, int length) -> var[]
    # Takes in a list of strings, ints, or presumably any other listable obj
    # and returns that shuffled list if length < 1 or
    # returns a list of length <length> using elements from lst.

    @staticmethod
    def rand_list_from_list(lst, length=0):

        if (length < 1):
            random.shuffle(lst)
            return lst
        else:
            return random.choices(lst,k=length)

    #======================================================================
    # RAND_LIST_OF_PAGENUMS(int lower, int upper, int listLength) -> int[]
    # returns a list of page numbers, in range(<lower>,<upper>),
    # of size <listLength>. This gets used to set the <_keyPage> for each
    # book and is also used to set the page length of the book.

    @staticmethod
    def rand_list_of_pagenums(lowerBound, upperBound, listLength):

        return random.choices(range(lowerBound,upperBound), k=listLength)

#======================================================================
#======================================================================

class Book:

    def __init__(self, title="", author="", color="", keyPage=-1, numPages=-1, index=-1):
        self._title = str(title)
        self._author = str(author)
        self._color = str(color)
        self._keyPage = int(keyPage)
        self._numPages = int(numPages)
        self._index = int(index)

    # Accessor functions
    
    def get_title(self):
        return self._title
    def set_title(self, newTitle):
        print("setting title")
        self._title = str(newTitle)

    def get_author(self):
        return self._author
    def set_author(self, newAuthor):
        self._title = str(newAuthor)

    def get_color(self):
        return self._color
    def set_color(self, newColor):
        self._title = str(newColor)

    def get_keyPage(self):
        return self._keyPage
    def set_keyPage(self, keyPage):
        self._keyPage = int(keyPage)

    def get_numPages(self):
        return self._numPages
    def set_numPages(self, numPages):
        self._title = int(numPages)

    def get_index(self):
        return self._index
    def set_index(self, index):
        self._index = int(index)

    # Property Functions
    
    title = property(get_title,set_title)
    author = property(get_author,set_author)
    color = property(get_color,set_color)
    keyPage = property(get_keyPage,set_keyPage)
    numPages = property(get_numPages,set_numPages)
    index = property(get_index,set_index)

    def __str__(self):
        output =(
            "TITLE: " + self._title + "\n" +
            "AUTHOR: " + self._author + "\n" +
            "COLOR: " + self._color + "\n" +
            "NUMPAGES: " + str(self._numPages) + "\n" +
            "KEY PAGE: " + str(self._keyPage) + "\n" +
            "INDEX: " + str(self._index) + "\n"
        )
        return output