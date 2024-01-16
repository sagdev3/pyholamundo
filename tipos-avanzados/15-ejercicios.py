from pprint import pprint

string = 'Hola mundo este es mi string'


def quita_espacio(texto):
    return [char for char in texto if char != " "]


def cuenta_caracteres(lista):
    chars_dict = {}
    for char in lista:
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    return chars_dict


def ordena(dict):
    return sorted(
        dict.items(),
        key=lambda key: key[1],
        reverse=True
    )


def mayores_tuplas(lista):
    maximo = lista[0][1]
    respuestas = {}
    for orden in lista:
        if maximo > orden[1]:
            break
        respuestas[orden[0]] = orden[1]
    return respuestas


def crea_mensaje(diccionario):
    mensaje = "Los que mas se repiten son: \n"
    for key, valor in diccionario.items():
        mensaje += f"- {key} con {valor} repeticiones \n"
    return mensaje


sin_espacio = quita_espacio(string)
contados = cuenta_caracteres(sin_espacio)
ordenados = ordena(contados)
mayores = mayores_tuplas(ordenados)
mensaje = crea_mensaje(mayores)
pprint(mensaje)
