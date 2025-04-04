#55. Última vez que reutilizamos el mismo código.. lo prometo . A partir del programa anterior haz que sea todo exactamente igual pero teniendo en cuenta que el programa se repita siempre y cuando la suma acumulada sea superior a 50 o la suma acumulada sea par. Con While

suma_total=0
repeticiones=0
while suma_total<50 or suma_total&2==0:
    numero1=int(input("introduce el primer numero: "))
    numero2=int(input("introduce el segundo numero: "))
    suma=numero1+numero2
    print("la suma es: ",suma)
    suma_total+=suma
    print("la suma total es: ",suma_total)
    repeticiones+=1
    if repeticiones==1:
        print("llevas",repeticiones,"repetición")
    else:
        print("llevas",repeticiones,"repeticiones")
else:
    print("programa finalizado")