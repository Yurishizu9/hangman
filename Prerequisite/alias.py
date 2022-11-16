'''
Import Local Modules
Import Modules from Packages
Import Variables from Modules
Making Changes to Modules
Importing 3rd Party Packages
Giving Aliases to Modules
There are many 3rd party packages that share the same name for their modules. For example, datetime has a class called time, and there is another package called time that has a module called time.

Create a new file called alias.py
In alias.py, import time and call time.time(). You should see the current timestamp printed, something like "1661958068.7087212"
'''
import time

print(time.time())


'''
Now, from datetime, import time and call time.time(). You should see an error like: "AttributeError: type object 'datetime.time' has no attribute 'time'"
Instead of calling time.time(), call time(). You should see a time printed, in this case "00:00:00"
'''
from datetime import time
#print(time.time())
print(time())


'''
This is because both time calls are trying to call different functions with the same name. The first time you were calling time.time(), which is a function that returns the current timestamp. The second time you were calling the time() class, which returns an object with the time you specified. If you want to tell them apart, you can give them aliases.

From datetime, import time as datetime_time and call datetime_time(). You should see a time printed, in this case "00:00:00"
From time, import time as time_time and call time_time(). You should see the current timestamp printed, something like "1661958068.7087212"
'''
from datetime import time as datetime_time
from time import time as time_time
print(datetime_time())
print(time_time())