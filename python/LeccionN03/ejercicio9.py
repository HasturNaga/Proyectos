# Ejercicio 9: mostrar una frase sin espacios y contar su longitud
# Hacer un prrograma donde el usuario ingrese una frase, se le
# devolverar la misma frase pero sin espacios en blanco, y
# adeemas un contador de cuantos caracteres tiene la frase
# (sin contar los espacios en blanco)
# Ejemplo:      frase = vivir por siempre en paz
#               frase final = vivirporsipreenpaz
#               N° de caracteres: 20 + un espacio
frase1 = input("Digite una frase: ")
frase2 = " "
for i in frase1:
    if i != " ":
        frase2 += i
frase1 = frase2
print(f'\nFrase final: {frase1}')
print(f'N° de caracteres: {len(frase1)}')