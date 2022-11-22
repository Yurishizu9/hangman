#%% checks if input is vallid
while True:
    guess = input('Please, enter a single alphabetical character: ')
    if len(guess) == 1 and guess.isalpha():
        break
    else:
        print('Invalid letter.')