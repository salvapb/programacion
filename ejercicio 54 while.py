#54. Modifica el programa anterior y haz que se repita el ciclo automáticamente hasta que el total de todas las sumas sea superior a 50, será entonces cuando el programa finalice. No hará falta preguntar si deseas repetir la operación. En cada operación aparece por pantalla la suma de la operación y su acumulado. Para aquellos de vosotros que os fijáis en los detalles, controlar que el mensaje del acumulado es singular o plural.. . Con While
suma_total=0
repeticiones=0
while suma_total<50:
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
    if suma_total>50:
        print("has llegado a 50, programa finalizado")

