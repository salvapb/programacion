#31. Asigna a una variable de texto la siguiente frase: A quién madruga Dios ayuda. Comprueba si existen las siguientes palabras mostrando por pantalla la posición de su índice.

frase= "A quién madruga Dios ayuda"
var2=input("introduce una palabra:")

indice=frase.find(var2)
if var2 in frase:
    print("la palabra esta en la frase y esta en el indice",indice)
    
else:
    print("la palabra no esta en la frase") 