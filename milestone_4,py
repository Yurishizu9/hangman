#%% choose a random word from list
import random

word_list = ['mango', 'banana', 'pear', 'apple', 'coconut']


class Hangman():
    '''_summary_

        Parameters
        ----------
        word_list : _type_
            _description_
        num_lives : int, optional
            _description_, by default 5
        

        Attributes
        ----------
        word : str
            The word to be guessed, picked randomly from the word_list. Remember to import the random module into your script.

        word_guessed : list 
            A list of the letters of the word, with _ for each letter not yet guessed. For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']. If the player guesses 'a', the list would be ['a', '_', '_', '_', '_'].

        num_letters : int 
            The number of UNIQUE letters in the word that have not been guessed yet.

        num_lives : int 
            The number of lives the player has at the start of the game.

        word_list : list 
            A list of words.

        list_of_guesses : list 
            A list of the guesses that have already been tried. Set this to an empty list initially.
                
        '''
    def __init__(self, word_list, num_lives = 5):
        
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(word)
        self.num_letters = len(word)
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []



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