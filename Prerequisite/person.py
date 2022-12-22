from datetime import datetime

'''PERSON CLASS

Create a class called Person
Define its initialiser
It must take in a name, a date_of_birth in ISO format (YYYY-MM-DD), and a list of friends
It should initialise attributes for each of those. Be careful, don't use a default value for friends! This will cause problems whenever you initialise a new instance of the class. To know more about, take a look at this link 
Instantiate your class and test that it works before continuing - do this for every section going forward
Define the __str__ magic method which returns a string representation of the person, detailing their name, DOB and number of friends
Define the __gt__ magic method that defines how to use the greater than sign to compare the age of two people (hint: Compare the DOB of the two people)
Create a method called add_friend, which takes in another instance of the person class and adds it to this instance's friends attribute. Assume that every relationship goes both ways: this method should append each friend to the other's list, in just one call
'''

class Person():
    '''_summary_

    Parameters
    ----------
    name : str
        person's name
    date_of_birth : str
        in the format 'YYYY-MM-DD'
    friends : list, optional
        list of friends, by default it is empty
    '''
    def __init__(self, name, date_of_birth, friends = list()):
        
        self.name = name
        self.date_of_birth = datetime.strptime(date_of_birth, '%Y-%m-%d').date()
        self.friends = friends

    def __str__(self):
        return f'Name: {self.name}, DOB: {self.date_of_birth}, Friends: {len(self.friends)}'

    def __gt__(self, other_person):
        return self.date_of_birth > other_person.date_of_birth

    def add_friend(self, other_person):
        self.friends.append(other_person.name)
        other_person.friends.append(self.friends)
    

tim = Person('Tim', '2012-10-31')
matt = Person('Matt','2000-08-28')

tim.add_friend(matt)

print(tim)
print(matt)
print('Is Matt older than Tim?', matt > tim)

d1 = datetime.strptime('2012-10-31', '%Y-%m-%d').date()
d2 = datetime.strptime('2000-08-28', '%Y-%m-%d').date()

print(f'{d2} > {d1}: {d2 > d1}')