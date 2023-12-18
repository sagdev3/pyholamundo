numero1 = ''
numero2 = ''
operacion = ''

while True:
    numero1 = input('Ingrese el primer numero: ')
    if numero1.lower() == 'salir':
        break
    if numero1 != '':
        numero1 = float(numero1)
    else:
        print('Debe ingresar un numero valido')

    operacion = input('Ingresa un signo de operacion ')
    if operacion == '':
        print('El campo no debe encontrarse vacio')
    if operacion != '+' and operacion != '-' and operacion != '*' and operacion != '/':
        print('Debe ingresar operaciones validas')

    numero2 = input('Ingrese el primer numero: ')
    if numero2.lower() == 'salir':
        break
    if numero2 != '':
        numero2 = float(numero2)
    elif numero2 == '':
        print('Debe ingresar un numero valido')

    if operacion == '+':
        print(float(numero1) + float(numero2))
    elif operacion == '-':
        print(float(numero1) - float(numero2))
    elif operacion == '*':
        print(float(numero1) * float(numero2))
    elif operacion == '/':
        print(float(numero1) / float(numero2))
    elif operacion.lower() == 'salir':
        break
    else:
        print('Operacion no valida')
        break
