#Me parece que hacerlo con string de números en vez de números es bastante limitado, por lo que lo cambié
#a hacerlo a números. Eso te permite usar la calculadora con todos los números positivos. Además, lo hice en español.
#Lo mejor es usar una función

def calculadora():
    print('Hola, raza! Bienvenido a esta calculadora.')
    print('Esta calculadora puede sumar y restar números positivos.')
    primer_factor = int(input("No seas malito, escribe aquí el primer número que quieres sumar: "))
    segundo_factor = int(input("Ya estás! Ahora escribe el segundo número que quieres sumar: "))
    suma_resta = input("Con que no pusiste atención en la primaria, eh? Naaah, es broma. "
                       "¿Quieres sumar o restar? \n(Recuerda que suma se escribe '+'; resta '-'): ")
    if primer_factor >= 0 & segundo_factor >= 0:
        if suma_resta == "+":
            print(f'Esa está fácil. El resultado de {primer_factor} más {segundo_factor} es {primer_factor + segundo_factor}')
        elif suma_resta == "-":
            print(f'Compa, el resultado de restar {primer_factor} menos {segundo_factor} es {primer_factor - segundo_factor}')
    else:
        print("No soy ROBOTINA, compa. Tienes que escoger números enteros a sumar o restar y usar el operador '+' o '-'")
        return calculadora()

    contador = input("Quieres usarla de nuevo? Es gratis! (Escribe 'si' o 'no'): ")
    if contador == "si":
        calculadora()
    elif contador == "no":
        print("Que tengas buen día, compa!")
    else:
        print("Sólo puedes escribir 'si' o 'no'. Intentalo de nuevo")

calculadora()