#46. A partir del programa anterior, soluciona el error que se produce en el test anterior con la palabra Abrigo utilizando únicamente una instrucción.
vocales = "aáeéiíoóuú"
vocales_f = ""
consonantes_f = ""
palabra = input("Introduce una palabra: ")

for recorrido in palabra.lower():
    if recorrido in vocales:
        vocales_f = vocales_f + recorrido
    else:
        consonantes_f = consonantes_f + recorrido
       
print("Las vocales en la palabra",palabra, "son:", vocales_f)
print("Las consonantes en la palabra", palabra,"son:", consonantes_f)