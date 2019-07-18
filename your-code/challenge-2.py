"""
The code below generates a given number of random strings that consists of numbers and 
lower case English letters. You can also define the range of the variable lengths of
the strings being generated.

The code is functional but has a lot of room for improvement. Use what you have learned
about simple and efficient code, refactor the code.
"""

import random
import sys
def RandomStringGenerator(l=12,characters=list('qwertyuiopasdfghjklzxcvbnm1234567890')):
    string = ''.join([random.choice(characters) for numbers in range(l)])
    return string

def BatchStringGenerator(lenght, minimum=8, maximum=12):
    if minimum > maximum: sys.exit('Incorrect min and max string lengths. Try again.')
    else: maximum = maximum + 1
    return [RandomStringGenerator(random.choice(range(minimum,maximum))) for i in range(lenght)] 

a = input('Enter minimum string length: ')
b = input('Enter maximum string length: ')
n = input('How many random strings to generate? ')

BatchStringGenerator(int(n), int(a), int(b))
