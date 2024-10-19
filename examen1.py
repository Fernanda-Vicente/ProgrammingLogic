name=input("Ingrese su nombre: ")
calificación1= int(input("Ingrese la primera calificación (de 0 a 100): "))
calificación2= int(input("Ingrese la segunda calificación (de 0 a 100): "))
calificación3= int(input("Ingrese la tercera calificacion (de 0 a 100): "))
promedio=(calificación1+calificación2+calificación3) /3

print("{:<25}" .format("Nombre"))
print("{:<25}" .format(name))
print("{:<25}" .format("Calificaciones"))
print("{:<25}" .format(calificación1))
print("{:<25}" .format(calificación2))
print("{:<25}" .format(calificación3))
print("{:<25}" .format("Promedio final"))
print("{:<25}" .format(promedio))

if promedio >=70:
        print(f"\nAprobado")
elif promedio <=70:
        print(f"\nReprobado")