var1=float(input("introduzca el peso en kilogramos: "))
var2=float(input("introduzca la estatura en metros: "))
imc=var1/var2**2
print("tu indice de masa corporal es: ",imc)
if imc>25:
    print("hay sobrepeso")
if imc==25:
    print("hay sobrepeso")
