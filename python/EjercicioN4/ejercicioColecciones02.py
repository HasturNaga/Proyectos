# Ejercicio 2: Operaciones de conjunto con listas
# Escriba un programa que tenga 2 listas y que a continuacion
# cree las siguientes listas(en la que no debe haber repeticiones)
# 1 Lista de palabras que aparecen en las listas
# 2 Lista de palabras que aparecen en la primera lista, pero no en la segunda
# 3 Lista de palabras que aparecen en la segunda lista, pero no en la primera
# 4 Lista de palabras que aparacen en ambas listas

lista1 = ["Ricardo", "Elena", "Angeles", "Alfonso", "Noemi"]
lista2 = ["Ricardo", "Elena", "Angeles", "Malena", "Federico"]

conjunto1 = set(lista1)
conjunto2 = set(lista2)

operacion1 = list(conjunto1 | conjunto2)
operacion2 = list(conjunto1 - conjunto2)
operacion3 = list(conjunto2 - conjunto1)
operacion4 = list(conjunto1 & conjunto2)

print(f"Lista de palabras que aparecen en las listas: {operacion1}")
print(f"Lista de palabras que aparecen en la primera lista, pero no en la segunda: {operacion2}")
print(f"Lista de palabras que aparecen en la segunda lista, pero no en la primera: {operacion3}")
print(f"Lista de palabras que aparacen en ambas listas: {operacion4}")