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