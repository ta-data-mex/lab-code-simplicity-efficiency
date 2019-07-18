#Debido a que un diccionario con los valores a eligir era muy limitado, decidí que los input permitieran cualquiera número entero
#Además agregué la multiplicación y la división a las opciones de la calculadora
#A pesar de ser un códio mucho más corto, aún considero que se puede hacer más pequeño
def calculator():
      
    print('Welcome to this calculator! \n It can add, subtract, multiply and divide \n')
    first_number = int(input('Choose your first number (just integers): '))
    operation = input('Which operation do you want to do? \n (+, -, *, / ) ')
    second_number = int(input('Choose your second number (just integers): '))
    if (first_number >= 0) & (second_number >= 0):
        if operation == '+':
            print('The result is: ', first_number + second_number)
        elif operation == '-':
            print('The result is: ', first_number - second_number)
        elif operation == '*':
            print('The result is: ', first_number * second_number) 
        elif operation == '/':
            if second_number > 0:
                print('The result is: ', first_number / second_number)
            else:
                print('Divide any number between 0 is not posible. \n Try again.')
    else:
        print('That is not an integer. Please just add integers.')
        return calculator()
    
    cont_using = input('Do you want to continue using the calculator? \n (yes or no) ')
    if cont_using == 'yes':
        return calculator()
    elif cont_using == 'no':
        print('Goodbye.') 
        
calculator()