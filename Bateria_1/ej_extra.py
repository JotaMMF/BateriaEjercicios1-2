"""
Definir una funcion que,
dada una lista, retorne
los elementos únicos de 
la lista:

Ej:
[1,2,2,3,4,4,5] -> [1,2,3,4,5]

NO USAR set() o UNIQUE()
"""
list1 = [1,2,2,3,4,4,5,4,4,4,3,3,2,2,7,7,7,7,7,5,4,8,8,8,9,9,6,5,8,9]

def unicos_lista(lista):
    lista_unicos = []

    for num_unico in lista:
        for num_repetido in lista:
            if num_unico == num_repetido and num_unico not in lista_unicos:
                lista_unicos.append(num_unico)
    
    return lista_unicos

print (unicos_lista(list1))