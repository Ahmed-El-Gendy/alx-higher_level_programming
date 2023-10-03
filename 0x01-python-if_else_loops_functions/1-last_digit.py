#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
i = abs(number)
if i % 10 > 5:
    print(f"Last digit of {number} is {i%10} and is greater than 5")
elif i % 10 == 0:
    print(f"Last digit of {number} is {i%10} and is 0")
else:
    print(f"Last digit of {number} is {i%10} and is less than 6 and not 0")
