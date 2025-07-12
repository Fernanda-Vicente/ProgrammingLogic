class Perros:
    def _int_(self, nombre, raza, color): #Constructor
       self.nombre=nombre
       self.raza=raza
       self.color=color
    def ladrar(self): #METODO DE ACCION/parametro para inicializar.
        print("Guau!")
        print("-"*30) #Separador

    def mostrar_informacion(self): #METODOS QUE MUESTRA DE LA INFORMACION
        print(f"Nombre:{self.nombre}")
        print(f"Raza:{self.raza}")
        print(f"Color:{self.color}")
        print("-"*30) #Separador

perro1 = Perros("Lucas", "Husky", "Blanco")
perro2=Perros("Max","Labrador", "Miel")
perro3=Perros("Plga", "Chihuahua","Negro")
   #ACCEDIENDO A LOS OBEJETOS CON SUS ATRIBUTOS
perro1.mostrar_informacion()
perro2.ladrar()
perro3.mostrar_informacion()