# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 17:09:56 2021

@author: maril
"""

"""Funciones matemáticas"""
import math

num1, num2, num, men= 12.572,15.4,4,'1234'
print(math.ceil(num1),'\t', math.floor(num1) )
print(round(num1,1),'\t', type(num), '\t', type(men))

#Funciones de cadenas
mensaje= 'Hola'+'mundo'+'Python'
men1= mensaje.split()
men2=''.join(men1)
print(mensaje[0], mensaje[0:4], men1, men2)
print(mensaje.find("mundo"), mensaje.lower())

#Funciones de fecha
from datetime import datetime, timedelta, date
hoy, fdia= datetime.now(), date.today()
futuro= hoy+timedelta(days=30)
dif, aa, mm, dd= futuro-hoy,hoy.year, hoy.month, hoy.day
fecha= date(aa,mm,dd+2)
print(hoy, fdia, futuro, dif, fecha) 