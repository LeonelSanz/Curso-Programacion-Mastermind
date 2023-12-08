
sistema = input("IOS o Android? \n")

movil_ideal = "Ninguno"

if sistema == "Android":
    dinero = input("Tienes dinero? (S/N) ")

    if dinero == "N":
        movil_ideal = "Android chino 100$"

    else:
        camara = input("Te importa la camara? (S/N) ")
        if camara == "S":
            movil_ideal = "Google Pixel Supercamara"
        else:
            movil_ideal = "Android calidad-precio"

elif sistema == "IOS":
    dinero = input("Tienes dinero? (S/N) ")

    if dinero == "S":
        movil_ideal = "Iphone Ultra Pro Max"
    else:
        movil_ideal = "Iphone de segunda mano"

print("Tu movil ideal es " + movil_ideal)