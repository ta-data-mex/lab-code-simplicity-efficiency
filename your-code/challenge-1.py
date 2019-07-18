"""
This is a dumb calculator that can add and subtract whole numbers from zero to five.
When you run the code, you are prompted to enter two numbers (in the form of English
word instead of number) and the operator sign (also in the form of English word).
The code will perform the calculation and give the result if your input is what it
expects.
"""
def dumb_calculator():
    print('Welcome to this calculator!')
    print('It can add and subtract whole numbers from zero to five')
    a = input('Please choose your first number (zero to five): ')
    b = input('What do you want to do? plus or minus: ')
    c = input('Please choose your second number (zero to five): ')

    num_list=['zero','one', 'two','three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    num_lett={i:num_list[i] for i in range(len(num_list))}
    lett_num={num_list[i]:i for i in range(len(num_list))}

    if (a not in num_list[:6]) or (c not in num_list[:6]):
        b = 'Hm'
    if b == 'plus':
        ans = lett_num[a]+lett_num[c]
    elif b == 'minus':
        ans = lett_num[a]-lett_num[c]
    else: 
        return ("I am not able to answer this question. Check your input.")

    if ans < 0:
        return(f"{a} {b} {c} equals negative {num_lett[abs(ans)]}")
    elif ans >= 0:
        return(f"{a} {b} {c} equals {num_lett[(ans)]}")

dumb_calculator()
