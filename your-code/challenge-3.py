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
#Wrapped everything up inside the function and changed its logic. It was bothering me that we had 3 nested for loops and wanted to reduce those.
#The previous function used the for loops to create a list with all the combinations possible within the range 3,X (considering a right angle triangle
#cannot have an integer side that is smaller than 3. After having the list, it applied the pytagoras theorem to all the elements in the list.
#It seemed a waste of resources to do all that, so I decided to decompose the theorem and use 1 while loop to check my conditions, from 3 to the limit X.
def my_function():
    #added input to the function
    y = int(input('What is the maximal length of the triangle side? Enter any integer larger than 5: '))
    #added condition that I could not have a maximal length smaller than 5.
    if y < 5:
        return 'Please enter an integer larger than 5.'
    #added initial values to one of my sides (a) and defined my hipotenuse with any value (it will be updated later). Also created a list to store hipotenuse values.
    a = 3
    c = 0
    c_lst = []
    #the loop will continue while my hipotenuse (c) is smaller than the input y.
    while c <= y :
        #if my side a is an even number, then it means that the hipotenuse minus a is necessarily equal to 2. If I transform the theroem in a
        # 2nd degree pair of equations, it is the following system.
        #If a is even, I will apply the equations to the other sides and will check if the results of b and c are integers.
        #if that happens, then I will add my hipotenuse c to a list of valid hipotenuses.
        if a % 2 == 0:
            b = a ** 2 / 4 - 1
            c = a ** 2 / 4 + 1
            if b % 1 == 0 and c % 1 == 0:
                c_lst.append(c)
        #doing the same with the applicable condition if a is an odd number.
        elif a % 2 == 1:
            b = (a ** 2 - 1) / 2
            c = (a ** 2 + 1) / 2
            if b % 1 == 0 and c % 1 == 0:
                c_lst.append(c)
        #after applying the conditions and adding c to the list (or not), I will add 1 to a, so I can test with another set of variables.
        a += 1
    #in the end, when I reach my input, I will have an ordered list with all my valid hipotenuses. I return the last element of the list.
    return c_lst[-1]

print(my_function())
