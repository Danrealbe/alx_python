#!/usr/bin/python3
 
def safe_print_division(a, b):
    try:
        quot = a / b

    except ZeroDivisionErro:
        quot = None

    finally:
        print("Inside result: {}".format(quot))
    return quot 
