"""
This is a dumb calculator that can add and subtract whole numbers from zero to five.
When you run the code, you are prompted to enter two numbers (in the form of English
word instead of number) and the operator sign (also in the form of English word).
The code will perform the calculation and give the result if your input is what it
expects.

The code is very long and messy. Refactor it according to what you have learned about
code simplicity and efficiency.
"""

print('Welcome to this calculator!')
print('It can add and subtract whole numbers from zero to five')
a = input('Please choose your first number (zero to five): ')
b = input('What do you want to do? plus or minus: ')
c = input('Please choose your second number (zero to five): ')

nums = {'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5}
vals = {'0':'zero','1':'one','2':'two','3':'three','4':'four','5':'five'}
ops = {'plus':'+','minus':'-'}
check_num = lambda x: True if x in nums else False
check_op = lambda x: True if x in ops else False

def operation(n1,op,n2):
    if (check_num(n1) and check_num(n2) and check_op(op)):
        if op == 'plus':
            res = nums[n1] + nums[n2]
            print('%s %s %s equals %s' % (n1,op,n2,vals[str(res)]))
        else:
            res = nums[n1] - nums[n2]
            print('%s %s %s equals negative %s' % (n1,op,n2,vals[str(res*-1)]))
    else:
        print("I am not able to answer this question. Check your input.")

operation(a,b,c)
print("Thanks for using this calculator, goodbye :)")