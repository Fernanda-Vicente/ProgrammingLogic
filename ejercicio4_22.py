#Fernanda Michelle Vicente Galindo.
#Ejercicio 4: Programa que sume números hasta que el usuario ingrese 0.

suma=0     #se define el valor de la variable.
numero= None    #se crea la variable y al asignarle el valor de None da a entender que no tiene un valor numerico asignado.

while numero!=0:   #Se crea el bucle con while, haciendo que se ejecute mientras el valor sea distinto que 0.
    numero=int(input("Introduzca un numero: "))  #le pedirá al usuario introducir algún número.
    suma+=numero     #se suma el valor de "numero" 
print("La suma total es: ")
print(suma)     #se imprime la suma total.

#EXPLICACIÓN: 
#Primero se definen las dos variables en este caso "suma" es iguala 0 y "numero" con None, esto significa que no tiene un valor númerico específico asignado.
#El bucle while en este código funciona cuando la variable "numero" es diferente a 0.
#Dentro de este bucle también se le pide al usuario que ingrese cualquier nuúmero, en la línea 9 se suma la variable "suma" y "numero".
#Finalmnente se imprime "La suma total" y el resulatdo de la suma se mostrará en la terminal.