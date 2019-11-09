numeros = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
resultados_posibles = {-5:'minus five', -4:'minus four', -3:'minus three', -2:'minus two', -1:'minus one', 0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten'}

def calculadora_chafa():
    print('Welcome to this calculator!')
    print('It can add and subtract whole numbers from zero to five')
    a = input('Please choose your first number (zero to five): ')
    b = input('What do you want to do? plus or minus: ')
    c = input('Please choose your second number (zero to five): ')

    if b == 'plus':
        resultado = numeros[a] + numeros[c]
    elif b == 'minus':
        resultado = numeros[a] - numeros[c]
    else:
        resultado = print('I am not able to answer this question. Check your input.')
    return resultado

print(calculadora_chafa())
print("Thanks for using this calculator, goodbye :)")