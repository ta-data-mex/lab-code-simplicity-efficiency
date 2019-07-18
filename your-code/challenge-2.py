"""
The code below generates a given number of random strings that consists of numbers and 
lower case English letters. You can also define the range of the variable lengths of
the strings being generated.

The code is functional but has a lot of room for improvement. Use what you have learned
about simple and efficient code, refactor the code.
"""
import random
import sys

def BatchStringGenerator(n_str, min_range, max_range):
    if min_range < max_range:
        list_str = [RandomStringGenerator(random.choice(range(min_range, max_range))) for i in range(n_str)]
    elif min_range==max_len:
        list_str = [RandomStringGenerator(min_range) for i in range(n_str)]
    else:
        sys.exit('Incorrect min and max string lengths. Try again.')
    return list_str

def RandomStringGenerator(length):
    LETTERS = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
               'o','p','q','r','s','t','u','v','w','x','y','z','0','1',
               '2','3','4','5','6','7','8','9']
    s = ''
    for i in range(length):
        s += random.choice(LETTERS)
    return s

min_len = input('Enter minimum string length: ')
max_len = input('Enter maximum string length: ')
num_str = input('How many random strings to generate? ')

print(BatchStringGenerator(int(num_str), int(min_len), int(max_len)))