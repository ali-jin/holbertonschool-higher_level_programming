#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
LastDigit = number % 10
string = ""
if LastDigit > 5:
    string = "and is greater than 5"
elif LastDigit < 6 and LastDigit != 0:
    string = "and is less than 6 and not 0"
else:
    string = "and is 0"
print(f"Last digit of {number} is {LastDigit} {string}")
