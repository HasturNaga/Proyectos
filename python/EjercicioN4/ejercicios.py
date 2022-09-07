print('Rango de 0 a 10 con numeros divisibles entre 3')
for i in range(11):
    if i % 3 == 0:
        print(i)

rango = range(2, 7)
for i in rango:
    print(i)

print('Rango con valores de inicio = 3, fin = 10 incremento = 2')
for i in range(3, 11, 2):
    print(i)

# Definimos una tupla

cocina = ('Cuchara', 'Cuchillo', 'Tenedor')
print(len(cocina))

print(cocina[0])

print(cocina[-1])

print(cocina[0:1])

verduras = ('papa',) # siempre debe llevar la coma para que sea una tupla

for cocinar in cocina:
    print(cocinar, end= ' ')

