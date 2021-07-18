# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 17:07:46 2021

@author: maril
"""

'''Uso de While Infinito'''
c=1

while True:
    print(c)
    break
#while validación
vocal= input("Ingrese vocal: ")
while vocal not in ('a','e','i', 'o', 'u'):
    if vocal == '.':
        break
    vocal= input("Vocal: ")
print("Su vocal o punto es: {}" .format(vocal)) 