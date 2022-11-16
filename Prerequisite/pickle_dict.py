'''
Create a script that stores a dictionary in a pickle file and then read it back into Python.

Create a new file called pickle_dict.py
In pickle_dict.py, import pickle
Create a dictionary called my_dict with the keys a, b, and c and the values 1, 2, and 3
Create a context manager that opens a file called my_dict.pkl in write mode and writes my_dict to the file.
You should see a file called my_dict.pkl in your directory. If you try to open it, you will see a bunch of gibberish. This is because it is a pickle file and not a text file.
'''

import pickle

my_dict = {
    'a': 1,
    'b': 2,
    'c': 3
}

with open('my_dict.pkl', 'wb') as file:
    pickle.dump(my_dict, file)

