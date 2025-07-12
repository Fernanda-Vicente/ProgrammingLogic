''''Instrucciones'''

class Perros:
    def __init__(self, nombre, raza, color): #Constructor
       self.nombre=nombre
       self.raza=raza
       self.color=color
        
    '''Constructor: Metodo especial dentro de una clase que se llama automaticamente cuando se crea una instancia.
        
       Su funcion principal es inicializar el objeto asignando sus valores.'''
     

    def ladrar(self): #METODO DE ACCION/parametro para inicializar.
        print("Guau!")
        print("-"*30) #Separador

    def mostrar_informacion(self): #METODOS QUE MUESTRA DE LA INFORMACION
        print(f"Nombre:{self.nombre}")
        print(f"Raza:{self.raza}")
        print(f"Color:{self.color}")
        print("-"*30) #Separador


    #CREACION DE INSTANCIAS
perro1=Perros("Lucas", "Husky", "Blanco")
perro2=Perros("Max","Labrador", "Miel")
perro3=Perros("Plga", "Chihuahua","Negro")
   #ACCEDIENDO A LOS OBEJETOS CON SUS ATRIBUTOS
perro1.mostrar_informacion()
perro2.ladrar()
perro3.mostrar_informacion()