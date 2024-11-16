import random
import os
from zoneinfo import available_timezones

CURRENT_TURN = None
NEXT_TURN = None
NAMES = []
TURNS_REMAINING = 9
entry_dict = {
    1: [0, 0],
    2: [0, 1],
    3: [0, 2],
    4: [1, 0],
    5: [1, 1],
    6: [1, 2],
    7: [2, 0],
    8: [2, 1],
    9: [2, 2],
}

player_sym = {}

#take player names
def player_names():
    player1 = str(input("Enter your name (Player 1): "))
    player2 = str(input("Enter your name (Player 2): "))
    if player1 != '' and player2 != '':
        NAMES.append(player1)
        NAMES.append(player2)
    elif player1 == '' and player2 == '':
        NAMES.append('Bot 1')
        NAMES.append('Bot 2')
    elif player1 == '' and player2 != '':
        NAMES.append('Bot 1')
        NAMES.append(player2)
    elif player2 != '' and player2 == '':
        NAMES.append(player1)
        NAMES.append('Bot 2')


#assign x to a player
def assign_sign():
    global CURRENT_TURN
    CURRENT_TURN = 0

def switcher():
    global CURRENT_TURN, NEXT_TURN
    if CURRENT_TURN == 0:
        NEXT_TURN = CURRENT_TURN + 1
    elif CURRENT_TURN == 1:
        NEXT_TURN = CURRENT_TURN - 1


# Game Logic
def main():
    global TURNS_REMAINING, CURRENT_TURN
    game = [['-','-','-'],['-','-','-'],['-','-','-']]
    win_seq = [[]]
    player_names()
    assign_sign()
    available_locations = list(entry_dict.keys())
    while TURNS_REMAINING > 0:
        def input_validator():
            print(f'Available Locations --> {available_locations}')
            user_input = int(input(f'{NAMES[CURRENT_TURN]} enter your input: '))

            if user_input not in available_locations:
                input_validator()
            else:
                player_sym.get(f'NAMES[CURRENT_TURN]')
                if CURRENT_TURN == 0:
                    symbol = 'X'
                elif CURRENT_TURN == 1:
                    symbol = 'O'
                game[entry_dict.get(user_input)[0]][entry_dict.get(user_input)[1]] = symbol
                for x in game:
                    print(*x, sep=' | ')
                    print('---------')
                available_locations.pop(available_locations.index(user_input))

        input_validator()
        switcher()
        CURRENT_TURN = NEXT_TURN
        TURNS_REMAINING = TURNS_REMAINING - 1

main()