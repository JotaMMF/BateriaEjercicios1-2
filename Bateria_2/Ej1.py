"""
Crear una función donde se implemente el siguiente 
algoritmo que permite calcular si un
año es bisiesto:
1. Si el año es uniformemente divisible por 4, 
vaya al paso 2. De lo contrario, vaya al paso
5.

2. Si el año es uniformemente divisible por 100, 
vaya al paso 3. De lo contrario, vaya al
paso 4.

3. Si el año es uniformemente divisible por 400, 
vaya al paso 4. De lo contrario, vaya al
paso 5.

4. El año es un año bisiesto (tiene 366 días).
5. El año no es un año bisiesto (tiene 365 días).
Probar con varios años que la función funciona de manera correcta.
"""
def annobisiesto(anno):
    bisiesto = False
    if anno%4 == 0:
        if anno%100 != 0:
            bisiesto = not bisiesto
        else:
            if anno %400 ==0:
                bisiesto = not bisiesto 
    return bisiesto

print(annobisiesto(2024))