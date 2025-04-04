#60. Diseña un programa que al introducir un número, realice su tabla de multiplicar del 1 al 10. Utiliza únicamente el while

numero=int(input("introduce el numero que quieras multiplicar: "))
numero_multi=0
repeticiones=0
while numero*10!=numero_multi and repeticiones!=11:
    print(numero*repeticiones)

    repeticiones+=1
