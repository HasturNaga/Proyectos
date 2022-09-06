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
print(nombres)

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
tupla = ('13', '1', '8', '3', '2', '5', '8')

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
    'IDE':'Integrated Development Enviroment',
    'POO':'Programacion Orientada a Objetos',
    'SABD':'Sistema de Administracion de Base de Datos'
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
diccionario.pop()
print(diccionario)

#Vaciar un diccionario
diccionario.clear()
print(diccionario)

# Eliminar un diccionario
del diccionario

# Concatenaqr lista
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


