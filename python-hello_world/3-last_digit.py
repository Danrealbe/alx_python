#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = abs(number) % 10
# soluction 
if number >= 5:
        digit = - digit
            print("Last digit of {} is {} and is".format(number, digit), end="")
                print("{} the string is greater than 5".format(number))
            elif number == 0:
                    print("{} the string and is 0".format(number))
                else:
                        print("{} less than 6 and not 0".format(number))
