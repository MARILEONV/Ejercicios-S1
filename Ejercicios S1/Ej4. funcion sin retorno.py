# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 17:08:32 2021

@author: maril
"""

"""Funciones sin retorno"""
def vocales(frase):
    for car in frase:
        if car in ('a', 'e', 'i', 'o', 'u'):
            print(car)

"""Llamada a función"""
oracion= input("Ingrese la oración: ")
vocales(oracion.lower())

"""Función con retorno de valor"""
def promedio(notas):
    summ=0
    for n in notas:
        summ+=n
    return summ/len(notas)

#Llamada a función
listanotas= [2,4,6,8,10]
prom= promedio(listanotas)
print("Promedio: {}={} " .format(listanotas,prom))