# Ejercicio 5: factorial de un numero positivo.
# Hacer un programa para calcular de faactoril de un numero positivo.
numero = int(input("Digite un numero: "))
while numero < 0:
    print("Error -> El numero tiene que ser positivo.")
    numero = int(input("Digite un numero: "))
factorial = 1
for i in range(1, numero + 1):
    factorial *= i
print(f"\nEl factorial del numero {numero} positivo ingresado es: {factorial}")
