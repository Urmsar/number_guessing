class Game:
    max_nr = 0
    limit_of_guess = 5
    lost_round = 0
    win_round = 0

    def __init__(self, win: bool = False):
        self.win = win

    def reset(self):
        self.limit_of_guess = 5
        self.max_nr = 0

    def set_difficulty(self, choice):
        if choice == '1':
            self.max_nr = 3
        elif choice == '2':
            self.max_nr = 5
        elif choice == '3':
            self.max_nr = 9


class Player:
    def __init__(self, name, computer: bool, players_number=None):
        self.name = name
        self.players_number = players_number
        self.computer = computer
