class Vehiculo:
    '''
    Definir una clase padre llamada Vehiculo y dos clases hijas llamadas Auto y Bicicleta, las cuales heredan de la clase padre Vehiculo. La clase padre debe tener los siguientes atributos y metodos:
    Vehiculo (clase padre)
    -Atributos (color, ruedas)
    -Metodos (__init__(color, ruedas) y __str__())

    Auto (clase hija de Vehiculo)
    - Atributos (velocidad km/hr)
    - Metodos (__init__(color, ruedas, velocidad) y __str__())

    Bicicleta (clase hija de Vehiculo)
    - Atrebutos (tipo(tipo(urbana, montaña, etc.)))
    - Metodos (__init__(color, ruedas, tipo) y __str__())

    Crear un objeto de cada clase.
    '''
class Vehiculo:

    def __init__(self, color, ruedas):
        self._color = color
        self._ruedas = ruedas

    def __str__(self):
        return f'Color: {self._color}, Ruedas: {self._ruedas}'

class Auto(Vehiculo):

    def __init__(self, color, ruedas, velocidad):
        super().__init__(self, color, ruedas, velocidad)
        self._color = color
        self._ruedas = ruedas
        self._velocidad = velocidad

    def __str__(self):
        return f'Color: {self._color}, Ruedas: {self._ruedas}'

class Bicicleta(Vehiculo):

    def __init__(self, color, ruedas, tipo):
        super().__init__(self, color, ruedas, tipo)
        self._color = color
        self._ruedas = ruedas
        self._tipo = tipo

    def __str__(self):
        return f'Color: {self._color}, Ruedas: {self._ruedas}'


