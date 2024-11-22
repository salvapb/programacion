#37. Programa que pregunte cuantas notas quiero introducir y para cada nota diga si estoy aprobado o suspendido.
num_notas=int(input("introduce el numero de notas que quieres introducir: "))

for contador in range (num_notas):
    nota=float(input("introduce tu primera nota: "))
    if nota>5:
        print("asignatura aprobada")
    if nota<5:
        print("asignatura suspendida")