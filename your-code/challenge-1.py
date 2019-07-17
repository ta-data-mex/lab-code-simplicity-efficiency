#Computadora update

#Se utiliza una funcion para ejecutar todas las operaciones
#Recibe también operaciones 
#Soporta el ingreso de strings 


def calculadora(operacion, n1, n2):
  if operacion == "1":
    return n1 + n2
    #print(n1+n2)
  elif operacion == "2":
    #print(n1-n2)
    return n1 - n2
  elif operacion == "3":
    #print(n1*n2)
    return n1*n2
  elif operacion == "4":
    #print(n1/n2)
    return n1/n2
  else:
      print("Ha ingresado una operación que esta calculadora no reconoce")

print('Bienvenido a la calculadora\n Solo tienes que ingresar dos numeros')

intentos = 4
while intentos > 0:
    try:
         a = int(input('Ingresa el primer valor:'))
         c = int(input('Ingresa el segundo valor:'))
         b = input('Elija 1 si quiere sumar, 2 si quiere restar, 3 si quiere multiplicar y 4 si quiere dividir: ')
         print("El resultado es: %d" % calculadora(b,a,c))
         x = input("¿Desea salir? (responda con si o no)")
         if x == "si" or x == 'yes':
             print("Ok, que tengas un buen dia")
             break;
         else:
             print("Continuamos...")
    except:
         intentos = intentos - 1
         print("¡Tienes que ingresar un numero!. Vuelve a intentarlo. Tienes %i chances más" % intentos)





