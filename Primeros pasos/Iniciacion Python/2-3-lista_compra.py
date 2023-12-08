
lista_compra = []

while True:
    compra = input("Que deseas comprar? ([Q] para salir) ")
    if compra == "Q":
        break
    elif compra in lista_compra:
        print("{} ya esta en la lista".format(compra))
    else:
        if input("Seguro que quieres añadir \"{}\"? [S/N] ".format(compra)) == "S":
            lista_compra.append(compra)
            print("{} añadido".format(compra))

print("La lista de la compra es:\n"
      "{}".format(lista_compra))