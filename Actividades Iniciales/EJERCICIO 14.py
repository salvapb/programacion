#14. Realiza un programa que a partir de introducir el diámetro de un círculo calcule el área y perímetro. Importa la librería match y utiliza el valor PI para hacer el cálculo. Redondea el resultado a un decimal.

import math
var1=int(input("introduce el valor del diametro: "))
perimetro=round(2*math.pi*(var1/2))
print("el perimetro es: ",perimetro)
area=round(math.pi*(var1/2)**2)
print("el area es: ", area)
