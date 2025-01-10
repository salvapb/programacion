var_1=input("dime una contraseña de 8 caracteres: ")
contraseña=len(var_1)
while contraseña!=8:
    print("no aceptado")
    var_1=input("dime una contraseña de 8 caracteres: ")
    contraseña=len(var_1)
print("bien")