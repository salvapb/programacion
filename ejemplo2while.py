import random

numero=int(input("introduce un numero: "))

numerosec=random.randint(1, 4)


while numero!=numerosec:
    print("no es igual")
    numero=int(input("vuelve a intentarlo: "))
print("programa finalizado")