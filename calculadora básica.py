def calculadora():
    print("calculadora básica")

    num1=int(input("Ingresa el primer número: "))
    num2=int(input("Ingresa el segundo número: "))

    print("\nSelecciona la operación: ")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    opcion=int(input())


    if opcion==1:
        print(f"\nEl resultado de sumar {num1}+{num2} es: {num1+num2}")
    elif opcion==2:
        print(f"\nEl resultado de restar {num1}-{num2} es: {num1-num2}")
    elif opcion==3:
        print(f"\nEl resultado de multiplicar {num1}*{num2} es: {num1*num2}")
    elif opcion==4:
        if num2 !=0:
            print(f"\nEl resultado de dividir {num1}/{num2} es: {num1/num2}")
        else:
            print("\nError: no se puede dividir entre 0")
    else:
        print("\nOpción inválida. Por favor elige una opción correcta.")
calculadora()