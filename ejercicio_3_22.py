#Fernanda Michelle Vicente Galindo.
#Ejercicio 3: Menú interactivo que permita elegir opciones hasta seleccionar "Salir".

while True:      #Se crea un bucle el cual se repetirá.
 
 print("\n1. Opción 1.") #El "\n" se usa para dar un salto entre una línea y otra.
 print("2. Opción 2.")
 print("3. Salir")
 opcion=int(input("Elije una opción:"))  #El usuario ingresará la opción.
 
 if opcion==1:  # Si la opción elegida es 1 se imprimira "Elegiste la opción 1".
   print("Elegiste la opción:", opcion)
 elif opcion==2:   #Si no eligio la opcion anterior y eligió la 2 se imprime "Elegiste la Opción 2".
   print("Elegiste la opción:", opcion)
 elif opcion==3:   #Lo mismo sucede con la opción 3, solo que en esta es la salida del programa.
   print("Saliendo del programa.")
   break 
 
 #EXPLICACIÓN:
 #Se crea el bucle de while el cual repite el código.
 #Seguido de eso se crean los prints de las opciones con "\n", esto significa que habra un espacio entre el bucle que aparecerán en la terminal un poco separadas, y la opcion que ingresará el usuario.
 #También se usa "if" el cual se ejecuta cuando el usuario elije la opción 1 e imprime la linea 8 junto con la opción que el usuario colocó.
 #De igual manera se usa "elif" por si no se eligio lo opción anterior y en su caso colocó la opción 2 se imprime la linea 10 en la terminal.
 #Finalmente, al escoger la opción 3 en la terminal aparece "saliendo del programa", llegando a su limíte de opciones. Y con la instrucción "break", cortamos el bucle de while, para que no se repita.
 

