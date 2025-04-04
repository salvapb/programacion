#ejercicio3
listanum=[]
listaletra=[]
valores=input("introduce valores:")
lista1=valores.split("-")
for recorrer in lista1:
    if recorrer.isnumeric():
        listanum.append(int(recorrer))
    
    else:
        if "." in recorrer:
            listanum.append(recorrer)
        else:
            listaletra.append(recorrer)
            
print(listanum)
print(sum(listanum))



