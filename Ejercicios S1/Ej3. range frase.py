# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 17:08:12 2021

@author: maril
"""

# For range(v) - range(vi,vf) - range(vi,vf,inc)
frase= input("Ingrese frase: ")
for indice in range(len(frase)):
    print(indice,'=',frase[indice])

# For in cadena - in(tupla) - in[lista]
cvoc = 0
for car in frase:
    if car in ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U"):
        if car in ["A", "E", "I", "O", "U"]:
            continue
        else:
            cvoc= cvoc+1
print("cantidad vocales: {}" .format(cvoc))

# Comprehension-[var for var in datos condicion]
#[car for car in['a', 'e', 'i', 'o', 'u'] if car not in ('a', 'i', 'o')] 