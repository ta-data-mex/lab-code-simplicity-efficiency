"""
The code below generates a given number of random strings that consists of numbers and 
lower case English letters. You can also define the range of the variable lengths of
the strings being generated.

The code is functional but has a lot of room for improvement. Use what you have learned
about simple and efficient code, refactor the code.
"""
'''
def RandomStringGenerator(l=12, a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']):
    p = 0
    s = ''
    while p<l:
        import random
        s += random.choice(a)
        p += 1
    return s

def BatchStringGenerator(n, a=8, b=12):
    r = []
    for i in range(n):
        c = None
        if a < b:
            import random
            c = random.choice(range(a, b))
        elif a == b:
            c = a
        else:
            import sys
            sys.exit('Incorrect min and max string lengths. Try again.')
        r.append(RandomStringGenerator(c))
    return r

a = input('Enter minimum string length: ')
b = input('Enter maximum string length: ')
n = input('How many random strings to generate? ')

print(BatchStringGenerator(int(n), int(a), int(b)))
'''

#refactored code

#la definicion de la funcion se ha quedado igual, lo que cambie fue el interior
def RandomStringGenerator(l=12, a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']):
    #use una comprenhension, para retornar los valores que se van tomando de la lista de letras en el rango de l
    return "".join(random.choice(a) for x in range(l))


def BatchStringGenerator(n, a=8, b=12):
    #use un try except para eliminar el if y todas las condiciones, el except recibe y resuelve si se puede ejecutar la funcion random choice
    r = []
    for i in range(n):
        try:
            c = random.choice(range(a, b+1))
        except:
            sys.exit('Incorrect min and max string lengths. Try again.')
        #solo puse la el random en el try, para evitar que el error en caso de que se ejecute, afecte otra linea de codigoo
        r.append(RandomStringGenerator(c))
    return r

#en lugar de llamar las librerias en cada parte donde se usan, las invoco desde el comienzo
import random
import sys
#los input desde el comienzo estan en entero y el print sigue igual

a = int(input('Enter minimum string length: '))
b = int(input('Enter maximum string length: '))
n = int(input('How many random strings to generate? '))

print(BatchStringGenerator(n, a, b))