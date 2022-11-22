# Hangman

## [Milestone 1](#m1)

- I made a GitHub repository
- The technologies I used where [Github](https://github.com/) and [Git](https://git-scm.com/)
- I used Git (a distributed version control system)  to record changes changes to my files overtime. I used GitHub to host my git repository.
 
```bash
git init
```
this initialises a new Git repository

```bash
git add .
```
will stage all files

```bash
git commit -m "First commit"
```
will commit all files in the stagged state `-m` flag is to add a commit message

```bash
git clone <repository-url>
```
clones an existing repository from GitHub onto your system

```bash
git push
```
pushes changes from your system to back to GitHub

![image](https://user-images.githubusercontent.com/67028414/203396676-f37c457b-1174-44ff-a699-3eb1112de41b.png)

## Milestone 2

> does not connect to [Milestone 1](#milestone-1)

- Created variables for the game
- I used `import random`, `if/else`, `isalpha` 
- I used the `random` module to make a random selection from a list of words, `if/else` to set conditions to check if input was a la single character and `isalpha` to check if input was a letter.

```python
word_list = ['mango', 'banana', 'pear', 'apple', 'coconut']
```
Defined a list of possible words.

```python
import random

word = random.choice(word_list)
print(word)
```
Choose a random word from the list.

```python
guess = input('enter a single letter: ')
```
Ask the user for the input.

```python
if guess.isalpha() and len(guess) == 1:
    print('Good guess!')
else:
    print('Oops! That is not a valid input.')
```
Check that the input is a single character.

![image](https://i.imgur.com/giuUFYe.png)


