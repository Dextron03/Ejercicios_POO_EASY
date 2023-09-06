#3)Crear tres clases ClaseA, ClaseB, ClaseC que ClaseB herede de ClaseA y ClaseC herede de ClaseB. Definir un constructor a cada clase que muestre un mensaje. Luego definir un objeto de la clase ClaseC.

class A:
  pass

class B(A):
  print("Estoy en B")

class C(B):
  print("Estoy en C")

vaina = A()

