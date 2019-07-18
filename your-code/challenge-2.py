"""
The code below generates a given number of random strings that consists of numbers and 
lower case English letters. You can also define the range of the variable lengths of
the strings being generated.

The code is functional but has a lot of room for improvement. Use what you have learned
about simple and efficient code, refactor the code.
"""

# moví afuera de las funciones las librerías a importar para que funcionen en todo el ambiente
# y mejor lectura del código
import random
import string
import sys


# Reduje la función random_string_generator y renombre a las dos para que se ajustaran a la etiqueta de Python

def random_string_generator(length = 5):
    letters_digits = string.ascii_letters + string.digits #trae todas las letras y numeros
    return''.join(random.choice(letters_digits) for i in range(length)) #regresa lo mismo que el while pero con un for loop y un join

# Renombre las variables de la función para que sean significativos los nombres y sea más fácil leer el código

def batch_string_generator(repeat, minimun=8, maximun=12):
    random_strings = []
    long = None
    for i in range(repeat):
        if minimun < maximun:
            long = random.choice(range(minimun, maximun))
        elif minimun == maximun:
            long = minimun
        else:
            sys.exit('Incorrect min and max string lengths. Try again.')
        random_strings.append(random_string_generator(long))
    return random_strings

minimun = input('Enter minimum string length: ')
maximun = input('Enter maximum string length: ')
repeat = input('How many random strings to generate? ')

print(batch_string_generator(int(repeat), int(minimun), int(maximun)))



