"""
You are presented with an integer number larger than 5. Your goal is to identify the longest side
possible in a right triangle whose sides are not longer than the number you are given.

For example, if you are given the number 15, there are 3 possibilities to compose right triangles:

1. [3, 4, 5]
2. [6, 8, 10]
3. [5, 12, 13]

The following function shows one way to solve the problem but the code is not ideal or efficient.
Refactor the code based on what you have learned about code simplicity and efficiency.
"""

# Renombré la función y las variables a algo significativo con el propósito de la función. Coloqué dentro de la función
# el input que sólo acepta números enteros y el print le di un formato más amigable. El cálculo de los posibles lados
# que pueden formar el triángulo lo puse en una compreh-
# ensión de lista.

def triangle_longest_side():
    num = int(input("What is the maximal length of the triangle side? Enter a number: "))
    side = 0
    solutions = [[a, b, c] for a in range(5, num) for b in range(4, num) for c in range(3, num) if (a*a == b*b + c*c)]
    for sides in solutions:
        if side < max(sides):
            side = max(sides)
    print(f"The longest side possible is {side}")
    return side
