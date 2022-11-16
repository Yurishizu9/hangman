'''
You can read the contents of the pickle file back into Python.

Create a new file called read_pickle_dict.py
In read_pickle_dict.py, import pickle
Create a context manager that opens the file my_dict.pkl in read mode and reads the contents of the file into a variable called my_dict
Print my_dict. You should see the dictionary printed.
'''
import pickle

with open('my_dict.pkl', 'rb') as file:
    print(pickle.load(file))