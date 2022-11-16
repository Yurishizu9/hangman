'''
The program asks two inputs from the user: player1 and player2. The inputs can be either 'rock', 'paper' or 'scissors'.

Code the logic of the game to see who wins. Print the result like: 'Player 1 wins' or 'Player 2 wins'
If one of the inputs is not 'rock', 'paper' or 'scissors', print 'Invalid input'
If both inputs are the same, print "It's a tie"
'''


# %%
player_1 = 'rock' #input('Player 1 choose "rock", "paper" or "scissors": ')
player_2 = 'lizard' #input('Player 2 choose "rock", "paper" or "scissors": ')

valid_moves = ["rock", "paper", "scissors"]

if player_1 not in valid_moves or player_2 not in valid_moves:
    print(f'Player 1: {player_1}\nPlayer 2: {player_2}\nInvalid input')
else:
    if player_1 == player_2:
        print(f'Player 1: {player_1}\nPlayer 2: {player_2}\nIt\'s a tie')
    
    elif player_1 == 'scissors' and player_2 == 'paper' or player_1 == 'paper' and player_2 == 'rock' or player_1 == 'rock' and player_2 == 'scissors':
        print(f'Player 1: {player_1}\nPlayer 2: {player_2}\nPlayer 1 wins')
    else:
        print(f'Player 1: {player_1}\nPlayer 2: {player_2}\nPlayer 2 wins')
# %%
