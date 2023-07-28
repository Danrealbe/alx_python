#!/usr/bin/python3
 
def safe_print_division(a, b):

    try:
        quote = a/b

    except ZeroDivisionErro:
        quote = None

    finally:
        print("Inside result:{}".format(quote))
    return quote 
