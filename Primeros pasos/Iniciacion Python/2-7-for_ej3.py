
numero = int(input("Elije un numero "))

for num in range(1, 11):
    if num % 2 == 0:
        print("{} x {} = {}".format(num, numero, num * numero))