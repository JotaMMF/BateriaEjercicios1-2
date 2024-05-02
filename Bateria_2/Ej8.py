cesta_dict = {}
art_nombre = ""
total= 0

while True:
    art_nombre = input('Introduzca el NOMBRE del artículo '\
                    '(END para terminar): ')
    
    if art_nombre.upper() == "END":
        break

    art_precio = float(input("Introduzca el PRECIO "\
                             "del artículo: "))

    cesta_dict[art_nombre] = art_precio


for article in cesta_dict:
    print("%s : %s €" % (article, cesta_dict[article]))
    total += cesta_dict[article]
print ("Total:", total, "€")
