numeros = [2, 4, 1, 45, 75, 22]

# numeros.sort(reverse=True)

numerosOrdenados = sorted(numeros, reverse=True)
print(numerosOrdenados)

usuarios = [["Chanchito", 4], ["Felipe", 1], ["Pulga", 5]]


usuarios.sort(key=lambda el: el[1])
print(usuarios)
