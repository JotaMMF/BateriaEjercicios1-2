"""
Imaginemos que en nuestra tienda 
hay un carné por puntos y que 
alguien debe pagar el
precio_final_de_compra. 

Si tienes menos de 100 puntos realizaremos un 
descuento del10%. 
Si es mayor a 100 y menor a 
150 aplicamos un 12%. 
Si tienes 150 un 15% y sino, el
resto de los casos de más de 150, un 20%.
"""

def carne_descuentos(puntos, precio_Init):
    descuento = 0
    if puntos < 100:
        descuento = 10
    elif puntos in range(101,150):
        descuento = 12
    elif puntos == 150:
        descuento = 15
    elif puntos > 150:
        descuento = 20
    
    return precio_Init - (precio_Init * (descuento /100))

puntosUser = float(input ("Indique su núm de puntos: "))
precioInicial = float(input ("Indique el total a pagar: "))

print(carne_descuentos(puntosUser,precioInicial))