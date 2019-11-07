#Vamo a intentar simplificar el código
#import sys
#import random

def RandomStringGenerator(len =12, a = list('abcdefghijklmnopqrstuvwxyz0123456789')):
    import random
    string_len = "".join([random.choice[a] for x in range(len)])
    return string_len
    #return print(int(input("Enter minimum string length: "))

def BatchStringGenerator(n, min=8, max=12):
    import sys
    if min > max:
        sys.exit('Incorrect min and max string lengths. Try again.')
    else:
        return [RandomStringGenerator(random.choice(range(min, max))) for i in range(n)]

a = input('Enter minimum string length: ')
b = input('Enter maximum string length: ')
n = input('How many random strings to generate? ')

print(BatchStringGenerator(int(n), int(a), int(b)))
