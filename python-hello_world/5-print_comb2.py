#printing combination of number

for number in range(0, 100):
    if number ==90:
        print("{}".format(number))
    else:
        print("{:02},".format(number), end=" ")
