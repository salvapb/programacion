#Realitzar un programa que permeti introduir una ‘paraula clau’ amb les següents característiques

print("La longitud del password té que tenir una longitud d’entre 6 i 8 caràcters")
print("La introducció per teclat de cada caràcter respectarà la següent seqüencia: ")
print("Posicion 1: Un número major o igual 1 i menor o igual a 5")
print("Posicion 2: Una lletra minuscula")
print("Posicion 3: Una lletra majuscula")
print("Posicion 4: Un dels següents símbols *,_,@")
print("Posicion 5: Una lletra minuscula")
print("Posicion 6: Un numero major o igual 6 i menor o igual a 9")
print("Posicion 7: Un dels següents símbols %,/,#")
print("Posicion 8: Un número menor o igual que 5")

password=input("introduce la palabra clave: ")
#esta variable sirve para saber el numero de errores durante el password
errores=0
#este if len sirve para que si la contraseña introducida tiene menos de 5 caracteres introducir un error
if len(password)<6 or len(password)>8:
    print("Error, el password té una longitud de" ,len(password)," caràcters i no compleix els requisits")
#este elif sirve para saber si la contraseña introducida esta dentro de los parametros indicados para seguir con el program
elif len(password)==6 or len(password)==7 or len(password)==8:
#esto sirve para que el primer carácter siga las normas establecidas de que el primer numero tiene que estar entre 1 y 5
    if password [0]<str(1) or password [0]>str(5):
        print("Error en el caràcter 1" ,end=" ")
        errores=errores+1
#el islower sirve para que el segundo caracter sea minuscula como dicen las normas
    if password[1].islower() == False:
        print("Error en el caràcter 2" ,end=" ")
        errores=errores+1
#el isupper sirve para que el tercero caracter sea mayuscula como dicen las normas
    if password[2].isupper() == False:
        print("Error en el caracter 3",end=" ")
        errores=errores+1
#este if not sirve para encontrar en el 4 carácter un:@,*,_. Si no lo tiene se introduce un error
    if not password[3]=="@" and not password[3]=="*" and not  password[3]=="_":
        print("Error en el caràcter 4",end=" ")
        errores=errores+1
#el islower sirve para que el segundo caracter sea minuscula como dicen las normas
    if password[4].islower() == False:
        print("Error en el caràcter 5",end=" ")
        errores=errores+1
#esto sirve para que el quinto carácter siga las normas establecidas de que el primer numero tiene que estar entre 1 y 5
    if password [5]<str(6) or password [5]>str(9):
        print("Error en el caràcter 6",end=" ")
        errores=errores+1

#este if len sirve para que  el programa identifique si tiene 7 u 8 letras para seguir
    if len(password)==7 or len(password)==8:
#este if not sirve para encontrar en el 6 carácter un:/,%,#. Si no lo tiene se introduce un error
        if not password[6] == "%" and not password[6] == "/" and not  password[6] == "#":
            print("Error en el caràcter 7",end=" ")
        errores=errores+1
#este if len le sirve al programa para saber si la contraseña tiene 8 letras para seguir
    if len (password)==8:
#esto sirve para que el septimo carácter siga las normas establecidas de que el primer numero tiene que estar entre 1 y 5
        if password [7]<str(0) or password[7]>str(5):
            print("Error en el caràcter 8",end=" ")
        errores=errores+1
# este if errores==0 le indica al programa que si en la variable errores no se ha sumado nada significa que el password es correcto
    if errores==0:
        print("el password es correcto")