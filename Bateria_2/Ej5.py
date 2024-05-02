"""
Remplazar cada letra de una frase dada por el usuario por la posición que le corresponde
en el abecedario y mostrar el nuevo string en pantalla. Por ejemplo:
Hola → H(8) o(15) l(12) a(1)
"""
import string

palabra = "Espantapajaros"

abecedario = list(string.ascii_lowercase)

for letra in palabra.lower():
    print (letra+"(" + str(abecedario.index(letra)) +")", 
           end="")