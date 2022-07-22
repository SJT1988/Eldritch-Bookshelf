import os
import re
from Library import *
from collections import OrderedDict

# States is a class that contains a dictionary
# of dictionaries that is used to determine menu
# progression

class State:

    states = {}
    #idx_pg = []
    #=========================================================
    #VALIDATE(var ans, str[] opt, str state)
    
    def validate(self, ans, opt) -> bool:
        if int(ans) in range(1,len(opt)+1):
            self._current_state = opt[int(ans)-1][1]
            print(self._current_state)
            return True
        else:
            return False
        
        
        # if re.match('[0-9]{1,2} [0-9]{1,3}', str(ans)):
        #     idx = int(str(ans).split()[0])
        #     pg = int(str(ans).split()[1])
        #     if pg > 0 and pg <= BookShelf._books[idx].numPages:
        #         State.idx_pg = [idx,pg]
        #         return True
        # else:
        #     return False

    #=========================================================
    # PROGRESS_UPDATE()
    # Change the state of progression keys/milestones

    def progress_update(self, state):
        if state == "main menu":
            for v in self.keys:
                v = False
        elif state == "start":
            self.keys["started"] = True
        
        elif state == f"clue {BookShelf._clue_order[0]}":
            self.keys["got clue 1"] = True
        elif state == ["stanza 1"]:
            self.keys['found stanza 1'] = True
        elif state != True: #TODO
            self.keys['wrote stanza 1'] = True

        elif state == f"clue {BookShelf._clue_order[1]}":
            self.keys["got clue 2"] = True
        elif state == ["stanza 2"]:
            self.keys['found stanza 2'] = True
        elif state != True: #TODO
            self.keys['wrote stanza 2'] = True

        elif state == f"clue {BookShelf._clue_order[2]}":
            self.keys["got clue 3"] = True
        elif state == ["stanza 3"]:
            self.keys['found stanza 3'] = True
        elif state != True: #TODO
            self.keys['wrote stanza 3'] = True

        elif state == f"clue {BookShelf._clue_order[3]}":
            self.keys["got clue 4"] = True
        elif state == ["stanza 4"]:
            self.keys['found stanza 4'] = True
        elif state != True: #TODO
            self.keys['wrote stanza 4'] = True
    
    #=========================================================
    # CURRENT CLUE() -> [int,str]
    # returns the active clue the player is working on

    def current_clue(self):

        if self.keys["wrote stanza 1"] == False:
            return [1, BookShelf._clue_order[0]]
        if self.keys["wrote stanza 2"] == False:
            return [2, BookShelf._clue_order[1]]
        if self.keys["wrote stanza 3"] == False:
            return [3, BookShelf._clue_order[2]]
        if self.keys["wrote stanza 4"] == False:
            return [4, BookShelf._clue_order[3]]
        else:
            return [5,'']

    #=========================================================
    # BLACK_LEDGER_STATE() -> str
    # checks current progress to determine which state the
    # hub option `read the black ledger` will take the player to.
    # 

    def black_ledger_state(self) -> str:

        i = self.current_clue()[0]
        if self.keys[f"wrote stanza {str(i)}"] == True:
            if i != 3:
                return f"clue {i+1}" # on current clue but already wrote it.
                # this should already have happened. This shouldn't ever trigger.
            else:
                return 'endgame'
        else:
            if self.keys[f"found stanza {str(i)}"] == True:
                return "beckon scrawl"
            else: # give current clue
                return f"clue {self.current_clue()[1]}"

    #=========================================================
    # DISPLAY_PAGE

    #=========================================================

    def __init__(self):

        #=========================================================
        # INITIALIZE [PROGRESS] KEYS
        self.keys = OrderedDict({
            'started': False,
            'got clue 1': False,
            'found stanza 1': False,
            'wrote stanza 1': False,
            'got clue 2': False,
            'found stanza 2': False,
            'wrote stanza 2': False,
            'got clue 3': False,
            'found stanza' : False,
            'wrote stanza 3': False,
            'got clue 4': False,
            'found stanza 4': False,
            'wrote stanza 4': False
        })
        #=========================================================
        # INITIALIZE STATES
        self._current_state = ""
        State.states = states = {
            "main menu": {
                "message": "M A I N   M E N U",
                "options": [
                    ("START GAME", "start"),
                    ("QUIT GAME", "quit")
                ]
            },
            "hub": {
                "message": "\n".join([
                    "CHOOSE WISELY."
                ]),
                "options": [
                    ("Read the Black Ledger", self.black_ledger_state()),
                    ("Search Books", "search menu"),
                    ("Write in the Black Ledger", "wLedger conditions"),
                    ("Quit", "main menu") 
                ]
            },
            "start": {
                "message": "\n".join([
                    "When you first started working for the Rare Book Collector,",
                    "each day was joyful. You were thrilled to catalog exotic",
                    "titles and study their forbidden contents.",
                    "",
                    "That all changed with the arrival of the Black Ledger.",
                    "It arrived a week ago with a shipment of 100 other books.",
                    "Its offputing binding feels neither animal or synthetic.",
                    "The cover's eldritch patterns give you a headache.",
                    "",
                    "You have no idea who wrote the mad scrawlings within.",
                    "The ethereal landscapes inside confound, compell and repulse you.",
                    "You swore to never read another page, but they call to you--",
                    "in your quiet moments. In your sleep. In your mind."
                ]),
                "options": [("One more page?", "first meeting"), ("One more page.", "first meeting")]
            },
            "first meeting": {
                "message": "\n".join([
                    f"{os.getlogin()}...",
                    f"{os.getlogin()}, please, read my words.",
                    "",
                    "My kingdom was usurped by a jaundiced tyrant.",
                    "His sigil could raise the dead and bend minds to his will.",
                    "He claimed to be a god, but his dark power poisoned all who embraced it.",
                    "He destroyed all others who resisted, but me, he made an example of.",
                    "",
                    "I am now a prisoner in these pages.",
                    "You must break the curse so I can rescue my beloved."
                ]),
                "options": [("\"How?\"", "instructions"), ("\"Screw this.\"", "leave 1")]
            },
            "instructions": {
                "message": "\n".join([
                    "The xanthic king hid stanzas of a powerful song within 4 other books:",
                    "My lady's requim for our lost city.",
                    "His curse prevents me from telling you their exact locations",
                    "But he underestimates me. I can provide clues.",
                    "",
                    "Find them,",
                    "write their mournful words in this ledger,",
                    "and break the curse."
                ]),
                "options": [("Where should I start looking?", f"clue {BookShelf._clue_order[0]}")]
            },
            "clue A": {
                "message": "\n".join([
                    f"Inside a book whose title begins with '{BookShelf._e_books[0].title}'...page {str(BookShelf._e_books[0].keyPage)}."
                ]),
                "options": [("Find it", "hub")]
            },
            "clue B": {
                "message": "\n".join([
                    f"Within the pages of the book of '{BookShelf._e_books[1].author}'...page {str(BookShelf._e_books[1].keyPage)}."
                ]),
                "options": [("Start looking", "hub")]
            },
            "clue C": {
                "message": "\n".join([
                    f"Seek a {BookShelf._e_books[2].color} tome...page {str(BookShelf._e_books[2].keyPage)}."
                ]),
                "options": [("Start looking", "hub")]
            },
            "clue D": {
                "message": "\n".join([
                    f"Find the author with initials \"{BookShelf._e_books[3].get_initials()}\"...page {str(BookShelf._e_books[3].keyPage)}."
                ]),
                "options": [("Start looking", "hub")]
            },
            "lorem ipsum":{
                "message": random.choice([
                    "\n".join([
                    "Lorem ipsum dolor sit amet. Ut sequi ullam est debitis",
                    "molestiae qui dicta consequatur in molestiae consectetur",
                    "sit temporibus cupiditate non voluptatibus repellendus in",
                    "quae officia. 33 voluptas dicta sed similique culpa est",
                    "quidem exercitationem maiores enim ab magnam sequi id",
                    "molestias dolores! Et earum aliquid At laborum sunt eos",
                    "dolorem sunt."
                    ]),
                    "\n".join(["Est architecto perferendis sed magni maxime eum laborum",
                    "quia non enim aperiam. Id praesentium voluptas ut odio",
                    "tempore et doloremque atque a incidunt laborum. Et soluta",
                    "voluptas id laborum nisi et nisi voluptate ut rerum impedit",
                    "in rerum ipsa. Quo omnis nihil qui vero unde a dolor fuga sit",
                    "itaque cumque et fugiat aspernatur sed eius quibusdam non"
                    "quibusdam consequatur."
                    ]),
                    "\n".join(["Est consequatur doloribus eos voluptatem voluptate et vitae",
                    "sapiente qui consectetur vero non quaerat voluptates sit debitis",
                    "laborum et error dignissimos. At veniam consequatur et vitae",
                    "sequi est recusandae saepe aut aperiam suscipit non recusandae",
                    "tenetur aut optio natus. Est dolorum omnis est officiis dignissimos",
                    "qui voluptatem debitis ab quia asperiores. Qui quam dolorum est"
                    "nobis aliquam est nihil sapiente eum veniam quia ab quia distinctio."])
                ]),
                "options": [("This isn't what I'm looking for (go back).", "hub")]
            },
            "search menu":{
                "message": "S O R T    B O O K S H E L F",
                "options": [
                    ("Read a book", "read menu"),
                    ("Sort by Title", "sort title"),
                    ("Sort by Author - First", "sort auth first"),
                    ("Sort by Author - Last", "sort auth last"),
                    ("Sort by Color", "sort color"),
                    ("Sort by Length", "sort length"),
                    ("Back", "hub")
                ]
            },
            #Brute forcing sort screens:
            "sort title":{
                "message": BookShelf.make_table(1),
                "options": [("Back", "search menu")]
            },
            "sort auth first":{
                "message": BookShelf.make_table(2),
                "options": [("Back", "search menu")]
            },
            "sort auth last":{
                "message": BookShelf.make_table(3),
                "options": [("Back", "search menu")]
            },
            "sort color":{
                "message": BookShelf.make_table(4),
                "options": [("Back", "search menu")]
            },
            "sort length":{
                "message": BookShelf.make_table(5),
                "options": [("Back", "search menu")]
            },

            "dead": { 
                "message": "\n".join([
                    "YOU DIED"
                ]),
            "options": []
            },
            "leave 1": {
                "message": "\n".join([
                    "The player returned to his home planet and died.",
                    ":P"
                ]),
                "options": [("YOU DIED", "main menu")]
            },
            "quit": { #state exists only to trigger program closing
                "message": "",
            "options": []
            }
        }

    
