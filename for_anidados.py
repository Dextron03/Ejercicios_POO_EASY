# 4)Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado.

class ComparatorList:
  def __init__(self, list_one : list, list_two : list) -> list:
    self.list_one = list_one
    self.list_two = list_two
  
  def superposicion(self):
    repite : int = 0
    for x in self.list_one:
      for i in self.list_two:
        if i == x:
          print(f"{x} (͠≖ ͜ʖ͠≖)👌 {i}")
          repite +=1
        else:
          print(f"{x} (ㆆ_ㆆ) {i}")
    if repite > 0:
      print(repite)
      repite = True
      print(repite)
    else:
      print(repite)
      repite = False
      print(repite)

prueba = ComparatorList(["Hola", "Perro", "Juan"], ["Braily", "Carro", "Hola"])
prueba.superposicion()