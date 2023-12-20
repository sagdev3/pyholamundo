def suma(*numeros):
    resultado = 0
    for numeros in numeros:
        resultado += numeros
    print(resultado)


suma(2, 3, 5)
suma(2, 3, 5, 8)
suma(2, 3, 5, 30, 5)
