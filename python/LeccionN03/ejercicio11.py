# Ejercicio 11: Agenda telefonica
# Hacer un programa un simule una agenda de contatos.
# Crear un diccionario donde la clava sea el nombre del usuario
# y el valor sea e telefono. e programa tendra el siguiente menu de opciones:
#       1. Nuevo contacto
#       2. Borrar contacto
#       3. Ver contcto existentes
#       4. Salir
agenda = {}
while True:
    print('\.:MENU:.')
    print('1. Nuevo contacto')
    print('2. Borrar contacto')
    print('3. Ver contacto existentes')
    print('4. Salir')
    opcion = int(input('Digite el nombre del contacto: '))
    if opcion == 1:
        nombre = input('Digite el nombre del contacto: ')
        telefono = input('Digite el numero de telefono: ')
        if nombre not in agenda:
            agenda[nombre] = telefono
            print('Contacto agregado exitosamente...!!')
        else:
            print('Este nombre de contacto ya exite')
    elif opcion == 2:
        nombre = input('Cual es el nombre del contacto: ')
        if nombre in agenda:
            del (agenda[nombre])
            print('Se ha eliminado el cantacto requerido.')
        else:
            print('Este contacto no existe en la agenda.')
    elif opcion == 3:
        print('Agenda de conctatos.')
        for clave, valor in agenda.items():
            print(f'Nombre: {clave}, Telefono: {valor}')
    elif opcion == 4:
        print('Grcias por utilizar su agenda de contacto')
        break
    else:
        print('Se equivoco de opcion de menu.')
