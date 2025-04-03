#28. Mejora el programa anterior para controlar también la introducción de símbolos. Utiliza elif.
var1=input("introduce una letra: ")

if var1.islower()==True:
    print("la letra es minuscula")
    
elif var1.isupper()==True:
    print("la letra es mayuscula")
    
elif var1.isnumeric()==True:
    print("El valor introducido es un número")

else:
    print("La letra es un simbolo")


