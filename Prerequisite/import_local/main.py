'''Inside the import_local folder, you will find four files and a folder called package_1.

In main.py, import function_1 from module_1 and call it. Test it works by running python main.py in the terminal. You should see the message "This is function 1 in module 1"
Import function_2 from module_1 and call it. Test it works by running python main.py in the terminal. You should see the message "This is function 2 in module 1"
Now, import function_1 from module_2 and call it. Test it works by running python main.py in the terminal. You should see the message "This is function 1 in module 2"
Notice that you imported function_1 twice. Which one got called when you ran python main.py? Why?
'''
import module_1
module_1.function_1()
module_1.function_2()

import module_2
module_2.function_1()


'''
In main.py, import function_package() from package_1.module_1 and call it. Test it works by running python main.py in the terminal. You should see the message "I am in function_package() in package_1/module_1.py"
Notice that you can import modules that are inside a package, just like you can import modules that are in the same folder as your main file. This makes it easier to organise your code into different files and folders.
'''
from package_1.module_1 import function_package
function_package()


'''
Open module_2.py. Check that there is a variable called x in the file. This variable is not inside a function, so it is a global variable and you can access it from any other file.

In main.py, import x from module_2 and print it. Test that it works by running python main.py in the terminal. You should see the message 'Hello, I am in module 2'
Now, in main.py, create another variable called x and assign it the value "Hello, I am in main.py". Then, print x. Test that it works by running python main.py in the terminal. You should see the message "Hello, I am in main.py"
Notice that the value of x has changed now. This is because you overwrote the value of x when running main.py.
'''
from module_2 import x
print(x)
x = 'Hello, I am in main.py'
print(x)


