#63. Realiza un programa que permita tirar 100 veces un dado y nos presente por pantalla el número de veces que se repite cada número
import random
numerorandom=0
tiradas=0
numeros1=0
numeros2=0
numeros3=0
numeros4=0
numeros5=0
numeros6=0

while tiradas<100:
    numerorandom=random.randint(1,6)
    if numerorandom==1:
        numeros1+=1
    elif numerorandom==2:
        numeros2+=1
    elif numerorandom==3:
        numeros3+=1
    elif numerorandom==4:
        numeros4+=1
    elif numerorandom==5:
        numeros5+=1
    else:
        numeros6+=1
    tiradas+=1


print(f"los numeros unos han sido {numeros1}, de dos{numeros2}, de tres {numeros3},de cuatros {numeros4}, de cincos {numeros5} y de seis {numeros6}")
    
