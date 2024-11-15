import random

NAMES = []

#take player names
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

print('Selecting which player will be X')

#assign x to a player
pick = int(random.randint(0,1)) # Done
print(f'{NAMES[0]} will be X.')

#start game
#alternate chances


#perform checks for winner
