#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
count = 0
#print function
def print_last_digit():
    if last_digit > 5:
        print("Last digit of {:d} is {:d} and is greater than five".format(number, last_digit))
    elif last_digit == 0:
        print("Last digit of {:d} is {:d} and is zero".format(number, last_digit))
    else:
        print("Last digit of {:d} is {:d} and is less than 6 and not zero".format(number, last_digit))         

if number < 0:
    number *= -1
    count = 1    
last_digit = number % 10


if count == 1:
    number *= -1
    last_digit *= -1
    print_last_digit
else:
    print_last_digit



