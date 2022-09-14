# Repaso de set o conjunto
conjunto2 = set()
conjunto1 = {'bye',}
conjunto2.add(7)
conjunto2.add('Hola')
print(conjunto2)
conjunto1.add('hola')
print(conjunto1)
print(3 not in conjunto1)

# Como saber la igualdad de dos conjuntos
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

# Como saber si ambos conjuntos son disconexos, esto es si comparten algun elemnto en comun.
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

# Seguimos mostrando como reecorrer un diccionario con el ciclo for
for i in seleccionArgentina:
    print(f'{i} -> {seleccionArgentina[i]}')

