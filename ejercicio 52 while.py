#52. Realiza un programa que sume dos números enteros por teclado y presente el resultado por pantalla. El programa preguntará si deseas o no repetir la operación. Con While

numero1=int(input("introduce el primer numero: "))
numero2=int(input("introduce el segundo numero: "))
suma=numero1+numero2
print(suma)
respuesta=input("deseas repetir la operacion s/n:")
while respuesta!= "n":
    if respuesta=="s":
        numero1=int(input("introduce el primer numero: "))
        numero2=int(input("introduce el segundo numero: "))
        suma=numero1+numero2
        print(suma)
        respuesta=input("deseas repetir la operacion s/n:")
print("programa finalizado")
    