#62. Realiza un programa que pida dos números por teclado y presente por pantalla qué números hay pares e impares en ese rango. Utiliza for. Contempla si primer valor es superior al segundo.

var1=int(input("introduce un numero: "))
var2=int(input("introduce otro numero: "))

for recorrer in range(var1,var2):
    if recorrer%2==0:
        print(recorrer, "es par")
    else:
        print(recorrer, "es impar")
        