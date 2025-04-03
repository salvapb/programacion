import math
var1=int(input("introduce el valor de radio: "))
var2=int(input("introduce el valor de altura: "))

area=2*math.pi*var1*var2+2*math.pi*var1**2

print("el area es: ","{:.2f}".format(area))
volumen=math.pi*var1**2*var2
print("el volumen es: ","{:.2f}".format(volumen))
