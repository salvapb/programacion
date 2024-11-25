#42. Imprima el siguiente patrón con el ciclo for. 
var="*****"

for contador in range(len(var)):
    contador+1
print(var[0:contador])

for contador in range(len(var)):
    print(var[contador:5])