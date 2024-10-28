#31. Asigna a una variable de texto la siguiente frase: A quién madruga Dios ayuda. Comprueba si existen las siguientes palabras mostrando por pantalla la posición de su índice.

var1= A quién madruga Dios ayuda 
var2=input("introduce una palabra:")

if var2 in var1:
    print("la palabra esta en la frase y esta en el indice")
    
else:
    print("la palabra no esta en la frase") 