punto1 = {"x": 19, "y": 'Hola'}
punto2 = {"y": 15}


nuevoPunto = {**punto1, "lala": 'Hola mundo', **punto2, "z": 'Mundo'}
print(nuevoPunto)
