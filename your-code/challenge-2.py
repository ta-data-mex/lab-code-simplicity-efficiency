#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 16:08:26 2019

@author: rodolfopardo
"""
#GEnerador de alfanumerico random
#La idea fue sintetizar todo en una funcion que solo ejecute de acuerdo al largo de palabras que seleccione usuario
#Se realiza en una funcion 
#Se importan las librerias random y string
#While con un try y except para evitar errores

import random
import string

def random_string(*args):
    letters = string.ascii_lowercase + string.digits
    str_final = ''.join(random.choice(letters) for i in range(size))
    return str_final


count = 5
while count > 0:
       try:    
           size = int(input("De cuantos caracteres quiere generar un string aleatorio: "))
           print(random_string(size))
           x = input("¿Desea salir?: (responda si o no)")
           if x == "si" or x == 'yes':
                print("Ok, que tengas un buen dia")
                break;
           else:
             print("Sigamos generando strings!")
       except:
            print("Por favor, ingrese un numero, no letra. Tiene %s chances" % count)
            count = count - 1


