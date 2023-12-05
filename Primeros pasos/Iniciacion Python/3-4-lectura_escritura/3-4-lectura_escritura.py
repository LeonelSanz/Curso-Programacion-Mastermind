
SALIDA = "SALIR"
LISTA = "LISTA"


def preguntar_producto_usuario():
    return input("Introduce un producto [{} para ver productos disponibles, {} para salir] ".format(LISTA, SALIDA))


def guardar_archivo(archivo):
    nombre_fichero = input("Como quieres que se llame el archivo? ")
    with open(nombre_fichero + ".txt", "w") as mi_archivo:
        mi_archivo.write("\n".join(archivo))


def main():
    lista_compra = []
    lista_permitidos = ["Pan", "Pollo", "Pipas", "Leche"]

    input_usuario = preguntar_producto_usuario()

    while input_usuario != SALIDA:
        if input_usuario == LISTA:
            print("Productos disponibles: {}".format(lista_permitidos))
            input_usuario = preguntar_producto_usuario()

        else:
            if input_usuario in lista_permitidos:
                lista_compra.append(input_usuario)
                print("\n".join(lista_compra))
                input_usuario = preguntar_producto_usuario()
            else:
                print("Ese producto no esta disponible")
                input_usuario = preguntar_producto_usuario()

    guardar_archivo(lista_compra)


if __name__ == "__main__":
    main()
