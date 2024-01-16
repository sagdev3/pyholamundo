punto = {"x": 25, "y": 50}
print(punto)
print(punto["x"])

punto["z"] = 45
# print(punto, punto["lala"])
if "lala" in punto:
    print("Encontre lala", punto["lala"])
else:
    print('No hay lala')


print(punto.get("x"))
print(punto.get('lala', 97))

del punto["x"]
del (punto["y"])
print(punto)
punto["x"] = 25

for valor in punto:
    print(valor, punto[valor])

for valor in punto.items():
    print(valor)

for llave, valor in punto.items():
    print(llave, valor)


usuarios = [
    {"id": 1, "nombre": "Chanchito"},
    {"id": 2, "nombre": "Santi"},
    {"id": 3, "nombre": "Javier"},
    {"id": 6, "nombre": "Felipe"},
]

for usuario in usuarios:
    print(usuario["nombre"])
