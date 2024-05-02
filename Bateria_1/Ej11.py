"""
Definir un histograma procedimiento() que tome una lista 
de números enteros e imprima
un histograma en la pantalla. Ejemplo: 
procedimiento([4, 9, 7]) debería imprimir lo
siguiente:
****
*********
*******
"""
from Ej10 import generar_n_caracteres

def procedimiento(lista):
    printeo = ""
    for numero in lista:
        printeo += generar_n_caracteres(numero)

    return printeo
    
print (procedimiento([1,20,15])) 