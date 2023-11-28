import random

random_num = random.randint(1, 10)
num = int(input("Elegi un numero del 1 al 10 "))

if num == random_num:
    print("Enhorabuena, ganaste, el numero era {}".format(random_num))

if num > 10:
    print("Te has pasado un poco, era entre 1 y 10")

if num < 1:
    print("Te has quedado corto, era entre 1 y 10")

if num != random_num:
    print("Fallaste, el numero era {}".format(random_num))