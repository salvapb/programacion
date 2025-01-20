#59. Diseña un programa que “piense” un numero aleatorio entre 0 y 1000 para que nos pida que intentemos adivinarlo. En cada intento, el programa nos dirá si el numero introducido es mayor o menor del correcto. No utilices break para salir del bucle. Cuando se acierte el número debe mostrarse por pantalla un mensaje y el número de intentos.
import random
intentos=0

numerorandom=random.randint(1,1000)
numero=int(input("introduce un numero: "))
while numerorandom!=numero:
    intentos+=1
    if numerorandom<numero:
        print("el numero que has introducido es mayor")
    elif numerorandom>numero:
        print("el numero que has introducido es menor")

    numero=int(input("introduce un numero: "))      
else:
    print(f"has acertado,llevas {intentos} intentos")
