#15. Utiliza el valor Pi de la librería math para calcular el área y volumen de un cilindro, introduciendo por teclado el valor de radio y altura. Resultado con 2 decimales.

import math
var1=int(input("introduce el valor de radio: "))
var2=int(input("introduce el valor de altura: "))

area=2*math.pi*var1*var2+2*math.pi*var1**2

print("el area es: ","{:.2f}".format(area))
volumen=math.pi*var1**2*var2
print("el volumen es: ","{:.2f}".format(volumen))
