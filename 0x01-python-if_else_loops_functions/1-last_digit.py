#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = "Last digit of"
last_digit = number % 10
while number < 0:
    number *= -1
    last_digit = number % 10 
    last_digit *= -1
    number *= -1
if last_digit > 5:
    print(str + number + "is" + last_digit +"and is greater than 5")
elif last_digit == 0:
    print(str + number + "is" + last_digit +"and is 0")
elif last_digit < 6 and last_digit != 0:
    print(str + number + "is" + last_digit +"and is less than 6 and not 0")
