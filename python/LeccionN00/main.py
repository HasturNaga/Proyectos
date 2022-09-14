
print('Hola Mundo')

miVariable = 3
print(miVariable)
miVariable = "Hola a todos los estudiantes de la tecnicatura"
print(miVariable)
miVariable = 3.5
print(miVariable)
x = 10
y = 2
z = x + y
print(id(x))
#
print(id(y))
print(id(z))

a = "Hola alumnos"
print(type(a))
#Tipos de datos.
x = 10
print(x)
print(type(x))
x = 14.5
print(x)
print(type(x))
x = "Hola Mundo"
print(x)
print(type(x))
x = True
print(x)
print(type(x))
x = False
print(x)
print(type(x))

# ejercicion1
dia = input('¿Como estuvo tu dia hoy (1 al 10)?')
print("Mi dia estuvo de ", dia)
# ejercicion2
titulo = input("Ingrese el titulo del libro: ")
autor = input("Ingrese el autor del libro: ")

#EjercicioN3
miGrupoFavoritoEs = "AudioSlave"
caracteristicas = "La mejor banda del mundo"
print("Mi grupo favorito es ", miGrupoFavoritoEs, caracteristicas)

numero1 = "8"
numero2 = "7"
print(int(numero1) + int(numero2))

miBooleano = 1 > 2
print(miBooleano)

if(miBooleano):
    print("La variale es Verdadera")
else:
    print("La variale es Falso")

resultado = input("Ingrese un valor: ")
print(resultado)

varNumUno = int(input("Ingrese el primer numero: "))
varNumDos = int(input("Ingrese el segundo numero: "))

varResultado = varNumUno + varNumDos
print("El resultado de la suma es: ", varResultado)

# Operadores10


operadorA = 8
operadorB = 5
suma = operadorA + operadorB

print("El resultado de la suma es: ", suma)
print(f"El resultado de la suma es: {suma}")

resta = operadorA - operadorB
print("El resultado de la resta es: ", resta)
print(f"El resultado de la resta es: {resta}")

multiplicacion = operadorA * operadorB
print("El resultado de la resta es: ", multiplicacion)
print(f"El resultado de la resta es: {multiplicacion}")

division = operadorA / operadorB
print("El resultado de la division es: ", division)
print(f"El resultado de la division es: {division}")

division = operadorA // operadorB
print("El resultado de la division es: ", division)
print(f"El resultado de la division (int) es: {division}")

modulo = operadorA % operadorB
print("El resultado de la modulo es: ", modulo)
print(f"El resultado de la modulo es: {modulo}")

exponente = operadorA ** operadorB
print("El resultado de la exponente es: ", exponente)
print(f"El resultado de la exponente es: {exponente}")

# Area y perimetro
alto = int(input("Ingrese el alto del rectangulo: "))
ancho = int(input("Ingrese el ancho del rectangulo: "))
area = alto * ancho
perimetro = (alto + ancho) * 2
print("El area del rectangulo es: ", area)
print("El perimero del rectangulo es: ", perimetro)

# Operadores de asignacion
miVariable1 = 10
print(miVariable1)

miVariable1 = miVariable1 + 1
print(miVariable1)

miVariable1 += 1
print(miVariable1)

miVariable1 += 2
print(miVariable1)

miVariable1 -= 2
print(miVariable1)

miVariable1 *= 3
print(miVariable1)

miVariable1 /= 1
print(miVariable1)

# Operadores de comparacion
a = 4
b = 6

resultado = a == b
print(resultado)

resultado = a != b
print(resultado)

resultado = a > b
print(resultado)

resultado = a < b
print(resultado)

resultado = a <= b
print(resultado)

resultado = a >= b
print(resultado)

# Continuacion de operadores

c = false
d = false
resultado = c and d
print(resultado)

resultado  = c or d
print(resultado)

resultado = not a
print(resultado)

valor = int(input("Digite un numero entre 0 y 5: "))
valorMinimo = 0
valorMaximo = 5
dentroRango = (valor >= valorMinimo and valor <= valorMaximo)
if dentroRango:
    print(f'El valor {valor} esta dentro de rango')
else:
    print(f'El valor {valor} no esta dentro de rango')

# Operadores logicos
vacaciones = False
diaDescanso = False
if not (vacaciones or diaDescanso):
    print('Tiene trabajo que hacer.')
else:
    print('Puede asistir al juego.')
#  Rango entre 20 y 30
edad = int(input("Ingrese la edad dela persona"))
if (20 <= edad < 30) or (edad >= 30 and edad < 40):
    print("Estas dentro del rango de los (20) a los (30) años")
else:
    print("No estas dentro del rango de los (20) a los (30) años")

# Numero mayor
varUno = int(input("Ingrese el primer valor: "))
varDos = int(input("Ingrese el segundo valor: "))

if varUno < varDos:
    print("El primer valor es menor que el segundo.")
else:
    print("El segundo valor no es menor que el segundo.")

# Datos de un libro
print("Digite los siguiente datos del libro.")
nombre = input("Digite el nombre del libro: ")
id = int(input("Digit el ID del libro: "))
precio = float(input("Digite el precio del libro: "))
envioGratuito = input("Indicar se el libro es gratuito (True/False):")
if envioGratuito == "True":
    envioGratuito = True
elif envioGratuito == "False":
    envioGratuito = False
else:
     envioGratuito = "El valor es incorrecto, debe escribir True/false"
print(f'''
        Nombre: {nombre}
        Id: {id}
        Precio: {precio}
        Envio Gratuito: {envioGratuito}
''')

