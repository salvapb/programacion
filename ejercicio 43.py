#43. Realiza un programa que recorra con un for una palabra introducida por teclado y se imprima por pantalla cada letra
var_palabra = input("Introduzca una palabra: ")
contador = 0
for recorrido in var_palabra:
    print("En la posición", contador,"está la", recorrido)
    contador+=1