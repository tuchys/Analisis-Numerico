
import numpy as np
import math
e = math.e

# INGRESO
fx = lambda x: (x**3)-(x*2)-5
    #((668)/x)*(1-e**(-0.146843*x))-40
    #(x**3)-(x*2)-5
    #(math.cos(x)**2)-x**2
              #x*math.sin(x)-1
              #(x**3)-(2*x**2)+(4/3)*x-(8/27)
              

a = 2
b = 3
tolerancia = 10e-16


# PROCEDIMIENTO
tabla = []
tramo = abs(b-a)
fa = fx(a)
fb = fx(b)

while not(tramo<=tolerancia):
    
    c = b - fb*(a-b)/(fa-fb)
    fc = fx(c)
    cambio = np.sign(fa)*np.sign(fc)
    tabla.append([a,c,b,fa,fc,fb,tramo])
    
    
    if cambio>0:
        tramo = abs(c-a)
        a = c
        fa = fc
        print('La raiz es : ' ,c)
    else:
        tramo = abs(b-c)
        b = c
        fb = fc
        print('La raiz es : ' ,c)
    

tabla = np.array(tabla)
ntabla = len(tabla)
# SALIDA
for i in range(0,ntabla,1):
    print('iteración:  ',i)
    
    
print('raiz:  ',c)
print('error: ',tramo)