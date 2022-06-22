
num = int(input("Digite un numero en el rango de 1 a 3"))
numTexto = ''
if num == 1:
    numTexto = "Numero 1"
elif num == 2:
    numTexto = "Numero 2"
elif num == 3:
    numTexto = "Numero 3"
else:
    numTexto = "Has ingresado un numero fuera de rango"
print(f'El numero ingresado es: {num} - {numTexto}')

# Opeador ternario
condicion = True
print("Condicion Verdadera") if condicion else print ("Condicion Falsa")

