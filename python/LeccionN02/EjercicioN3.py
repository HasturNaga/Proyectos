
# Primeros numeros

n = int(input("\n Ingrese la cantidad de numeros a sumar:"))
suma = 0
for i in range(n):
    print(i)
    suma += i
print(f"La suma es: {suma}")

# Salario
salario = 0
sumaSalario = 0

for i in range(5):
    horasTrabajada = float(input(f"Ingrese la cantidad de horas trabajadas del empleado {i + 1}: "))
    tarifacA.S,FAHora = float(input("Ingrese el precio por hora de este empleado"))
    salario = horasTrabajada * tarifaHora
    print(f"El salario del mpleado {i} es de${salario}")
    sumaSalario += salario

print(f"La suma de todos los salarios es de: {sumaSalario}")

# Factorial
fact = 1
num = int(input("Ingrese el numero para calcular el fatorial: "))
while num <= 0:
    print("El numero ingresado es menor o igual a cero, vuelva a ingresarlo: ")
    num = int(input("Ingrese el numero para calcular el fatorial: "))

for i in range(num):
    fact += fact * i
    print(f"El factorial del numero ingresado es: {fact}")

# Año bisiesto
anio = int(input("Ingrese un año"))
if (anio %4 == 0 and anio % 100 != 0) or anio % 400 == 0:
    print("El año ", anio, " es bisiesto")
else:
    print("El año ", anio, " no es bisiesto")

# Numeros positivos, negativos y neutros

i = 1
varPos = 0
varNeg = 0
varNeu = 0

while i <= 10:
    varNum = int(input(f"Ingrese el numero {i}"))
    if varNum == 0:
        varNeu = varNeu + 1
    else:
        if varNum < 0:
            varNeg = varNeg + 1
        else:
            varPos = varPos + 1
    i += 1
print(f"{varNeu} numeros son neutros.")
print(f"{varNeg} numeros son negativos.")
print(f"{varPos} son numeros positivos.")

# Calificaion
suma = 0
promedio = 0
baja = 0
calificacion = 999999
i = 1

for i in range(10):
    calificacion = float(input("Ingrese una calificacion"))
    suma = suma + calificacion
    if calificacion < baja:
        baja = calificacion
promedio = suma / 10

print(f"La nota mas baja es {baja}")
print(f"El promedio del curso es {promedio}")

