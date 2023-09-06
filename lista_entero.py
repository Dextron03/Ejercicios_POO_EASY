# 5)Cargar una lista de 10 enteros, luego mostrarlos por pantalla a cada elemento separados por una coma. Usando funciones.

class ListaEnteros:
  def __init__(self, lista : list) -> str:
    self.lista = lista
    
  def tranformlist(self):
    integers_cadena = ",".join(map(str, self.lista))
    return integers_cadena
  
lista = ListaEnteros([1,2,3,4,5,6,7,8,9,10])
print(lista.tranformlist())