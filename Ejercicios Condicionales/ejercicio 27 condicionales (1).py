#27. Mejora el programa anterior para controlar que el valor introducido es una letra y en caso de introducir un número, aparezca un aviso por pantalla

var1=input("introduce una letra: ")

if var1.islower()==True:
    print("la letra es minuscula")
    
elif var1.isupper()==True:
    print("la letra es mayuscula")
    
elif var1.isnumeric()==True:
    print("El valor introducido es un número")

else:
    print("La letra es mayúscula ¿?")
