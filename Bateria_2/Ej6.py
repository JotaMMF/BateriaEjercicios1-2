"""
Escribir un programa que almacene las 
asignaturas de un curso (por ejemplo 
Matemáticas, Física, Química, Historia y Lengua) 
como claves de un diccionario, 
pregunte al usuario la nota que ha sacado en 
cada asignatura y actualice cada entrada del 
diccionario. 

Imprimir el diccionario al final del programa.
"""

dict_asignaturas = {
    "Matemáticas" : 0,
    "Física" : 0,
    "Química" : 0,
    "Historia" : 0,
    "Lengua" : 0,
}

for asignatura in dict_asignaturas:
    nota_asignatura = input("Introduzca la nota de %s: " 
                            % asignatura)
    dict_asignaturas[asignatura] = nota_asignatura

for n in dict_asignaturas:
    print ("%s: %s " % (n,int(dict_asignaturas[n])))