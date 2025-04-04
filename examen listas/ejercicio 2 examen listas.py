#ejercicio2
frase2=""
frase=input("introduce una frase: ")

lista1=frase.split()

palabra=input("introduce palabra: ")

contar=lista1.count(palabra)


frase2=",".join(lista1)
print(contar)
print(frase2)