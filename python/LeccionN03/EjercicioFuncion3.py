# Como parametro de la funcion y regresar como resultado
# la multiplicacion de todos los valores pasados como agumentos.

def multiplicar_valores(*numeros):
    resultado = 1
    for numero in numeros:
        resultado *= numero
    return resultado

print(multiplicar_valores(3, 5, 15, 4))