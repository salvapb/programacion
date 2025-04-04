#57. Realiza un programa que permita adivinar un número comprendido entre 1 y 5. El programa debe controlar si el usuario introduce un número no comprendido entre 1 y 5
import random

numero=int(input("introduce un numero del 1 al 5: "))
if numero<1 or numero>5:
    print("el numero debe ser del 1 al 5")
numerosec=random.randint(1, 5)


while numero!=numerosec:
    print("no es igual")
    numero=int(input("vuelve a intentarlo: "))
print("programa finalizado")