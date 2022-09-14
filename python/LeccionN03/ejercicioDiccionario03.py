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

personajes = []
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

# Dada la siguiente tupla
tupla = (13, 1, 8, 3, 2, 5, 8)
# e imprimir por consola [1, 3, 2]

lista = []
# Filtramos los elementos menores a 5 de la tupla
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


