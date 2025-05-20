class Contacto:                   #Clase que recopile la información del contacto
  def __init__(self, nombre, apellido, celular):
    self.nombre = nombre;
    self.apellido = apellido;
    self.celular = celular
  
  def __str__(self):
    return f"Información de contacto: Nombre: {self.nombre}, Apellido: {self.apellido}, Celular: {self.celular}"  #Muestra información del contacto
  
  
class Contactos():               #clase que crea una lista de contactos, agrega elementos a esa lista y los elimina
  def __init__(self):
    self.lista_de_contactos = []
  
  def agregar_contactos(self, contacto):           #Agrega a la lista de contactos 
    nombre = contacto.nombre
    apellido = contacto.apellido
    celular = contacto.celular
    tupla = (nombre, apellido, celular)       #Crea una tupla con los elementos del objeto Contacto creado
    self.lista_de_contactos.append(tupla)        #Lo agrega a la lista de contactos
    
  def eliminar_contactos(self,contacto):       #Elimina contacto
    for i in self.lista_de_contactos:            #Iteramos en la lista para buscar el contacto a eliminar
      if contacto.nombre == i[0]:                #Lo encontramos
        indice = self.lista_de_contactos.index(i)        #Buscamos su indice
        self.lista_de_contactos.pop(indice)               #Lo eliminamos por el indice
    
  
  def mostrar_contactos(self):
    return self.lista_de_contactos                    #Muestra la lista de contactos
  
  
martin = Contacto("Martin", "Taroco", 92425889)
gabriel = Contacto("Gabriel", "Antúnez", 92425489)
pedro = Contacto("Pedro", "Díaz", 93425481)

contactos = Contactos()

contactos.agregar_contactos(martin)
contactos.agregar_contactos(gabriel)
contactos.agregar_contactos(pedro)

lista = contactos.mostrar_contactos()
print(lista)


contactos.eliminar_contactos(martin)

lista = contactos.mostrar_contactos()

print(lista)
