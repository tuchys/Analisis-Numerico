# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 07:35:28 2021

@author: josem
"""


import matplotlib.pyplot as plt

n = 10
n = n
division = 0
multiplicacion = 0
adicion = 0
total = 0

suma =  (1/3)*((2*n) +1) * (n*(n + 1 )/2)

for i in range(1, n):
    
    multiplicacion += 4
    division += 2
    adicion += 2


    
print("El resultado es: ", suma)
print("numero de multiplicaciones hechas: ", multiplicacion)
print("numero de divisiones hechas: ", division)
print("numero de sumas hechas: ", adicion)
total = multiplicacion+division+adicion
print("El total de operaciones fue: ", total )

plt.plot(suma)
plt.show()

