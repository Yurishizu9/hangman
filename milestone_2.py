#%% choose a random word from list
import random

word_list = ['mango', 'banana', 'pear', 'apple', 'coconut']
word = random.choice(word_list)
print(word)

#%% ask the user for the input
guess = input('enter a single letter: ')

if guess.isalpha() and len(guess) == 1:
    print('Good guess!')
else:
    print('Oops! That is not a valid input.')
# %%
