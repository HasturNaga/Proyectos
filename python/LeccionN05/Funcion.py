class Funcion:

    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def motrar_detalles(self):
        print(f'Los datos a mostrar son los siguientes: {self._nombre} {self._apellido} {self._edad}')

    @property
    def nombre(self):
        print('Estamos utilizando el metodo get nombre')
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        print('Estamos utilizando el metodo set nombre')
        self._nombre = nombre

    @property
    def apellido(self):
        print('Estamos utilizando el metodo get apellido')
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        print('Estamos utilizando el metodo set apellido')
        self._apellido = apellido

    @property
    def edad(self):
        print('Estamos utilizando el metodo get edad')
        return self._edad

    @edad.setter
    def edad(self, edad):
        print('Estamos utilizando el metodo set edad')
        self._edad = edad

    def __del__(self):
        print(f'Funcion: {self._nombre} {self._apellido} {self._edad}')

persona1 = Funcion('Ariel', 'Betancud', 22)
print(persona1.nombre, persona1.apellido, persona1.edad)
persona1.nombre = 'Juan Pedro'
print(persona1)
print(persona1.motrar_detalles())
# Atributo read_only la edad porque no tine el metodo set.

persona2 = Funcion('Octavio', 'Rodriguez', 24)
print(persona2.nombre)
print(persona2.apellido)
print(persona2.edad)
persona2.nombre = 'Luciano'
persona2.apellido = 'Martinez'
persona2.edad = 23
print(persona2.motrar_detalles())

persona3 = Funcion('Andres', 'Ramires', 54)
print(persona2.nombre)
print(persona2.apellido)
print(persona2.edad)
persona3.nombre = 'Facundo'
persona3.apellido = 'Martinez'
persona3.edad = 29
print(persona3.motrar_detalles())

persona4 = Funcion('Ricardo', 'Modon', 35)
print(persona2.nombre)
print(persona2.apellido)
print(persona2.edad)
persona4.nombre = 'Pedro'
persona4.apellido = 'Mansilla'
persona4.edad = 45
print(persona4.motrar_detalles())
