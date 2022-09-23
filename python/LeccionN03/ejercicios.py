import math
# Ejercicio 1: iterar un rango de 0 a 10 numeros divisibles entre 3
# Ejemplo de ejecucion: 0, 3, 6, 9
print('Rango de 0 a 10 con numeros divisibles entre 3')
for i in range(11):
    if i % 3 == 0:
        print(i)

# Ejercicio 2: crear un rango de numros de 2 a 6 e imprimalos
# Ejemplo de ejeccion: 2, 3, 4, 5, 6
print('Rango con valores de inicio = 2 y fin = 6')
rango = range(2, 7)
for i in rango:
    print(i)

print('Rango con valores de inicio = 3, fin = 10 incremento = 2')
for i in range(3, 11, 2):
    print(i)

# Ejercicio 3: crear un rango de 3 a 10 pero con incrmento de 2 en 2, en lugar de 1 en 1
# Ejemplo de ejecucion = 3, 5, 7, 9

print('Rango con valores de inicio = 3, fin fin = 10, incremeno = 2')
for i in range(3, 11, 2):
    print(i)

# Definimos una tupla

cocina = ('Cuchara', 'Cuchillo', 'Tenedor')
print(len(cocina))

print(cocina[0])

print(cocina[-1])

print(cocina[0:1])

verduras = ('papa',)# siempre debe llevar la coma para que sea una tupla

for cocinar in cocina:
    print(cocinar, end= ' ')

cocinaLista = list(cocina)
cocinaLista[0] = 'Plato'
cocina = tuple(cocinaLista)
print('\n', cocina)

del cocina

# Definimos la lista
# Filtramos los lementos menores a 5 de la tupla
tupla = (1, 2, 3, 4, 5)
lista = []
for elemento in tupla:
    if elemento < 5:
        lista.append(elemento)
print(lista)

# Ejercicio de matematica
# Para sacar la raiz cuadrada de un numero positivo
numero = int(input('Digite un numero positivo'))
while numero < 0:
    print('Error -> Deberia ser un numero positivo')
    numero = int(input('Digite un numero positivo: '))
print(f'\nSu raiz cuadrada es: {math.sqrt(numero):.2f}')
