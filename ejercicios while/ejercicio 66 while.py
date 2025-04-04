#66. Repite el ejercicio 63. En lugar de ‘tirar’ 100 veces un dado, modifica el programa para ver cómose comporta el dado en lanzamientos producidos durante aprox 3 segundos. 

import random
import time

dado_contador = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

tiempo_inicio = time.time()

while time.time() - tiempo_inicio < 3:
    lanzamiento = random.randint(1, 6)  
    dado_contador[lanzamiento] += 1  

tiempo_total = time.time() - tiempo_inicio

print("RESUMEN")
print(f"Tiempo: {tiempo_total}")
print(f"Uno: {dado_contador[1]}")
print(f"Dos: {dado_contador[2]}")
print(f"Tres: {dado_contador[3]}")
print(f"Cuatro: {dado_contador[4]}")
print(f"Cinco: {dado_contador[5]}")
print(f"Seis: {dado_contador[6]}")