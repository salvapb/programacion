#58. Modifica el programa anterior para que tengas 3 intentos. Utiliza while
import random
intentos=0
numero=int(input("introduce un numero de 1 a 5: "))
intentos+=1

numerosec=random.randint(1, 5)


while numero!=numerosec and intentos <3:
    
    print("numero no acertado")
    intentos+=1
    numero=int(input("vuelve a intentarlo: "))
print("numero acertado")
if intentos==3:
    print("programa finalizado, has hecho los 3 intentos")