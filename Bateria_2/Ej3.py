"""
Debemos crear una función para calcular la tarifa 
a pagar por los usuarios de un polideportivo.

La función recibe la tarifa anual total (100%), la edad del usuario y su
situación laboral. 
La tarifa final se calcula en base al criterio siguiente:

1. Criterio 1: Si es mayor de edad y está trabajando -> 
Paga el 100%

2. Criterio 2: Si es menor de edad y está trabajando -> 
Paga el 95%

3. Criterio 3: Si es mayor de edad y no está trabajando -> 
Paga el 75%

4. Criterio 4: Si es menor de edad y no está trabajando -> 
Paga el 50%

Probar diferentes configuraciones de usuario y tarifas y ver como afectan estos a la tarifa
final.
"""

def calcTarifa(tarif_anual, edad, sit_lab):
    #Criterios
    mayor_Edad = True
    if edad < 18:
        mayor_Edad = not mayor_Edad
    
    trabajando = True
    if sit_lab.lower() == "no":
        trabajando = not trabajando
    
    if mayor_Edad and not trabajando:
        tarifa_percent = 75
    elif not mayor_Edad and not trabajando:
        tarifa_percent = 50
    elif not mayor_Edad and trabajando:
        tarifa_percent = 95    

    return tarif_anual - (tarif_anual * (tarifa_percent/100))

print(calcTarifa(200, 26, "si"))