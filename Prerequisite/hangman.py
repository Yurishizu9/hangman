import random

class Hangman():
    '''a game of hangman

        Parameters
        ----------
        lives : _int_
            how many lives the player has
        word_list : _str_
            a word or selection of words you want to use for the game
        '''

    def __init__(self, lives, *word_list):
        self.word_list = word_list
        self.lives = lives

    def new_game(self):
        '''starts a new game
        '''
        # Choose a random word from list
        self.word = random.choice(self.word_list)
        # keeps track of the character that have been gueesed right
        self.guessed_right = ['_'] * len(self.word)
        self.ask_for_input()


    def ask_for_input(self):
        '''checks if user input is vallid
        '''
        while True:
            print(f'\nWord:', *self.guessed_right, sep=' ')
            print('lives:', self.lives)
            self.guess = input('Please, enter a single alphabetical character: ')
            if len(self.guess) == 1 and self.guess.isalpha():
                break
            else:
                print('Invalid letter.')
        self.check_guess()


    def check_guess(self):
        '''checks whether the guess is in the word
        '''
        self.guess = self.guess.lower()
        
        # is guess in word?
        if self.guess in self.word: 
            
            # have you already made this guess?
            if self.guess in self.guessed_right: 
                print(f'You already guessed "{self.guess}". Try again.')
                self.lives -= 1 # lose a lives
            else: 
                print(f'Good guess! "{self.guess}" is in the word.')
                self.find_all_occurence()
        else: 
            print(f'Sorry, "{self.guess}" is not in the word. Try again.')
            self.lives -= 1 # lose a lives
        self.is_game_over()


    def find_all_occurence(self):
        '''find all occurances of guess in word and updates guessed_right attribute
        '''
        for idx, val in enumerate(self.word):
            if val == self.guess:
                self.guessed_right[idx] = self.guess


    def is_game_over(self):
        '''checks to see if the game is over
        '''
        if '_' not in self.guessed_right:
            print('\nYou win!')
        elif self.lives == 0:
            print('\nYou lose!')
        else:
            self.ask_for_input()


# settings
game1 = Hangman(8, 'mango', 'banana', 'pear', 'apple', 'coconut')

# start game
game1.new_game()



