#!/usr/bin/python3
for num in range(90):
    if (num == 89):
        print(num)
    elif ((num % 10) > (num / 10)):
        print("{:02d}, ".format(num), end="")
