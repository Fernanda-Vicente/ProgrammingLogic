#Fernanda Michelle Vicente Galindo.
#Ejercicio 2: Juego de adivinar un número secreto entre 1 y 10.
num_secret=4   #se define el número secreto
num_usuario=0   
import random 

while num_secret!=num_usuario:   #se abre un bucle que se ejecuta mientras el número secreto sea diferente al del número del usuario
 num_usuario=(int(input("Adivina el número (entre 1 y 10): ")))    # el usuario ingresa el  número
 if num_usuario==num_secret:  #si el número de usuario es igual al número secreto se imprime el print.
  print("¡Felicidades!, adivinaste.")
 elif num_usuario!=num_secret:    #si es diferente se imprime el siguinete print.
  print("Incorrecto, intenta de nuevo.")

  #EXPLICACIÓN:
  #Se crea una variable en el cual se asigna el número secreto.
  #El bucle de while se ejecutará cuando el número secreto sea diferente que el número ingresado por el usuario.
  #En la línea 8 se pide al usuario ingresar el número que crea que es el secreto.
  #En la siguiente línea se usa el if para indicar si el número ingresado por el usuario es igual que el número secreto se imprime lo de la línea 10 en la terminal.
  #Con el elif da a entender que si no es asi y, el número igresado y el número secreto son diferentes se imprime el mensqaje de la línea 12.

  #En este código pude usar "if" y "elif" que estas se ejecutan cuando se cumplen ciertas condiciones.
  #Ademá pude comprender un poco mas de estas.