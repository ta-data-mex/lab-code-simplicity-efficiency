"""
The code below generates a given number of random strings that consists of numbers and 
lower case English letters. You can also define the range of the variable lengths of
the strings being generated.

The code is functional but has a lot of room for improvement. Use what you have learned
about simple and efficient code, refactor the code.
"""

#This cost me a lot of work just to understand the code since it had too many variables and all of them with
#terrible names that meant nothing.
#Also, having a simple operation like this split between 2 different functions does not seem to be very smart
#It was also bothering me that the order of the steps was not intuitive, I needed it to 'flow better'
#So, I will guide you to my steps:

def RandomStringGenerator():
    #inputs inside the function, wrap it all up. also rename them to make some sense
    minimo = int(input('Enter minimum string length: '))
    maximo = int(input('Enter maximum string length: '))
    limite = int(input('How many random strings to generate? '))
    #import string module so do not need to have a huge list of manually written strings
    import string
    import random
    #define chars variable for lowercase and digits
    chars = string.ascii_lowercase + string.digits
    #empty list where our strings will go
    str_lst = []
    #prevent errors
    if minimo > maximo:
        return 'Incorrect min and max string lengths. Try again.'
    #loop to have the same operation the number of times we need.
    while len(str_lst) < limite:
        #tmp variable for our random choice
        tmp = random.choice(range(minimo, maximo + 1))
        #tmp string to create strings
        tmp_str = ''.join(random.choice(chars) for _ in range(tmp))
        #add string to list
        str_lst.append(tmp_str)
    #return list
    return str_lst

print(RandomStringGenerator())