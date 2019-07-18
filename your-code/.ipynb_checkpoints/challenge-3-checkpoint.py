'''"""
You are presented with an integer number larger than 5. Your goal is to identify the longest side
possible in a right triangle whose sides are not longer than the number you are given.

For example, if you are given the number 15, there are 3 possibilities to compose right triangles:

1. [3, 4, 5]
2. [6, 8, 10]
3. [5, 12, 13]

The following function shows one way to solve the problem but the code is not ideal or efficient.
Refactor the code based on what you have learned about code simplicity and efficiency.
"""

def my_function(X):
    solutions = []
    for x in range(5, X):
        for y in range(4, X):
            for z in range(3, X):
                if (x*x==y*y+z*z):
                  solutions.append([x, y, z])
    m = 0
    for solution in solutions:
        if m < max(solution):
            m = max(solution)
    return m

X = input("What is the maximal length of the triangle side? Enter a number: ")

print("The longest side possible is " + str(my_function(int(X))))'''

#refactored code
# la definicion de la funcion se queda igual, sin cambio alguno
def my_function(X):
#Hice un list comprenhention, aunque creo que no fue lo mas optimo, en especial porque al momento de agregarlo a la lista, estoy agregando una lista con listas
    solutions = [[x,y,z] for x in range(5, X) for y in range(4, X) for z in range(3, X) if (x*x==y*y+z*z)]
    #por lo que al momento de retornarlo, tengo que sacar el maximo del maximo y creo que esta solucion no esta taaaan cool
    return max(max(solutions))

X = input("What is the maximal length of the triangle side? Enter a number: ")

print("The longest side possible is " , my_function(int(X)))