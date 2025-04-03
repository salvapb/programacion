#33. Programa un código que permita contar el número de vocales de la siguiente frase: No hay mal que dure cien años

var_frase= "No hay mal que dure cien años"
print("No hay mal que dure cien años")
var_frase=var_frase.lower()

var_a=var_frase.find("a,e,i,o,u")
print("el numero de a es: ",var_a)
print("el numero de e es: ",var_e)
print("el numero de i es: ",var_i)
print("el numero de o es: ",var_o)
print("el numero de u es : ",var_u)

var_e=var_frase.find("e")
print("el numero de e es: ",var_e)

var_i=var_frase.find("i")
print("el numero de i es: ",var_i)

var_o=var_frase.find("o")
print("el numero de o es: ",var_o)

var_u=var_frase.find("u")
print("el numero de u es : ",var_u)