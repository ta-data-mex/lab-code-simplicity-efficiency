"""
This is a dumb calculator that can add and subtract whole numbers from zero to five.
When you run the code, you are prompted to enter two numbers (in the form of English
word instead of number) and the operator sign (also in the form of English word).
The code will perform the calculation and give the result if your input is what it
expects.

The code is very long and messy. Refactor it according to what you have learned about
code simplicity and efficiency.
"""


def calculator():
    print('Welcome to this calculator!')
    print('It can add and subtract whole numbers from zero to five')
    a = input('Please choose your first number (zero to five): ').lower()
    b = input('What do you want to do? sum or rest: ').lower()
    c = input('Please choose your second number (zero to five): ').lower()

#Eliminé todo ese código porque no tenía sentido.
    values = {'zero': 0,
              'one': 1,
              'two': 2,
              'three': 3,
              'four': 4,
              'five': 5,
              }

    if 0 <= values[a] <= 5 and 0 <= values[c] <= 5:
        if b == 'sum' or b == "+":
            print(values[a] + values[c])
        if b == 'rest'or b == "-":
            print(values[a] - values[c])
    else:
        print("I am not able to answer this question. Check your input.")

    print("Thanks for using this calculator, goodbye :)")
calculator()
