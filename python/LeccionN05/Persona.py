class Persona:

    def __init__(self, nombre, apellido, edad, dni, *args, **kwargs):
        self.nombre = nombre
        self.apellido = apellido
        self._dni = dni
        self.edad = edad
        self.args = args
        self.kwargs = kwargs

    def mostrar_detalle(self):
        print(f'La clase Persona tiene los siguientess datos: {self.nombre} {self.apellido} {self._dni} {self.edad}, la direccion es: {self.args}, los datos importates son: {self.kwargs}')

persona1 = Persona('Ariel', 'Betancud', 23456789, 40)
# print(persona1.nombre)
# print(persona1.apellido)
# print(persona1.edad)
print(f'El objeto1 de la clase persona: {persona1.nombre} {persona1.apellido} Su edad es: {persona1.edad}')
persona2 = Persona('Osvaldo', 'Giordanini', 23456789, 45)
print(f'El objeto2 de la clase persona: {persona2.nombre} {persona2.apellido} Su edad es: {persona2.edad}')

persona1.nombre = 'Liliana'
persona1.apellido = 'Bucella'
persona1.edad = 40
print(f'El objeto1 modificdo de la clase persona: {persona1.nombre} {persona1.apellido} Su edad es: {persona1.edad}')

persona1.mostrar_detalle()
persona2.mostrar_detalle()

persona1.telefono = '444455529'
print(f'Este es el telefono de: {persona1.nombre} {persona1.telefono}')

persona3 = Persona('Rogelio', 'Romero', 22, 'Telefono', '2614445557', 'Calle Lopez', 823, 'Manzana', 77, 'Casa', 18, Altura=1.83, Peso=105, CFavorito='Azul', Auto='Citroen', Modelo=2021)
persona3.mostrar_detalle()
print(persona3._dni) #mal uso del encapsulamiento
# persona3.__nombre es la unica forma de encapsularlo. La variable tambien debe levar los guiones bajos
















