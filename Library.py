import random
from tabulate import tabulate
#======================================================================
#======================================================================

class BookShelf():
    
    _titlesFile = "randTitles.txt"
    _authorsFile = "randNames.txt"
    _books = []
    _SIZE = 100
    _e_books = []
    _clue_order = []
    
    #======================================================================

    def __init__(self):
        
        BookShelf._clue_order = ['A','B','C','D'] # used to order clue events
        random.shuffle(BookShelf._clue_order)

        _randTitles = BookShelf.rand_list_from_file(BookShelf._titlesFile)
        _randAuthors = BookShelf.rand_list_from_file(BookShelf._authorsFile)
        _randColors = BookShelf.rand_list_from_list(["red,","green","blue",
        "yellow","orange","purple","black","white"],BookShelf._SIZE)
        _randPages = BookShelf.rand_list_of_pagenums(1,199,BookShelf._SIZE)

        BookShelf._books = []

        # Generate _SIZE random books!
        for i in range(BookShelf._SIZE):
            book = Book(
                _randTitles[i],
                _randAuthors[i],
                _randColors[i],
                _randPages[i],
                _randPages[i] + random.randint(10,50),
                i
            )
            BookShelf._books.append(book)
        BookShelf.choose_event_books()
    
    #======================================================================
    # CHOOSE_EVENT_BOOKS()
    # Determines which 4 books from BookShelf._books will be marked to
    # "contain" stanzas by changing their self.event parameter from -1 to
    # 1, 2, 3, or 4. These books are copied into BookShelf.e_books
    # so that the State class can easily reference their parameters for
    # clue descriptions.

    @staticmethod
    def choose_event_books():
        # randomly pick 4 books' starting indices:
        e_indices = random.sample(range(BookShelf._SIZE),k=4)
        # reassign original books' event indices to 1-4,
        # and copy them into BookShelf.e_books:
        for i in range(4):
            BookShelf._books[e_indices[i]].event = i+1
            BookShelf._e_books.append(BookShelf._books[e_indices[i]])
    
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

    #=====================================================================
    # SORT_BOOKSHELF(int param_index)
    # sorts the bookshelf by the parameter associated with the given index:
    # 1 - Title
    # 2 - Author - First
    # 3 - Author - Last
    # 4 - Color
    # 5 - NumPages
    # (Secret):
    # 11 - PageKey
    # 12 - Event

    @staticmethod
    def sort_bookshelf(param_index):

        if param_index == 1:
            BookShelf._books.sort(key=lambda book: book.title)
        elif param_index == 2:
            BookShelf._books.sort(key=lambda book: book.author)
        elif param_index == 3:
            BookShelf._books.sort(key=lambda book: book.author.split(" ")[-1])
        elif param_index == 4:
            BookShelf._books.sort(key=lambda book: book.color)
        elif param_index == 5:
            BookShelf._books.sort(key=lambda book: book.numPages)
        elif param_index == 11:
            BookShelf._books.sort(key=lambda book: book.keyPage)
        #secret
        elif param_index == 12:
            BookShelf._books.sort(key=lambda book: book.event)
        else:
            print("ERROR: param_index must be an int from 1 to 5.")
            return
        # update index:
        for i in range(len(BookShelf._books)):
            BookShelf._books[i]._index = BookShelf._books.index(BookShelf._books[i])

    #=====================================================================
    # PRINT_BOOKSHELF()
    # Prints all bookshelf entries in its current order.
    # Full-version with spoiler fields (for debugging) are commented out.
    # NOTE: fancier table formats are bugged. They stop printing halfway.

    @staticmethod
    def print_bookshelf():
        # table = ['INDEX','TITLE','AUTHOR','COLOR','NUMPAGES','KEYPAGE','EVENT'],
        table = [['INDEX','TITLE','AUTHOR','COLOR','NUMPAGES'],
        ]
        for book in BookShelf._books:
            table.append([str(book.index),book.title,book.author,
            book.color,str(book.numPages)])
        # for book in BookShelf._books:
        #     table.append([str(book.index),book.title,book.author,book.color,
        #     str(book.numPages),str(book.keyPage),str(book.event)])
        print(tabulate(table, headers ="firstrow", tablefmt="plain"))

    @staticmethod
    def make_table(sort_indx=0):
        if sort_indx != 0:
            BookShelf.sort_bookshelf(sort_indx)
        table = [['INDEX','TITLE','AUTHOR','COLOR','NUMPAGES'],
        ]
        for book in BookShelf._books:
            table.append([str(book.index),book.title,book.author,
            book.color,str(book.numPages)])
        tbl = tabulate(table, headers ="firstrow", tablefmt="plain")
        with open('table.txt', 'w') as f:
            f.write(tbl)
        return tbl


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
        self._event = -1

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

    def get_event(self):
        return self._event
    def set_event(self, event):
        self._event = event

    # Property Functions
    
    title = property(get_title,set_title)
    author = property(get_author,set_author)
    color = property(get_color,set_color)
    keyPage = property(get_keyPage,set_keyPage)
    numPages = property(get_numPages,set_numPages)
    index = property(get_index,set_index)
    event = property(get_event, set_event)

    # Other Functions

    #======================================================================
    # Returns the punctuated initials of the author of the book
    # that calls it.
     
    def get_initials(self) -> str:

        first_last = self.author.split(" ")
        return first_last[0][0] + '.' + first_last[1][0] + '.'

    #======================================================================
    # __STR__() -> str
    # String typecast overload. Best for a single book. If you want to
    # print data from every book in the bookshelf, use
    # BOOKSHELF.PRINT_BOOKSHELF()

    def __str__(self):

        output =(
            "TITLE: " + self.title + "\n" +
            "AUTHOR: " + self.author + "\n" +
            "COLOR: " + self.color + "\n" +
            "NUMPAGES: " + str(self.numPages) + "\n" +
            "KEYPAGE: " + str(self.keyPage) + "\n" +
            "INDEX: " + str(self.index) + "\n" +
            "EVENT: " + str(self.event) + "\n"
        )
        return output