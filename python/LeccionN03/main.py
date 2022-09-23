nombres = ['Naty','Osvaldo','Lily','Ariel']
print(nombres)
print(nombres[0])
print(nombres[1])
print(nombres[3])
print(nombres[-1])
print(nombres[-2])
print(nombres)
print(nombres[0:2])
print(nombres[ :3])
print(nombres[1: ])
nombres[2] = 'Liliana'
nombres[0] = 'Natalia'
print(nombres)

for nombre in nombres:
    print(nombre)
else:
    print('Se terminaron los nombres de la lista')

print(len (nombres))

nombres.append('Marcelo')
nombres.append([1, 2, 3])
nombres.append(True)
nombres.append(10.45)
nombres.append([4, 5])
nombres.append(7)
print(nombres)
nombres.insert(1,'Alberto')
print(nombres)
nombres.insert(3,'Debora')
print(nombres)

nombres.remove('Alberto')
print(nombres)

nombres.pop()

del nombres[2]
print(nombres)

nombres.clear()
print(nombres)

del nombres
# print(nombres)

# Definir tuplas
cocina = ('Cuchara','Cuchilo','Tenedor')
print(cocina)

print(len(cocina))

print(cocina[0])
print(cocina[-1])
print(cocina[0:1])

verduras = ('papa',)

for cocinar in cocina:
    print(cocinar, end= ' ')

cocinar = 'plato'
print(cocinar)

cocinaLista = list(cocina)
cocinaLista[0] = 'Plato'
cocina = tuple(cocinaLista)
print('\n', cocina)

# Ejercicio de tupla
tupla = (13, 1, 8, 3, 2, 5, 8)

lista = []

for elemento in tupla:
    if elemento < 5:
        lista.append(elemento)
print(lista)

# Tipo set
planetas = {'Martes', 'Venus', 'Jupiter'}
print(len(planetas))

print('Martes' in planetas)

planetas.add('Tierra')
print(planetas)

planetas.remove('Jupiter')
print(planetas)
planetas.discard('Tierra')
print(planetas)

# Limpiar set
planetas.clear()
print(planetas)

# Eliminar set o conjunto
del planetas

# Diccionario
diccionario = {
    'IDE': 'Integrated Development Enviroment',
    'POO': 'Programacion Orientada a Objetos',
    'SABD': 'Sistema de Administracion de Base de Datos'
}
print(len(diccionario))
print(diccionario)

print(diccionario['IDE'])

print(diccionario.get('POO'))
print(diccionario.get('SABD'))

# Modificacion de elementos
diccionario['IDE'] = 'Entorno de Desarrollo Integrado'
print(diccionario)

# Como recorrer los elementos
for termino in diccionario:
    print(termino)

# Necesitamos una funcion para recorrer un diccionario
for termino, valor in diccionario.items():
    print(termino, valor)

# Otras maneras de acceder a un diccionario
for termino in diccionario.keys():
    print(termino)

for valor in diccionario.values():
    print(valor)

# Comprobar la existencia de algun elemento
print('IDE' in diccionario)

# Agregar un elemento
diccionario['PK'] = 'Primary key'
print(diccionario)

# Eliminar un elemento
diccionario.pop('SABD')
print(diccionario)

# Vaciar un diccionario
diccionario.clear()
print(diccionario)

# Eliminar un diccionario
del diccionario

# lista = Ariel, Liliana, Natalia, Osvaldo
# Colecciones en Python

nombres = ['Naty', 'Osvaldo', 'Lily', 'Ariel']
print(nombres)
print(nombres[0:2])
print(nombres[ :3])
print(nombres[1: ])
nombres[2]
nombres[0]
print(nombres)
# Iterar una lista
for nombre in nombres:
    print(nombre)
else:
    print('Se acabaron los elmentos de la lista.')

# Preguntamos cuantos elementos tiene la lista
print(len(nombres))

# Agregamos un elemento
nombres.append('Marcelo')
nombres.append([1, 2, 3])
nombres.append(True)
nombres.append(10.45)
nombres.append(7)
print(nombres)

# Inserte un elemnto en un indice espsifico
nombres.insert(1, 'Alberto')
print(nombres)
nombres.insert(3, 'Debora')
print(nombres)

# Concatenar lista

lista1 = [1, 2, 3, 1]
lista2 = [4, 5, 6, 1]
lista3 = lista1 + lista2
print(lista3)

lista3.extend([7, 8, 9, 1])
print(lista3)

print(lista3.index(5))

# Como saber si hay cuantos valores repetidos hay dentro en una lista
print(lista3.count(1))

# Para poner al reves una lista
lista3.reverse()
print(lista3)

# Para que una lista se multiplique repitiendo sus elementos
lista3 = lista3 * 2
print(lista3)

# Metodos de ordenamiento
lista3.sort()
print(lista3)
lista3.sort(reverse=True)
print(lista3)

# Repaso de tuplas
tupla = (4, 'Hola', 6.78, [1, 2, 78], 4, 'Hola')
print(tupla)
print(4 in tupla)
print(4 not in tupla)

# Repaso de set o conjunto
conjunto2 = set()
conjunto1 = {'bye'}
conjunto2.add(7)
conjunto2.add('Hola')
print(conjunto2)
conjunto1.add('hola')
print(conjunto1)
print(3 not in conjunto1)

# Como hacer la igualdad de dos conjuntos
print(conjunto2 == conjunto1)

# Operaciones en conjuntos
conjunto3 = conjunto1 | conjunto2
print(conjunto3)

conjunto3 = conjunto1 & conjunto2
print(conjunto3)

conjunto3 = conjunto1 - conjunto2
print(conjunto3)

conjunto3 = conjunto2 - conjunto1
print(conjunto3)


conjunto3 = conjunto1 ^ conjunto2
print(conjunto3)

conjunto3 = conjunto1 | conjunto2
print(conjunto2.issubset(conjunto3))
print(conjunto2.issubset(conjunto3))
print(conjunto3.issubset(conjunto1))
print(conjunto3.issubset(conjunto2))

print(conjunto3.issuperset(conjunto1))
print(conjunto3.issuperset(conjunto2))
print(conjunto2.issuperset(conjunto3))

# Como saber si ambos conjuntos son disconexo.
print(conjunto1.isdisjoint(conjunto2))

# Convertir un conjunto totalmente en inmutable
conjunto1 = frozenset

# Repso de diccionario
diccionarioNuevo = {'Azul': 'Blue', 'Rojo': 'Red', 'Verde': 'Green', 'Amarillo': 'Yellow'}
print(diccionarioNuevo)

# Como eliminar un diccionario
del (diccionarioNuevo['Azul'])


# Los diccionarios pueden guardar diferent tipos de datos
diccionario2 = {'Ariel': {'Edad': 40, 'Altura': 1.83}, 'Osvaldo': [45, 1.85], 'Natalia': [335, 1.67]}
print(diccionario2)

seleccionArgentina = {
    10: {'Nombre': 'Lionel Messi', 'Edad': 35, 'Altura': 1.70, 'Precio': '50 millones', 'Posicion': 'Extremo Derecho'},
    11: {'Nombre': 'Angel Di Maria', 'Edad': 34, 'Altura': 1.80, 'Precio': '12 millones', 'Posicion': 'Extremo Derecho'},
    21: {'Nombre': 'Paulo Dybala', 'Edad': 28, 'Altura': 1.77, 'Precio': '35 millones', 'Posicion': 'Media Punta'},
    19: {'Nombre': 'Nicolas Otamendi', 'Edad': 34, 'Altura': 1.83, 'Precio': '3.5 millones', 'Posicion': 'Defensa Central'},
    1:  {'Nombre': 'Franco Armani', 'Edad': 35, 'Altura': 1.89, 'Precio': '3.5 millones', 'Posicion': 'Portero'},
    26: {'Nombre': 'Nahuel Molina', 'Edad': 24, 'Altura': 1.80, 'Precio': '20 millones', 'Posicion': 'Lateral Derecho'},
    7: {'Nombre': 'Rodrigo De Paul', 'Edad': 28, 'Altura': 1.75, 'Precio': '40 millones', 'Posicion': 'Mediocentro'},
    14: {'Nombre': 'Exequiel Palacio', 'Edad': 23, 'Altura': 1.72, 'Precio': '15 millones', 'Posicion': 'Mediocentro'},
    12: {'Nombre': 'Joaquin Corea', 'Edad': 28, 'Altura': 1.81, 'Precio': '23 millones', 'Posicion': 'Mediapunta'}
}

for llave, valor in seleccionArgentina.items():
    print(llave, valor)
    print('Tenemos cargado en el diccionario la cantidad de jugadores:', end=' ')
print(len(seleccionArgentina))

# [Pilas usando listas
pila = [1, 2, 3]

# Agregar los elementos a la pila por el final
pila.append(4)
pila.append(5)
print(pila)

# Sacamos el elemento desde el final
elementoBorrado = pila.pop
print(f'Sacamos el elmento {elementoBorrado}')
print(f'La pila ahora quedo asi: {pila}')

# Colas con listas
cola = ['Ariel', 'Osvaldo', 'Liliana', 'Pilar']

# Agregamos elementos al final de la cola
cola.append('Natalia')
cola.append('Jose')
print(cola)

# Sacamos elementos de la cola
seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

for i in seleccionArgentina:
    print(f'{i} -> {seleccionArgentina}')
