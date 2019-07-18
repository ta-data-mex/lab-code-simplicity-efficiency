print('Welcome to this calculator!\nIt can add and subtract any numbers')
a = input('Please choose your first number between one and five: ')
b = input('What do you want to do? (plus or minus): ')
c = input('Please choose your second number between one and five: ')
diccionario = {'zero': 0, 'one': 1, 'two': 2, 'tree': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10}
oper = ['plus', 'minus']
if a not in diccionario or c not in diccionario:
    print("I am not able to answer this question. Check your input.")
else:
    if b in oper:
        if b == 'plus':
            d = diccionario[a] + diccionario[c]
            listOfKeys = [key  for (key, value) in diccionario.items() if value == d]
            print(f'{a} {b} {c} equals {listOfKeys[0]}')
        elif b == 'minus':
            d = diccionario[a] - diccionario[c]
            listOfKeys = [key  for (key, value) in diccionario.items() if value == d]
            print(f'{a} {b} {c} equals {listOfKeys[0]}')
    else:
        print("I am not able to answer this question. Check your input.")