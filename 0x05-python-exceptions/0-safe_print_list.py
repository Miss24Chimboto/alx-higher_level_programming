#!/usr/bin/python3
"""
Safe print a list
my_list: the list to print
x: number of elements to print
Returns:
The real number of elements printed
"""
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            count += 1
    except:
        print()
        return count
    print()
    return count
