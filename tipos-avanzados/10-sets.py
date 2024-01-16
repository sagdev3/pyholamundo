primer = {1, 1, 2, 2, 3, 4}
segundo = [3, 4, 5]
segundo = set(segundo)
print(primer | segundo)  # Union
print(primer & segundo)  # Intercepcion
print(primer - segundo)  # Diferencia
print(primer ^ segundo)  # Diferencia Simetrica

if 5 in segundo:
    print('Hola Mundo')
