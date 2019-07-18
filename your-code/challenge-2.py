import sys
import random

def RandomStringGenerator(l=12, characters=list('1234567890qwertyuiopasdfghjklzxcvbnm')):
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