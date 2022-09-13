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
    try:
        print("{:d}".format(value))
    except:
        return False
    return True
