import random

class Sweepstakes:
    def __init__(self):
        self.contestants = {
            0: {
                'fname': "Joe",
                'lname': "Bob"
            },
            1: {
                'fname': 'Bob',
                'lname': 'Arg'
            },
            2: {
                'fname': 'Gary',
                'lname': 'Smith'
            },
            3: {
                'fname': 'Jeff',
                'lname': 'Smith'
            },
            4: {
                'fname': 'Stacy',
                'lname': 'Dale'
            },
        }

    def pick_winner(self):
        winner = int(random.randint(0, 4))
        print(f'Winner is {self.contestants[winner]["fname"]} {self.contestants[winner]["lname"]}')
