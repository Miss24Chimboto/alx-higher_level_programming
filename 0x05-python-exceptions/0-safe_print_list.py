#!/usr/bin/python3
def safe_print_integer(value):
    """
    Safe print a list
    Args:
        my_list: the list to print
        x: number of elements to print
    Returns:
        Returns the real number of elements printed
    """
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


