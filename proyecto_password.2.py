#Realiza la VERSIONN 2 de la actividad Password utilizando bucles (for)
print("1.introduce un numero que esté dentro de el siguiente intervalo:1-3,")
print("1.introduce un numero que esté dentro de el siguiente intervalo:4-6")
print("1.introduce un numero que esté dentro de el siguiente intervalo:7-9")
print("3.introduce uno de estos simbolos *, _, @")
print("El password debe tener dos letras mayúsculas")
print("El password debe tener una letra minúscula")
print("3.introduce uno de estos simbolos  &, /, #")
print("la plabra tiene que tener 8 caracteres")

error1="Falta un número entre 1 y 3 "
error2="Falta un número entre 4 y 6 "
error3="Falta un número entre 7 y 9 "
error4="Falta una letra minúscula "
error5="Falta una letra mayúscula "
error6="Faltan dos letras mayusculas"
error7="Falta un símbolo de los siguientes: *,  _, @ "
error8="Falta un símbolo de los siguientes: &, /, # "
errores=error1 + error2 + error3 + error4 + error5 + error6 + error7+error8

var_min=0
var_may=0
error1=0
error2=0
error3=0
error4=0
error5=0
error6=0
error7=0
error8=0


password=input("introduce la palabra clave: ")

if len(password)<8 or len(password)>8:
    print("Error, el password té una longitud de" ,len(password)," caràcters i no compleix els requisits")
    if password.islower():
        var_min=var_min+1
        if var_min==0:
            error3=error3+1
    if password.isupper():
        var_may=var_may+1
        if var_may==0:
            error5=error5+1
            if var_may==1:
                error4=error4+1
        if not password=="@" and not password=="*" and not  password=="_":
            error6=error6+1
    if not password == "%" and not password == "/" and not  password == "#":
        error7=error7+1
        if password <str(3) or password >str(1):
            error1=error1+1
        if password <str(6) or password >str(4):
            error2=error2+1
        if password <str(9) or password >str(7):
            error3=error3+1
            print(error3)



