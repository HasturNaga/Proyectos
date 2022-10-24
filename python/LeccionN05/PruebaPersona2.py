from Funcion import Funcion

print('Creacion de Objetos'.center(50, '-'))
if __name__ == '__main__':
    persona5 = Funcion('Lionel', 'Messi', 35)
    persona5.motrar_detalles()

    print(__name__)

print('Eliminacion de Objetos'.center(50, '-'))
del persona5