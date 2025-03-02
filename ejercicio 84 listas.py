import random

listaword=""
listadeletras=[]
listadesorden=[]
lista=["casa","barco","gato","perro","madera","agua","puente","pantalón"]
listaword1=random.choice(lista)
listaword="-".join(listaword1)

listadeletras=listaword.split("-")

while len(listadeletras)>0:

    letra=random.choice(listadeletras)

    listadesorden.append(letra)

    listadeletras.remove(letra)
palabrasecreta="".join(listadesorden)

print("FORMA UNA PALABRA CON ", palabrasecreta)
 
usuario=input("adivina la palabra: ")

while listaword1!=usuario:
    print("error, no has hacertado")
    usuario=input("adivina la palabra: ")
else:
    print("eres un máquina")