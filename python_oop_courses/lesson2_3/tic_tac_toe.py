from random import choice


class Player:
    def __init__(self, name):
        self.name = name
        self.coordinate = None
        self.move = None

    def make_move(self):
        self.coordinate = input(f"Type in the coordinates where you want to move, for example, 1A\n"
                                f"{self.name}, your input: ")


class Game:
    def __init__(self, player1: Player, player2: Player):
        self.player1 = player1
        self.player2 = player2
        self.turn_is = choice([self.player1, self.player2])
        self.player1.move = 'X'
        self.player2.move = 'O'
        self.fields = {
            '1A': '_',
            '1B': '_',
            '1C': '_',
            '2A': '_',
            '2B': '_',
            '2C': '_',
            '3A': '_',
            '3B': '_',
            '3C': '_',
        }
        self.rounds = 0
        print(f"  1 2 3\n"
              f"A {self.fields['1A']} {self.fields['2A']} {self.fields['3A']}\n"
              f"B {self.fields['1B']} {self.fields['2B']} {self.fields['3B']}\n"
              f"C {self.fields['1C']} {self.fields['2C']} {self.fields['3C']}\n")

    def start(self):
        if self.rounds == 10:
            print(f'Draw!')
        self.turn_is.make_move()
        if self.fields[f"{self.turn_is.coordinate}"] == '_':
            self.fields[f"{self.turn_is.coordinate}"] = self.turn_is.move
        else:
            print("This field is already taken. Choose the other one!\n")
            self.start()
        if any([self.fields['1A'] == self.fields['2B'] == self.fields['3C'] != '_',
                self.fields['1C'] == self.fields['2B'] == self.fields['3C'] != '_',
                self.fields['1A'] == self.fields['2A'] == self.fields['3A'] != '_',
                self.fields['1B'] == self.fields['2B'] == self.fields['3B'] != '_',
                self.fields['1C'] == self.fields['2C'] == self.fields['3C'] != '_',
                self.fields['1A'] == self.fields['1B'] == self.fields['1C'] != '_',
                self.fields['2A'] == self.fields['2B'] == self.fields['2C'] != '_',
                self.fields['3A'] == self.fields['3B'] == self.fields['3C'] != '_']):
            print(f"  1 2 3\n"
                  f"A {self.fields['1A']} {self.fields['2A']} {self.fields['3A']}\n"
                  f"B {self.fields['1B']} {self.fields['2B']} {self.fields['3B']}\n"
                  f"C {self.fields['1C']} {self.fields['2C']} {self.fields['3C']}\n")
            print(f'{self.turn_is.name} won!')
        else:
            if self.turn_is == self.player1:
                self.turn_is = self.player2
            else:
                self.turn_is = self.player1
            print(f"  1 2 3\n"
                  f"A {self.fields['1A']} {self.fields['2A']} {self.fields['3A']}\n"
                  f"B {self.fields['1B']} {self.fields['2B']} {self.fields['3B']}\n"
                  f"C {self.fields['1C']} {self.fields['2C']} {self.fields['3C']}\n")
            self.rounds += 1
            self.start()


player_1 = Player("guryasha")
player_2 = Player("foke")

game1 = Game(player_1, player_2)
game1.start()
