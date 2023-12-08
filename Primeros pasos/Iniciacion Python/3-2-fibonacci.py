from time import sleep

def sumar_uno(a):
    a += 1
    print(a)
    if a != 100:
        sumar_uno(a)


def medir_largos(iterable, *args, sumar_todo=False):
    if args:
        largos = [len(iterable)]
        for a in args:
            largos.append(len(a))
        if sumar_todo:
            largos = sum(largos)
        return largos
    return len(iterable)


def fibonacci(a):
    if a <= 1:
        return a
    else:
        return fibonacci(a-1) + fibonacci(a-2)


def fibonacci_s_recursion(posicion):
    actual = 0
    siguiente = 1
    for x in range(posicion + 1):
        temporal = actual
        actual = siguiente
        siguiente = siguiente + temporal
    return temporal


def potencia(n, base=2):
    resultado = n
    for a in range(1, base):
        resultado *= n
    return resultado


def main():
    # for f in range(8):
    #     print(fibonacci_s_recursion(f))
    print(potencia(5, 3))


if __name__ == "__main__":
    main()