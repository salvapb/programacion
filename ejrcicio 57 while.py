#57. Realiza un programa que permita adivinar un número comprendido entre 1 y 5. El programa debe controlar si el usuario introduce un número no comprendido entre 1 y 5
import random
intentos=0
numero=int(input("introduce un numero de 1 a 5: "))

numerosec=random.randint(1, 5)


while numero!=numerosec:
    print("numero no acertado")
    numero=int(input("vuelve a intentarlo: "))


print("numero acertado")