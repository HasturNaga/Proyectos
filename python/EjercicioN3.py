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

