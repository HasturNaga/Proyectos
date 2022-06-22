contador = 0

while contador < 78:
    print("Ejecutando e ciclo while")
    contador += 1
else:
    print("Fin del ciclo while")

# Contador de increnmento
maximo = 5
contador = 0
while contador <= maximo:
    print(contador)
    contador += 1

# Contador de decremento
minimo = 1
contador = 5
while contador >= minimo:
    print(contador)
    contador -= 1

# Ciclo for
cadena = "Hello"
for i in cadena:
    print(i)
else:
    print("Fin del ciclo for")

# Break
for i in "Alemania":
    if i == "a":
        print(f"Letra encontrada: {i}")
        break
    else:
        print("Fin del ciclo for")

# Continue
for i in range(6):
    if i % 2 == 0:
        print(f"Valor: {i}")

for i in range(6):
    if i % 2 != 0:
        continue
    print(f"Valor: {i}")