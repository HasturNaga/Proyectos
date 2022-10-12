# Ejercicio 5: convertidor de temperaturas.
# Realizar dos funciones para conveertir de grados celcius
# a fahrenheit y visversa.
# Investigar las formulas
def celsius_fahrenheit(celsius):
    return  celsius * 9 / 5 + 32

def fahrenheit_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

celsius = float(input('Digite el valor de celsius: '))
resultado = celsius_fahrenheit(celsius)
print(f'{celsius} C a F -> {resultado:.2f}')

fahrenheit = float(input('Digite el  valor de fahrenheit'))
resultado = fahrenheit_celsius(fahrenheit)
print(f'{fahrenheit} F a C -> {resultado:.2f}')
