
winning_seq = []

NAMES = []

#take player names
def name_input():
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


def symbol_assign():
    name_input()
    print(NAMES)


def game_logic():
    turns = 9
    while turns > 0:
        print(turns)
        turns -= 1

game_logic()