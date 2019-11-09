"""
The code below generates a given number of random strings that consists of numbers and
lower case English letters. You can also define the range of the variable lengths of
the strings being generated.

The code is functional but has a lot of room for improvement. Use what you have learned
about simple and efficient code, refactor the code.
"""
import random
import sys


def randomStringGenerator():
    letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v','w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    long = 12
    acumulador = 0
    string_generated = ''
    while acumulador < long:
        string_generated += random.choice(letras)
        acumulador += 1
    return string_generated

print(randomStringGenerator())
print(randomStringGenerator())
print(randomStringGenerator())


def BatchStringGenerator():
    min = int(input('Enter minimum string length: '))
    max = int(input('Enter maximum string length: '))
    num_string = int(input('How many random strings to generate? '))
    list_c = []
    randomChoice = None
    for i in range(num_string):
        if min < max:
            randomChoice = random.choice(range(min, max))
        elif min == max:
            randomChoice = min
        else:
            sys.exit('Incorrect min and max string lengths. Try again.')
        list_c.append(randomStringGenerator())
    return list_c

print(BatchStringGenerator())

