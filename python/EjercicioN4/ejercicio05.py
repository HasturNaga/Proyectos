# Ejercicio 2: modificar los elementos de una lista
# Llenar una lista con los numeros del  al 10, luego modificar los
# elementos de la lista multiplicandolos por un valor ingresado por el usuario

lista = list(range(1, 11))
print('Lista original')
for i in lista:
    print(i, end='-')

valor = int(input('\nDigite un valor a multiplicar '))
# Multiplicamos todos los lmentos de la lista
for indice, i in enumerate(lista):
    lista[indice] *= valor

print(f'Lista final con los elementos mmultiplicados por {valor}')
for i in lista:
    print(i, end='-')