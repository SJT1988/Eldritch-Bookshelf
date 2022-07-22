import os
from Library import *

# States is a class that only contains a dictionary
# of dictionaries that is used to determine menu
# progression (for now)

class State:

    states = {
        "start": {
            "message": "\n".join([
                "When you first started working for the Rare Book Collector",
                "each day was joyful. You were thrilled to catalog exotic",
                "titles and study their forbidden contents.",
                "\n",
                "That all changed with the arrival of the Black Ledger.",
                "It arrived a week ago with a shipment of 100 other books.",
                "Its offputing binding feels neither animal or synthetic.",
                "The cover's eldritch patterns give you a headache.",
                "\n",
                "You have no idea who wrote the mad scrawlings within.",
                "The ethereal landscapes within confound, compell and repulse you.",
                "You swore to never read another page, but they call to you--",
                "in your quiet moments. In your sleep. In your mind."
            ]),
            "options": [("One more page?", "first meeting"), ("One more page?", "first meeting")]
        },
        "first meeting": {
            "message": "\n".join([
                f"{os.getlogin()}...",
                f"{os.getlogin()}, please, read my words.",
                "\n",
                "My kingdom was usurped by a jaundiced tyrant.",
                "His sigil could raise the dead and bend minds to his will.",
                "He claimed to be a god, but his dark power poisoned all who embraced it.",
                "He destroyed all others who resisted, but me, he made an example of.",
                "I am now a prisoner in these pages.",
                "You must break the curse so I can rescue my beloved."
            ]),
            "options": [("\"How?\"", "instructions"), ("\"Screw this.\"", "leave 1")]
        },
        "instructions": {
            "message": "\n".join([
                "The xanthic king hid stanzas of a powerful song within 4 other books.",
                "My lady's requim for our lost city.",
                "His curse prevents me from telling you their exact locations",
                "But I can provide clues.",
                "\n",
                "Find them,",
                "write their mournful words in this ledger,",
                "and break the curse."
            ]),
            "options": [("Where should I start looking?", f"clue str({BookShelf._clue_order[0]})")]
        },
        "clue A": {
            "message": "\n".join([
                f"Inside a book whose title begins with '{BookShelf._e_books[0].title}'...page {str(BookShelf._e_books[0].keyPage)}."
            ]),
            "options": [("Return.", "main menu")]
        },
        "clue B": {
            "message": "\n".join([
                f"Within the pages of the book of '{BookShelf._e_books[1].author}'...page {str(BookShelf._e_books[1].keyPage)}."
            ]),
            "options": [("Return.", "main menu")]
        },
        "clue C": {
            "message": "\n".join([
                f"Seek a '{BookShelf._e_books[2].color}' tome...page {str(BookShelf._e_books[2].keyPage)}."
            ]),
            "options": [("Return.", "main menu")]
        },
        "clue D": {
            "message": "\n".join([
                f"Find the author with initials \"{BookShelf._e_books[3].get_initials()}\"...page {str(BookShelf._e_books[3].keyPage)}."
            ]),
            "options": [("Return.", "main menu")]
        },
    }

    def __init__(self):
        pass

    
