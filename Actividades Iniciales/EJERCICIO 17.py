#17. Calcula el índice de masa corporal IMC de una persona, introduciendo por teclado elpeso (en kg) y dividiendo por la estatura (en metros y elevado al cuadrado). Si el resultadoes igual o superior a 25, debe aparecer un mensaje informando de sobrepeso.
var1=float(input("introduzca el peso en kilogramos: "))
var2=float(input("introduzca la estatura en metros: "))
imc=var1/var2**2
print("tu indice de masa corporal es: ",imc)
if imc>25:
    print("hay sobrepeso")
if imc==25:
    print("hay sobrepeso")
