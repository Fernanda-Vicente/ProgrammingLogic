seg=int(input("Ingrese la cantidad de segundos: "))
horas=seg//3600 #se convierten seg a hrs
sobrantes1=seg%3600   
minutos=sobrantes1//60  #conversion a minutos
sobrantes2=sobrantes1%60  #seg sobrantes
print("horas")
print(horas)
print("minutos")
print(minutos)
print("segundos")
print(sobrantes2)