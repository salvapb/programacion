#51. A partir del programa anterior, modifica el código para que sea el usuario quién introduzca el número de veces que desea que repita la frase Buenos días. Con While
repeticiones=0
var_veces=0
var_veces=int(input("introduce el numero de veces que quieres que se repita la frase: "))

while repeticiones<var_veces:
    print("buenos dias")
    repeticiones+=1
    