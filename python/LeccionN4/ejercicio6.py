# Ejercicio 6: tablas de multiplicar
# Hacer un programa que pida un numero por teclado y guarded
# En una ista su tabla de multiplicarhata el 10. Por ejemplo:
# Si digita el 5 la lista tendra: 5,10,15,20,25,30,35,40,45,50
numero = int(input("Digite un numero: "))
lista = []
for i in range(1, 11):
    lista.append(i*numero)
print(f'\nTabla de multiplicar del {numero}: \n {lista}')

for indice, i in enumerate(lista):
    print(f'{numero} x {i} = {lista[indice]}')
    