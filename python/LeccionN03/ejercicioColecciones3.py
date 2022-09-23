import math
# Ejercicio 3: Agregar personajes a una lista
# Escriba un programa deonde cree una lista con los siguiente personajes del señor de los anillos
# Nombre: Aragon
# Clase: Guerrero
# Raza: Dunadan del norte

# Nombre: Gandalf
# Clase: Mago
# Raza: Istar

# Nombre: Legolas
# Clase: Arquero
# Raza: Elfo Sindar

personajes = [] # Creamos lista vacia.
# Creamos diccionarios
P = {'Nombre': 'Aragon', 'Clase': 'Guerrero', 'Raza': 'Dunadan del Norte'}
personajes.append(P)
P = {'Nombre': 'Gandalf', 'Clase': 'Mago', 'Raza': 'Istar'}
personajes.append(P)
P = {'Nombre': 'Legolas', 'Clase': 'Arquero', 'Raza': 'Elfo Sindar'}
personajes.append(P)
P = {'Nombre': 'Sauron', 'Clase': 'Nigromante', 'Raza': 'Ainur y Maiar'}
personajes.append(P)
P = {'Nombre': 'Saruman', 'Clase': 'Mago', 'Raza': 'Istari y Ainur'}
personajes.append(P)
P = {'Nombre': 'Gimli', 'Clase': 'Gerrero', 'Raza': 'Enano'}
personajes.append(P)
print(personajes)
