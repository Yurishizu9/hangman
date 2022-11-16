'''
Given a list named my_list, write a program that checks if all the elements in the list are unique.

If the elements are unique, print 'All elements are unique'. If there are duplicate elements, print 'There are duplicate elements'.
'''


# %%
my_list = [2, 5, 2, 4]
print(my_list)


# %%
# method 1 use .count()

for x in range(len(my_list) - 1):
    if my_list.count(x) == 2:
        print(f'found a duplicate: {my_list[x]}')


# %%  
# method 2 turn list into sets and compare the length

my_set = set(my_list)
if len(my_list) != len(my_set):
    print(f'found a duplicates')


# %%
# method 3 seperating duplicates from the list with for loop

new_list = []
for x in my_list:
    if x not in new_list:
        new_list.append(x)
    else:
        print(f'found a duplicate: {x}')


# %%
# method 4 record occurances of items in a list to a disctionary

counter = {}
for x in my_list:
    if x not in counter:
        counter[x] = 1
    else:
        counter[x] += 1

for k, v in counter.items():
    if v > 1:
        print(f'found a duplicate: {k}')
# %%
