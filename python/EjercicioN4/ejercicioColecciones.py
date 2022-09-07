# Ejercicio 1: Eliminar duplicados de una lista
# Escriba un programa donde tenga una lista y que a continuacion
# eliminar los elementos repetidos, por ultimo mostrar a una lista

# Creamos una lista
lista = [1, 2, 3, "Ariel", 7, 7, 3, "Alberto", 1, "Ariel", 2, "Alberto"]
# conjunto = set(lista)
# lista = list(conjunto)
lista = list(set(lista))
print(lista)