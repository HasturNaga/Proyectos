# Ejercicio 2: crear una funcion para sumar los valores recibidos de tipo
# numericos, utilizando argumentos variables *aegs como paramtro de la
# funciony agregar como resultado la suma d todos lo valores pasado
# como argumentos.
# Definimos una funcion
def sumar_valor(*args):
    resultado = 0
    for valor in args:
        resultado += valor
    return resultado

print(sumar_valor(3, 5, 9))