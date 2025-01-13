#53. A partir del código anterior, haz que aparezca al finalizar el programa por pantalla el total las sumas y el número de repeticiones. Con While
repeticiones=0
suma_total=0
numero1=int(input("introduce el primer numero: "))
numero2=int(input("introduce el segundo numero: "))
suma=numero1+numero2
print(suma)
respuesta=input("deseas repetir la operacion s/n:")
repeticiones+=1
suma_total+=suma
while respuesta!= "n":
    if respuesta=="s":
        numero1=int(input("introduce el primer numero: "))
        numero2=int(input("introduce el segundo numero: "))
        suma=numero1+numero2
        print(suma)
        respuesta=input("deseas repetir la operacion s/n:")
        repeticiones+=1
        suma_total+=suma
print("el numero de repeticiones es: ",repeticiones)
print("la suma total es: ",suma_total)
print("programa finalizado")