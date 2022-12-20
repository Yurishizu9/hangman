# %%
'''VOID FUNCTIONS

A function that doesn't return anything is called a void function. In Python, you can define a void function by simply not including a return statement.

Create a function called void_function that doesn't return anything
Inside the function, print the string "This is a void function."
Call the function and assign the result to a variable called void_result
Print the value of void_result
What is the value of void_result? Why?

Notice that even though the function doesn't return anything, it still prints the string "This is a void function." to the console. This is because the print function still runs inside the function, even though the function doesn't return anything.

This is important to remember, sometimes you want your functions to perform actions without returning anything.
'''
def void_function():
    print('This is a void function')

void_result = void_function()
print(void_result)


# %%
'''RANGE CHECKER

Write a function called in_range which takes in three arguments: lower_bound, upper_bound, and number
If number is between lower_bound and upper_bound, print "{number} is between {lower_bound} and {upper_bound}."
If it isn't, print "{number} is NOT between {lower_bound} and {upper_bound}."
Call your function to test it
'''

def in_range(lower_bound, upper_bound, number):
    if lower_bound <= number <= upper_bound:
        print(f'{number} is between {lower_bound} and {upper_bound}')
    else:
        print(f'{number} is NOT bewteen {lower_bound} and {upper_bound}')
in_range(2, 4, 7)


# %%
'''BOOLEAN RANGE CHECKER

Write a function called in_range which takes in three arguments: lower_bound, upper_bound, and number
If number is between lower_bound and upper_bound, return True
If it isn't, return False
Call your function to test it
'''
def in_range(lower_bound, upper_bound, number):
    if lower_bound <= number <= upper_bound:
        return True
    else:
        return False
print(in_range(2, 4, 7))


# %%
'''RETURN A UNIQUE ITEM LIST 

Write a function called unique_list that takes in a list and returns a list with only the unique elements of the input.
'''
def unique_list(l: list):
    l = set(l)
    return list(l)

my_list = [1, 3, 5, 6, 4, 3, 2, 3, 3, 4, 3, 4, 5, 6, 6, 4, 3, 2, 12, 3, 5, 63, 4, 5, 3, 3, 2]
print(unique_list(my_list))

'''
Find another way of performing the same operation without defining a function.
'''
print(list(set(my_list)))


# %%
'''VOLUME OF A SPHERE

Write a function called volume_of_sphere that takes in a variable called radius which is the radius of a sphere
The function calculates the volume of a sphere. Search online for the formula for calculating the volumne and use PI = 3.14
The function should return the volume of the sphere rounded to 2 decimal points
Call your function to test it
'''
def volume_of_sphere(radius):
    PI = 3.14
    # volume = (4/3) × π × r³
    return round(4/3 * PI * radius**3, 2)
print(volume_of_sphere(4),'cm³') 
# 267.95 cm³


# %%
'''DEFAULT ARGUMENTS

Create a function which takes in a dictionary of attributes about a piece of clothing and prints each of the key-value pairs on a line
Define a function parameter called attributes_to_print with a default argument of 'all'
If a list is passed into the function as the attributes_to_print, print only the key-value pairs of the dictionary where the key exists in attributes_to_print. Otherwise, print them all.
Print a message to tell the user if a key doesn't exist
Call your function to test it
'''
def clothes( attr: dict, attributes_to_print = 'all'):
    for k, v in attr.items():
            print(f'{k}: {v}')
    
    print(f'\nSearch results for {attributes_to_print} attributes')

    if type(attributes_to_print) == list:
        for k, v in attr.items():
            if k in attributes_to_print:
                print(f'{k}: {v}')
    else:
        for k, v in attr.items():
            print(f'{k}: {v}')

clothes({'Gfg': 1, 'best': 3, 'is': 2}, ['Gfg', 'bests', 'ix']) 


# %%
'''PROFILE VALIDATOR

Create a function which takes in the name, age, and email of a user trying to create a new profile on our application
Check the name does not contain any of the following characters "!@£$%^&*()"
Check the email is valid by making sure it contains "@"
Check the age > 12
Turn each step above into a function, so that you have one function, whiich calls 3 other functions inside
Print a friendly error to explain the issue to the user if any of these checks does not pass
'''
def user(name, age, email):
    error = []
    error.append(name_check(name))
    error.append(email_check(email))
    error.append(age_check(age))

    if error == [None, None, None]:
        print('Profile created successfuly')
    else:
        for e in error:
            if e != None:
                print(f'- {e}')

def name_check(name):
    invalid_char = set('!@£$%^&*()')
    for x in invalid_char:
        if x in name:
            return f'name should not contain invalid characters {invalid_char}'

def email_check(email):
    if '@' not in email:
        return f'your email is invalid'

def age_check(age):    
    if not age > 12:
        return 'you must be at least 13 to join'

user('T!m', 12, 'exampleemail.com')


# %%
'''ZODIAC YEAR

How to Calculate Your Chinese zodiac sign mathematically?
Divide your year of birth by 12 and read about the remainder. 
If the number of the year can be divided with no remainder, take the remainder as zero. 
Each remainder corresponds to an animal sign.

0: Monkey
1: Rooster 
2: Dog 
3: Pig
4: Rat
5: Ox 
6: Tiger 
7: Rabbit
8: Dragon 
9: Snake 
10: Horse 
11: Sheep

source: https://www.travelchinaguide.com/intro/social_customs/zodiac/calculator.htm
'''
def zodiac_sign(year):
    animal = {
        0: 'Monkey',
        1: 'Rooster',
        2: 'Dog', 
        3: 'Pig',
        4: 'Rat',
        5: 'Ox', 
        6: 'Tiger', 
        7: 'Rabbit',
        8: 'Dragon', 
        9: 'Snake', 
        10: 'Horse', 
        11: 'Sheep'
    }
    return animal[year % 12]
year_of_birth = 2000
print(zodiac_sign(year_of_birth))


# %%
'''FACTORIAL FUNCTION

A recursive function is a function that calls itself. This is useful when you want to perform an operation on a number and all the numbers below it.

Define a recursive function called factorial that returns the factorial of a given number.

Define a function called factorial that takes in a number
If the number is 0, return 1
Otherwise, return the number multiplied by the factorial of the number minus 1. In this case, you have to call the function again inside itself.
Call your function to test it. Use the number 5 as an input, you should get 120 as an output.
'''
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)

print(factorial(5))
# factorial(5)
# 5 x 4 x 3 x 2 x 1 = 120


# %%
'''RECURSIVE FIBONACCI FUNCTION

Create a function which takes in an integer n, and when called, returns a list of the first n Fibonnaci numbers.
It should be a recursive function which calls itself inside the function body.
'''

def fibonnaci(n):
    #print(n)
    if n <= 2:
        return n - 1
    else:
        '''
        Honestly It is very hard to visualise/dry test this code
        I will have to revisit it again
        '''
        #print(f'{fibonnaci(n - 1)} + {fibonnaci(n - 2)} = {fibonnaci(n - 1) + fibonnaci(n - 2)}')
        return fibonnaci(n - 1) + fibonnaci(n - 2)
print(fibonnaci(6))  


# %%
'''FIBONNACI LOOP

- Write a for loop that prints the first 100 Fibonnaci numbers
- Create a function which returns True if the number is a multiple of 7 and False otherwise
- Call this function on each number inside your loop
- Add an elif condition to the loop to call another new function which checks if 
the number is greater than or equal to 100 OR is less than 50. In the case that it is 
True, format a string that prints the number and either "is larger than 100" or "is less than 50".
'''
def multiple_of_seven(n):
    return True if n % 7 == 0 else False


def fifty_to_hundred(n):
    if n >= 100 or n < 50:
        return True
    else:
        return False


a = 0
b = 1


for x in range(30):
    print(f'\n{a}')
    if multiple_of_seven(a):
        print('is multiple of seven')
    elif fifty_to_hundred(a):
        if a >= 100:
            print('is larger than 100')
        else:
            print('is less than 50')
    a, b = b, a + b



# %%
'''INVERSE
Define a recursive function called inverse that returns the inverse of a string, 
where the start and end characters appear at the middle of the word
'''
def inverse(word):
    if len(word) == 1:
        return word
    else:
        return word[-1] + inverse(word[1:-1]) + word[0]

print(inverse('hello'))


# %%
'''PALINDROME

A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward or forward. 
This includes capital letters, punctuation, and other special characters.

- Write a function that takes in a string and returns True if it is a palindrome and False otherwise
- Write a function that takes in a string and returns True if it is a palindrome and False otherwise. 
This time, ignore capitalisation and punctuation.

There are several ways to implement this. Some require less code, but some are more efficient; 
which is yours, and can you think of how to implement the other way?
'''
def palindrome(word):

    # if one character is left, return True
    if len(word) == 1:
        return True

    # when 2 chracters are left
    # check if they match 
    # then return True
    elif len(word) == 2:
        return word[0] == word[1]        
    else:
        # checks if the first and last character are a match, return True
        # check the rest of the word without the first and last characters is a palindrone, return True
        # need two truths to return True 
        return word[0] == word[-1] and palindrome(word[1:-1])

print(palindrome('racecar'))