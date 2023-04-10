#!/usr/bin/python3

import random

# Game instruction
print('Welcome to Rock, Paper, Scissors Game (Type "exit" to leave)\n')

# score [player, computer]
score = [0, 0]

while True:

    # available choices
    choices = ['rock', 'paper', 'scissors']

    # Winning winning_logic {winning_choice: losing_choice}
    winning_logic = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}
    winning_message = {'rock': 'Rock crushes scissors',
                       'paper': 'Paper covers rock',
                       'scissors': 'Scissors cut paper'
                       }

    computer = random.choice(choices)
    player = None

    while player not in choices and player != "exit":
        try:
            player = input('rock, paper or scissors? ').lower()
        except KeyboardInterrupt:
            print(f'\nFinal Score: Player[{score[0]}], Computer[{score[1]}]\nBye!')
            exit()

    # exit if player exits
    if player == 'exit':
        print(f'\nFinal Score: Player[{score[0]}], Computer[{score[1]}]\nBye!')
        exit()

    if winning_logic[player] == computer:
        result = "Player wins! " + winning_message[player]
        score[0] = score[0] + 1
    elif winning_logic[computer] == player:
        result = "Computer wins! " + winning_message[computer]
        score[1] = score[1] + 1
    else:
        result = "Draw"

    print(f"Computer: {computer}")
    print(f"Player: {player}")
    print(f"Result: {result}\n")
    print(f'Score: Player[{score[0]}], Computer[{score[1]}]')
