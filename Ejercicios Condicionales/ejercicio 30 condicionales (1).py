#30. Realiza un programa que controle si la longitud de una frase introducida por teclado esigual, menor o mayor de 11 caracteres. Utiliza elif

var1=input("introduce una frase: ")

longitud=len(var1)

if longitud>11:
    print("la frase tiene 11 o mas caracteres")

elif longitud<11:
    print("la frase tiene menos de 11 caracteres")
    
else:
    print("la frase tiene 11 caracteres")
