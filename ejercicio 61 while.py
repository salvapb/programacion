#61. A partir del código anterior, haz que el programa finalice si el valor de la tabla de multiplicar es superior o igual a 40.

numero=int(input("introduce el numero que quieras multiplicar: "))
repeticiones=0
while numero<40 and repeticiones!=10:
    repeticiones+=1
    numero=numero*repeticiones
    if numero<40:
        print(numero)
    else:
        print("programa finalizado")
