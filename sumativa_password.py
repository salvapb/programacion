#Realitzar un programa que permeti introduir una ‘paraula clau’ amb les següents característiques:
print('El password debe tener una longitud de entre 6 y 8 carácteres')
print('La contraseña debe respetar la siguiente secuencia:')
print('Posición 1: un número mayor o igual a 1 y menor o igual a 5')
print('Posición 2: una letra minúscula')
print('Posición 3: una letra mayúscula')
print('Posición 4: uno de los siguientes símbolos *, _, @')
print('Posición 5: una letra minúscula')
print('Posición 6: un número mayor o igual a 6 y menor o igual a 9')
print('Posición 7: un de los siguientes símbolos &, /, #')
print('Posición 8: un número menor o igual a 5')

password = input('Introduzca el password: ')
#Aquí pongo la variable errores para saber la cantidad de errores que hay en el password que se ha introducido.
errores = 0

#Este if sirve para medir la longitud de password. En caso de que la longitud no sea entre 6 y 8, como dice en las normas, se mostrará por pantalla un mensaje de error
if len(password)<6 or len(password)>8:
    print('Error, el password tiene una longitud de',len(password),'carácteres y no cumple los requisitos')
    
#Este elif le dice al programa que caso que la longitud del programa este entre los parámetros indicado, el programa siga adelante
elif len(password)==6 or len(password)==7 or len(password)==8:
    #Esto sirve para ver si el primer carácter esta entre 1 y 5, como dice en las normas. En caso que no sea así, por pantalla se mostrará un mensaje de error.
    if password[0]<str(1) or password[0]>str(5):
        #El end = '', lo que hace es, en caso que haya más de un error, todos saldrán concatenados, es decir, uno al lado del otro.
        print('Error en el carácter 1', end = ' ')
        #Esto sirve para que en caso de que este carácter no cumpla las normas del password, se le sume uno a la variable errores.
        errores = errores+1
    
    #Con este código comprobamos si el segundo carácter es una letra minúscula
    if password[1].islower() == False:
        print('Error en el carácter 2', end = ' ')
        errores = errores+1
        
    #Aquí el códiugo es bastate parecido al anterior, pero esta vez se comprueba si el carácter es una letra mayúscula.
    if password[2].isupper() == False:
        print('Error en el carácter 3', end = ' ')
        errores = errores+1
    
    #Este if comprueba que el carácter 4 sea uno de los 3 símbolos especificados en las normas.
    if not password[3] == '*' and not password[3] == '_' and not password[3] == '@':
        print('Error en el carácter 4', end = ' ')
        errores = errores+1
    
    #Este if comprueba de nuevo que el carácter sea una letra minsúcula
    if password[4].islower() == False:
        print('Error en el carácter 5', end = ' ')
        errores = errores+1
    
    #Con este if comprobamos que el carácter sea un número mayor o igual a 6, o un número menor o igual a 9.
    if password[5]<str(6) or password[5]>str(9):
        print('Error en el carácter 6', end = ' ')
        errores = errores+1
    
    #Este código de aquí es esencial, ya que hace que en caso de que el password tenga 6 carácteres, no ejecute los siguientes códigos, ya que estos solo se ejecutarán en caso de que el programa tenga 7 o 8 carácteres.
    if len(password)==7 or len(password)==8:    
        #Este if comprueba que el carácter 7 sea uno de los símbolos especificados en las normas.
        if not password[6] == '&' and not password[6] == '/' and not password[6] == '#':
            print('Error en el carácter 7', end = ' ')
            errores = errores+1
    
    #Con este if se consigue que el siguiente código solo se ejecute en caso de que el password no contenga 8 carácteres
    if len(password)==8:
        #Este if comprueba que el caracter sea un numero menor o igual a 5.
        if password[7]<str(0) or password[7]>str(5):
            print('Error en el carácter 8', end = ' ')
            errores = errores+1
    #Por último, este código le dice al programa que en caso de que no haya habido ningun error en el password, printee que el password es correcto por pantalla.        
    if errores==0:
        print('El formato del PASSWORD es correcto')