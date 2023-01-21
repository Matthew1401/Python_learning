"""
Write a program (function!) that takes a list and returns
a new list that contains all the elements of the first list minus all the duplicates.

Extras:
1. Write two different functions to do this - one using a loop and constructing a list, and another using sets.
2. Go back and do Exercise 5 using sets, and write the solution for that in a different function.
"""
import random

a_list = [1, 2, 3, 4, 5, 1]


def removing_duplicates_using_loop():
    new_list = []
    for element in a_list:
        if element not in new_list:
            new_list.append(element)
    return new_list


def removing_duplicates_using_sets():
    return list(set(a_list))


print(removing_duplicates_using_loop())
print(removing_duplicates_using_sets())

# Extra 2
a_list = random.sample(range(0, 100), random.randint(1, 50))
b_list = [random.randint(0, 100) for _ in range(random.randint(1, 50))]


def extra_2():
    c_list = a_list
    for element in b_list:
        c_list.append(element)
    return list(set(c_list))


print(extra_2())
