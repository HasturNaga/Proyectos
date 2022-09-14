# Bucles while y for

i = 1
varNumero = int(input("Ingrese un numero para sacar el factorial: "))
while varNumero <= 0:
    print("Numero incorrect")
    varNumero = int(input("Ingrese un numero para sacar el factorial: "))
else:
    while i <= varNumero:
        varNumero = varNumero * i
        i = i + 1
        print(varNumero)
