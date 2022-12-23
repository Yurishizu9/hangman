import random

word_list = ['mango', 'banana', 'pear', 'apple', 'coconut']


class Hangman():
    '''_summary_

        Parameters
        ----------
        word_list : list
            list of words to use for the game
        num_lives : int, optional
            chances for the player to make wrong guesses, by default 5
        

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
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(self.word)
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
    

    def check_guess(self, guess):
        '''check wether the guess is in the word.
        - if yes adds guess word guess.
        - if not take a life away.
        - add all guesses to list of guesses.

        Parameters
        ----------
        guess : str
            players character input
        '''
        guess = guess.lower()
        if guess in self.word:
            print(f'Good guess! "{guess}" is in the word.')
            for idx, x in enumerate(self.word):
                if x == guess:
                    self.word_guessed[idx] = x
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f'Sorry, {guess} is not in the word.')
            print(f'You have {self.num_lives} lives left.')
        self.list_of_guesses.append(guess)


    def ask_for_input(self):
        '''asks for user character input and checks if it's vallid.
        - if it is it calls check_guess
        - if not ask for user input again

        '''
        while True:
            guess = input('Please, enter a single alphabetical character: ')
            if len(guess) != 1 and guess.isalpha():
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)


game_1 = Hangman(word_list)
game_1.ask_for_input()