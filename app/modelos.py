from enum import Enum, auto

class TipoEntrada(Enum):
   BEBE = auto()
   NINO = auto()
   ADULTO = auto()
   JUBILADO = auto()


class Entrada:

    def __init__(self, edad: int):
        if edad <= 2:
          self.tipo = TipoEntrada.BEBE
          self.precio = 0
        elif edad <= 14:
          self.tipo = TipoEntrada.NINO
          self.precio = 14
        elif edad <= 65:
          self.tipo = TipoEntrada.ADULTO
          self.precio = 23
        else:                      
          self.tipo = TipoEntrada.JUBILADO
          self.precio = 18

class Grupo_Entrada:
   
    def __init__(self):
        self.total = 0
        self.num_entradas = 0

    def add_entrada(self, edad):
        nueva_entrada = Entrada(edad)
        self.num_entradas += 1
        self.total += nueva_entrada.precio

    def add_entradas(self, edades):
        for edad in edades:
            self.add_entrada(edad)

'''
      en funcion de la edad crear una entrada, incrementar el contador de entrada.
      Con el precio de la entrada nueva incrementar el total
      Tiene que pasar el test

'''