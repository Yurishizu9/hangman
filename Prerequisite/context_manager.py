
'''
Create a new file called context_manager.py
In context_manager.py, create a context manager that opens a file called test.txt in write mode and writes the message "Hello, I am a context manager!" to the file.
You should see the message "Hello, I am a context manager!" in the file test.txt
If you don't close the file, you might not be able to open it again!
'''
with open('test.txt', 'w') as file:
    file.write('Hello, I am a context manager!')

'''
You can also read the file using context managers.

In context_manager.py, create a context manager that opens the file test.txt in read mode and prints the contents of the file
Test that it works by running python context_manager.py in the terminal.
You should see the message "Hello, I am a context manager!" printed in the terminal
'''
with open('test.txt', 'r') as file:
    print(file.read())