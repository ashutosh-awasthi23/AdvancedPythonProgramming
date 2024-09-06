"""Hello I am docstring"""


def get_integer_input():
    """Hello I am docstring inside a function"""

    try:
        num = int(input("\nEnter number: "))
        print(f"The entered number is {num}")
    except ValueError:
        print("Value Error handled gracefully")


def get_element_from_list():
    li = [1, 2, 3, 4, 5, 6]
    try:
        i = int(input("\nEnter index: "))
    except IndexError:
        print("Given index is out of bound!")
    except TypeError:
        print("Type error occurred!")
    else:
        print(f"Element: {li[i]}")
    finally:
        print("Operation completed...")


def divide_numbers():
    a = 10
    b = 0
    try:
        d = a / b
        print(d)
    except ZeroDivisionError:
        print("\nDenominator is zero!!")


#
# get_integer_input()
# get_element_from_list()
# divide_numbers()
print(__doc__)
print(get_integer_input.__doc__)
