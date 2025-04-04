# PARTE 1: 7.5
import random
while True:
        acumulado = 0
        print("Bienvenido al juego del 7 y medio")
        while True:
            respuesta=input("¿Quieres carta? (s/n): ")
            if respuesta=="n":
                break
            elif respuesta=="s":
                carta=random.randint(1, 12)
                while carta in [8, 9]:
                    carta=random.randint(1, 12)
                print("Tu carta es:",carta)
                if carta in [10, 11, 12]:
                    acumulado +=0.5
                else:
                    acumulado +=carta
                print("Acumulas:",acumulado)
                if acumulado > 7.5:
                    print("Has perdido la partida!")
                    break
        if acumulado == 7.5:
            print("Enhorabuena, has ganado la partida")
        elif 6 <= acumulado < 7.5:
            print("Has sido un poco conservador")
        else:
            print("Quizás tendrías que arriesgar un poco ¿no?")
        repetir=input("¿Quieres jugar otra partida? (s/n): ")
        if repetir == "n":
            break

