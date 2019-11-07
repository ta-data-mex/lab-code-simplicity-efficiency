#Se hace de nuevo una función

def my_function(X):
    m, solutions = 0, [[x, y, z] for x in range(5, X) for y in range(4, X) for z in range(3, X) if (x*x==y*y+z*z)]
    return max([max(s) for s in solutions if m < max(s)])
X = my_function(int(input("What is the maximal length of the triangle side? Enter a number: ")))
print(f"The longest side possible is {X}")