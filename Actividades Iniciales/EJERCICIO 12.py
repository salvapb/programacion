#12. Realiza un programa que, introduciendo en los valores de lado, base menor, base mayor y altura de un trapecio isósceles, nos devuelva por pantalla en el área y el perímetro.
var1=float(input("introduce el valor del lado del trapecio: "))
var2=float(input("introduce el valor de la base menor del trapecio: "))
var3=float(input("introduce el valor de la base mayor del trapecio: "))
var4=float(input("introduce el valor de la altura del trapecio: "))
perimetro=var1+var1+var2+var3
print("el perimetro es: ",perimetro)
area=(var2+var3)*var4/2
print("el area es: ",area)
