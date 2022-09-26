# Ejercicio funciones 1: crear una funcion para sumar los valores recibidos de tipo
# numericos, utilizando argumentos variables *args como parametro de la funcion
# y agregar como resultado la suma de todos os valores pasados
# como argumntos.
def sumar_valores(*args):
    resultado = 0
    for valor in args:
        resultado += valor
    return resultado

# Llamamos a la funcion
print(sumar_valores(3, 5, 9, 2, 1))