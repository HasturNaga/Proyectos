# Ejercicio 7: juego adivina el numero
# Realizar un juego para adivinar un numero. Para ello se debe
# generar un numero aleatorio entre 1 y 100, y luego ir pidiendo
# numeros indicando "es mayor" o "es menor" segun ea mayor o menor
# con respecto a N. El proceso termina cuando el usuario acierta
# y alli se debe mostra el numero d intento.
import random
aleatorio = random.randint(0, 100)
contador = 0
while True:
    numero = int(input('Digite un numero: '))
    contador += 1
    if numero > aleatorio:
        print("\tNo es el numero, digite unnumero menor.")
    elif numero < aleatorio:
        print("\tNo es el numero, digite un numero mayor.")
    else:
        print(f"felicitaciones, acacbas de adivinar el numero {aleatorio}")
print(f"\nNumero d intentos: {contador}")

