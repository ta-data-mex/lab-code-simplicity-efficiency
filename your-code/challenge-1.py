"""
This is a dumb calculator that can add and subtract whole numbers from zero to five.
When you run the code, you are prompted to enter two numbers (in the form of English
word instead of number) and the operator sign (also in the form of English word).
The code will perform the calculation and give the result if your input is what it
expects.

The code is very long and messy. Refactor it according to what you have learned about
code simplicity and efficiency.
"""

#An input always gives us a string, but it does not mean we need to keep working with strings
def calc():
    print('Welcome to this calculator!\nIt can add and subtract whole numbers from 0 to 5.')
    # changed the input messages to ask for a digit that will be converted in to an int.
    a = int(input('Please choose your first number (0 to 5): '))
    b = input('What do you want to do? + or -: ') #asked for + or - for less probability of input error (less characters)
    c = int(input('Please choose your second number (0 to 5): '))
   # try and except to manage input errors
   # two probabilities of operations instead of accounting for all possibilities
    try:
        if b == '+':
            print(f'{a} + {c} = {a+c}')
        elif b == '-':
            print(f'{a} - {c} = {a-c}')
    except:
        print('I am not able to answer this question. Check your input.')
    print("Thanks for using this calculator, goodbye :)")

calc()

