from random import sample, choices

uniqueness = True

class Game():

    game_type = {
        'mastermind':{'variations': ['red', 'white', 'blue', 'brown', 'yellow', 'green', 'orange', 'purple'],
                      'unique': True,
                      'level': {'really easy': 3, 'easy': 4, 'normal': 5, 'hard': 8}
                      },
        'classic': {'variations': '1234567890',
                    'unique': True,
                    'level': {'really easy': 3, 'easy': 4, 'normal': 5, 'hard': 10}
                    },
    }

    def __init__(self, gtype, level = 'normal', unique=True):
        self.gtype = gtype
        self.level = level
        self.unique = unique
        self._gen_secret()

    def _gen_secret(self):
        if self.unique:
            self.secret = sample(self.game_type[self.gtype]['variations'],
                                 k=self.game_type[self.gtype]['level'][self.level])
        else:
            self.secret = choices(self.game_type[self.gtype]['variations'],
                                  k=self.game_type[self.gtype]['level'][self.level])

    def renew_secret(self):
        self._gen_secret()

    def compare_guess(self, user_guess):
        r = []
        for i in range(len(user_guess)):
            if user_guess[i] in self.secret:
                if user_guess[i] == self.secret[i]:
                    r.append(2) # bull
                else:
                    r.append(1) # cow
            else:
                r.append(0) # nothing
        return r

g = Game('mastermind', 'hard', False)
print(g.compare_guess(['yellow', 'blue', 'brown', 'white', 'purple', 'red', 'orange', 'green']))
