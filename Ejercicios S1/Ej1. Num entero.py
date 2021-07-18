# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 17:00:24 2021

@author: maril
"""

x= int(input("Ingresa un número entero: "))
if x<0:
    x=0
    print("Negativo cambiado a cero")
elif x==0:
    print("Cero")
elif x==1:
    print("Uno")
else:
    print("Ninguna opción")
print("Ok") if type(x)==int else print("-") 
