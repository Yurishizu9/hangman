# Hangman

## Milestone 1

>  Set up the environment.

I made a GitHub repository. The technologies I used were [Github](https://github.com/) and [Git](https://git-scm.com/). I used Git (a distributed version control system) to record changes to my files overtime. I used GitHub to host my git repository.

---

this initialises a new Git repository

```bash
git init
```

will stage all files

```bash
git add .
```

will commit all files in the stagged state `-m` flag is to add a commit message

```bash
git commit -m "First commit"
```

clones an existing repository from GitHub onto your system

```bash
git clone <repository-url>
```

pushes changes from your system to back to GitHub

```bash
git push
```

![image](https://user-images.githubusercontent.com/67028414/203396676-f37c457b-1174-44ff-a699-3eb1112de41b.png)

## Milestone 2

>Create the variables for the game

This does not connect to [~~Milestone 1~~](#milestone-1). I created variables for the Hangman game.
I used `import random`, `if/else`, `isalpha`. Furthermore, I used the `random` module to make a random selection from a list of words, `if/else` to set conditions to check if input was a la single character and `isalpha` to check if input was a letter.

---

Defined a list of possible words.

```python
word_list = ['mango', 'banana', 'pear', 'apple', 'coconut']
```

Choose a random word from the list.

```python
import random

word = random.choice(word_list)
print(word)
```

Ask the user for the input.

```python
guess = input('enter a single letter: ')
```

Check that the input is a single character.

```python
if guess.isalpha() and len(guess) == 1:
    print('Good guess!')
else:
    print('Oops! That is not a valid input.')
```

Here is the output.

![image](https://i.imgur.com/giuUFYe.png)

## Milestone 3

>Check if the guessed character is in the word

This connects to [Milestone 2](#milestone-2) as I had to extend and cleaned up the hangman code. I used functions and parameters to check if the guessed letter was in the randomly chosen word. Not only do I have an organized code, but now I can reuse parts of the code as many times.

---

The `ask_for_input` function iteratively checks if the user input is valid and also calls the `check_guess()` function, passing the `guess` parameter with it.

```python
def ask_for_input():

    while True:

        guess = input('Please, enter a single alphabetical character: ')

        if len(guess) == 1 and guess.isalpha():

            break

        else:

            print('Invalid letter.')

    check_guess(guess)
```

The `check_guess` function checks whether the guess is in the word.

```python
def check_guess(guess):

    guess = guess.lower()

    if guess in word:

        print(f'Good guess! "{guess}" is in the word.')

    else:

        print(f'Sorry, "{guess}" is not in the word. Try again.')
```

Here, I call the `ask_for_input()` function to start the game.

```python
ask_for_input()
```


## Milestone 4

>Create the Game class

This connects to [Milestone 3](#milestone-3). I used Object-Oriented Programming to develop an almost complete Hangman game. I used classes, methods, and magic methods to achieve this.

---

Here is how my code is looks. I have included comments to readable.

```python
import random

class Hangman():
    '''Hangman Game
    
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

  
  
word_list = ['mango', 'banana', 'pear', 'apple', 'coconut']
game_1 = Hangman(word_list)
game_1.ask_for_input()
```

## Milestone 5

>Putting it all together

This connects to [Milestone 4](#milestone-4). I coded the logic of the game using while loops, breaks, and functions. I now have a completed game.

---

I had to indent `self.num_letters -= 1` so it was in the `else` block as I was facing a weird bug where `word_guessed` and `num_letters` did not sync together when guessing a word that had letters appear more than once like “coconut”. For example, if you guess the letters “c” and “o” the values of these attributes will be `word_guessed = ['c','o','c','o','','','',]`
and `num_letters = 5` even though there are only **three** more letters left to guess the program thinks there are **five**.
 
Here is how the code looks.

```python
import random
 

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
        print(self.word)
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
                break
```

At the end, I added `play_game()` function to complete the game logic. It basically checks I have run out of lives or letters to guess to end or carry the game on.

There was another bug where the game didn't stop if I lose or win, and I was stuck in an infinite loop of _"Please, enter a single alphabetical character: "_. I fixed it by adding `break` 's in the while loops. When you lose or win the game, and in `ask_for_input()` in the `else` block. 

The rest of the code is below.

```python
  
def play_game(word_list):
    game = Hangman(word_list, 5)
    while True:
        if game.num_lives == 0:
            print('You lost!')
            break
        elif game.num_letters > 0:
            print(game.num_letters)
            print(game.word_guessed)
            game.ask_for_input()
        else:
            print('Congratulations. You won the game!')
            break 
  

word_list = ['mango', 'banana', 'pear', 'apple', 'coconut']
play_game(word_list)
```

## Conclusions

I enjoyed this module I learnt so much in the prerequisites, with the bash commands, OOP, packing with \*args and \*\*kwargs, enumerate() function, et cetera.

I found some prerequisite topic difficult at first, and I am glad I went through it because it made doing the milestone tasks a breeze. For example, there was a prerequisite task to make an OOP version of the hangman game way before I did it in the milestone. I am surprised I nailed it. I had all the required features of the game, though implementation were slightly different.

Not only that, but I understood everything within this module apart from `ModuleNotFoundError`. Which I didn't cover in any of the milestone, it was a prerequisite. 

I know that child classes can bypass raised `ModuleNotFoundError` in a parent class, but how is that possible?

I have tried digging on the internet, but I can't seem to find anyone talking about this specific scenario of child classes bypassing that raised error in the parent class. I hope to bring it up to one of my mentors.

There were some critical instruction. That were missed in the tasks. Which led to the bugs in [Milestone 5](#milestone-5). I took the initiative to fix those bugs and will be letting one of the mentors know about it, so the newer students don't get completely lost.
