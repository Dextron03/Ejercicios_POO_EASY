#1) Crear una clase Persona que tenga como atributos "cédula, nombre, apellido y la edad (definir las propiedades para poder acceder a dichos atributos)". Definir como responsabilidad una función para mostrar ó imprimir. Crear una segunda clase Profesor que herede de la clase Persona. Añadir un atributo sueldo ( y su propiedad) y en la función para imprimir su sueldo. Definir un objeto de la clase Persona y llamar a sus funciones y propiedades. También crear un objeto de la clase Profesor y llamar a sus funciones y propiedades.

class Person:
  def __init__(self, cedula, nombre, apellido, edad):
    self.cedula = cedula
    self.nombre = nombre
    self.apellido = apellido
    self.edad = edad
    
  def abrir_puerta(self):
    print(f"{self.nombre} esta abriendo la puerta.")

class Teacher(Person):
  def __init__(self, cedula, nombre, apellido, edad, sueldo):
    super().__init__(cedula, nombre, apellido, edad)
    self.sueldo = sueldo

  def imprimir_sueldo(self):
    print(f"el profesor {self.nombre} tiene un sueldo de {self.sueldo}.\n")

  def abrir_puerta(self):
    print(f"El profesor esta abriendo la puerta.")

first_person = Person("402-1882225-8", "Braily", "Roman", 18)
first_teacher = Teacher(first_person.cedula,first_person.nombre,first_person.edad,first_person.edad ,52000)

first_teacher.imprimir_sueldo()