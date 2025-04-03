#32. Cómo solucionarías con ayuda de métodos String el problema del ejercicio anterior para no distinguir entre mayúsculas y minúsculas
frase= "A quién madruga Dios ayuda"
var2=input("introduce una palabra:")
frase=frase.lower()
var2=var2.lower()

indice=frase.find(var2)
if var2 in frase:
    print("la palabra esta en la frase y esta en el indice",indice)
    
elif var2 in frase:
    print("la palabra esta en la frase y esta en el indice", indice)    
else:
    print("la palabra no esta en la frase") 