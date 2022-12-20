#%% choose a random word from list
import random

word_list = ['mango', 'banana', 'pear', 'apple', 'coconut']
word = random.choice(word_list)
print(word)

#%% checks if user character input is vallid
def ask_for_input():
    while True:
        guess = input('Please, enter a single alphabetical character: ')
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print('Invalid letter.')
    check_guess(guess)

#%% check wether the guess is in the word
def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print(f'Good guess! "{guess}" is in the word.')
    else:
        print(f'Sorry, "{guess}" is not in the word. Try again.')

ask_for_input()