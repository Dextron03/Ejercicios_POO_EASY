# 2)Crear una clase Contacto. Esta clase deberá tener los atributos "nombre, apellidos, teléfono y dirección". También deberá tener una función "SetContacto"  con los parámetros que permita cambiar el valor de los atributos. También tendrá una función "Saludar", que escribirá en pantalla "Hola, soy " seguido de sus datos. Crear también una clase llamada ProbarContacto. Esta clase deberá contener sólo la función principal, que creará dos objetos de tipo Contacto, les asignará los datos del contacto y les pedirá que saluden.

class Contacto:
  def __init__(self, nombre, apellidos, telefono, direccion):
    self.nombre = nombre
    self.apellido = apellidos
    self.telefono = telefono
    self.direccion = direccion
  
  def set_contacto(self) -> str:
    self.nombre : str = input("Nombre del contacto: ")
    self.apellido : str = input("Apellido del contacto: ")
    self.telefono : str = input("Numero de telefono del contacto: ")
    self.direccion : str = input("Direccion del contacto: \n")
  
  def saludar(self):
    print(f"\nHola soy {self.nombre}.\nApellido: {self.apellido}.\nNumero TEL: {self.telefono}.\nDireccion: {self.direccion}.\n")

    
class ProbarContacto(Contacto):
  def __init__(self, nombre, apellidos, telefono, direccion):
    super().__init__(nombre, apellidos, telefono, direccion)
  
  def createcontac(self):
    first_contact = Contacto("", "", "", "")
    second_contact = Contacto("", "", "", "")
    
    first_contact.set_contacto()
    print(f"\nSegundo contacto:")
    second_contact.set_contacto()
    
    first_contact.saludar()
    second_contact.saludar()

prueba = ProbarContacto("", "", "", "")

prueba.createcontac()