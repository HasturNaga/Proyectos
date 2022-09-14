
a = float(input("Digite un numero: "))
b = float(input("Digite un numero: "))
c = float(input("Digite un numero: "))
resultado = (a ** 3 * (b ** 2 - 2 * a * c)) / (2*b)
print(f'El resultado es: {resultado}')

# Ejercicio 3
mes = int(input("Digite un mes del año (1 - 12): "))
estacion = None
if mes == 1 or mes == 2 or mes == 3:
    estacion = "Verano"
if mes == 4 or mes == 5 or mes == 6:
    estacion = "Otono"
if mes == 7 or mes == 8 or mes == 9:
    estacion = "Invierno"
if mes == 10 or mes == 11 or mes == 12:
    estacion = "Primavera"
else:
    estacion = "Error no hay numero para este mes."
print(f'Para el mes {mes} la estacion es: {estacion}')

# Ejercicio 4
edad = int(input("Digite su edad: "))
mensaje = None
if 0 <= edad < 10:
    mensaje = "La infancia es increible y bella"
elif 10 <= edad < 20:
    mensaje = "Tienes muchoe cambios, mucho que estudiar."
elif 20 <= edad < 30:
    mensaje = "Amor y comienza el trabajo"
else:
    mensaje = "Error, etapa de vida no reconocida"
print(f'Tu edad es: {edad}, {mensaje}')

# Ejercicio 5
calificacion = int(input("Digite una calificacion entre 0 y 10"))
if 9 <= calificacion <= 10:
    print("A")
elif 8 <= calificacion <= 9:
    print("B")
elif 7 <= calificacion <= 8:
    print("C")
elif 6 <= calificacion <= 7:
    print("D")
elif 0 <= calificacion <= 6:
    print("F")
else:
    print("Valor incorrecto...")