import random
from time import sleep

from player import Game, Player

print("====NUMBER GUESSING GAME====")
limit_of_guess = 5
choice = None
player1 = Player(name='Urmas', computer=False)
player2 = Player(name='Skynet', computer=True)
game = Game()
game.win = False
while not game.win:
    if game.max_nr == 0:
        choice = input('choice level difficulty 1 or 2 or 3 ')
        if not choice.isnumeric() or int(choice) > 4:
            print(f'not offered "{choice}" choice')
            continue
        game.set_difficulty(choice)

    right_number = False
    while not right_number:
        player1.players_number = input(f"Choose number between 1 to {game.max_nr} : ")

        if not player1.players_number.isnumeric() or int(player1.players_number) > game.max_nr:
            print('You did not enter a valid char, try again')
        else:
            player1.players_number = int(player1.players_number)
            right_number = True

    player2.players_number = random.randint(1, game.max_nr)
    print("Skynet is thinking of a number...")
    sleep(1)
    print(f"You choose {player1.players_number}")
    game.limit_of_guess -= 1
    if player1.players_number == player2.players_number:
        print("You won!")
        game.win_round += 1
        game_again = input('do you play more y/N ')
        if game_again.upper() == "Y":
            game.reset()
        else:
            game.win = True
    else:
        if game.limit_of_guess == 0:
            print('you lost, you have no more limit of guess')
            game_again = input('do you play more y/N ')
            game.lost_round += 1
            if game_again.upper() == "Y":
                game.reset()
            else:
                game.win = True

        print(f"Skynet thought of {player2.players_number}")
        print(f'you lost, you have {game.limit_of_guess} attempts left.Try again.')
print(f'you win {game.win_round} round(s) and you play {game.win_round + game.lost_round} round(s)')
win_percent = 100.0 * game.win_round / (game.lost_round + game.win_round)
print(f'It makes {win_percent:.1f}% wins')
