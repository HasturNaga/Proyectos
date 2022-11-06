
class Vehiculo:

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f'Color: {self.color}, Ruedas: {self.ruedas}'

class Auto(Vehiculo):

    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return super().__str__()+' ,Velocidad (km/hr): '+str(self.velocidad)

class Bicicleta(Vehiculo):

    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__()+' ,Tipo: '+self.tipo

vehiculo1 = Vehiculo('azul', 3)
print(vehiculo1)

auto1 = Auto('Verde', 4, 150)
print(auto1)

bicicleta1 = Bicicleta('Negro', 2, 'Carrera')
print(bicicleta1)