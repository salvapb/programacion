# PARTE 1: 7.5
import random
alias=input("introduce tu alias: ")
while True:
        acumulado = 0
        print("Bienvenido al juego del 7 y medio ", alias)
        while True:
            respuesta=input("¿Quieres carta? (s/n): ")
            if respuesta=="n":
                break
            elif respuesta=="s":
                carta=random.randint(1, 12)
                while carta in [8, 9]:
                    carta=random.randint(1, 12)
                print(f" {alias}Tu carta es:",carta)
                if carta in [10, 11, 12]:
                    acumulado +=0.5
                else:
                    acumulado +=carta
                print(f"{alias} Acumulas:",acumulado)
                if acumulado > 7.5:
                    print("Has perdido la partida! Ahora es el turno es de la BANCA")
                    break
        if acumulado == 7.5:
            print("Enhorabuena, has ganado la partida Ahora es el turno es de la BANCA")
        elif 6 <= acumulado < 7.5:
            print("Has sido un poco conservador Ahora es el turno es de la BANCA")
        else:
            print("Quizás tendrías que arriesgar un poco ¿no? Ahora es el turno es de la BANCA")
        repetir=input("¿Quieres jugar otra partida? (s/n): ")
        
        if repetir == "n":
            break
        
TURNO DE LA BANCA. Pulsa enter para visualizar carta a carta