def my_function():
    x = int(input("What is the maximal length of the triangle side? Enter a number: "))
    solutions = []
    for x in range(5, x):
        for y in range(4, x):
            for z in range(3, x):
                if (x * x == y * y + z * z):
                    solutions.append([x, y, z])
    m = 0
    for solution in solutions:
        if m < max(solution):
            m = max(solution)
    return m


print(my_function())