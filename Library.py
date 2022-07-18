class Book:
    def __init__(self, title, author, numPages, color, genre, index,):
        self._title = str(title)
        self._author = str(author)
        self._numPages = int(numPages)
        self._color = str(color)
        self._genre = str(genre)
        self._index = int(index)

    def __str__(self):
        output =(
            "TITLE: " + self._title + "\n" +
            "AUTHOR: " + self._author + "\n" +
            "NUMPAGES: " + str(self._numPages) + "\n" +
            "COLOR: " + self._color + "\n" +
            "GENRE: " + self._genre + "\n" +
            "INDEX: " + str(self._index) + "\n"
        )
        return output