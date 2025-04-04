#45. Realiza un programa que permita introducir una palabra por teclado y puedas recorrer el string distinguiendo vocales y las consonantes:
vocales = "aáeéiíoóuú"
vocales_f = ""
consonantes_f = ""
palabra = input("Introduce una palabra: ")

for recorrido in palabra:
    if recorrido in vocales:
        vocales_f = vocales_f + recorrido
    else:
        consonantes_f = consonantes_f + recorrido
       
print("Las vocales en la palabra", palabra, "son:", vocales_f)
print("Las consonantes en la palabra", palabra,"son:", consonantes_f)