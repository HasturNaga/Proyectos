# Ejercicio 3: insertar elementos y ordenarlos.
# Pedir numeros y meterlos en una lista, cuando el usuario.
# introduca un numero 0, nuestro programa dejara de insertar.
# Por ultimo, mostrar los numeeros ordenados de menor a mayor.
lista = []
salir = False
while not salir:
    numero = int(input('Digite un numero'))
    if numero == 0:
        salir = True
    else:
        lista.append(numero)
lista.sort()
print(f'\nLista ordenada: \n{lista}')
