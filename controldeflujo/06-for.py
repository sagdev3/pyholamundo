buscar = 10
for numero in range(15):
    print(numero)
    if numero == buscar:
        print('encontrado', buscar)
        break
else:
    print('no se encontro')
