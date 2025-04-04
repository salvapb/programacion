#1
var1="1.sin plomo 95"
var2="2.sin plomo 98"
var3="3.gasoleo A"
var4="4.gasoleo A+"
print(var1, var2, var3, var4)
var_gasolina=input("introduce el numero del combustible que quieres: ")
var_litros=input("introduce el numero de litros que quieres repostar: ")

var_litros1=var_litros*1
var_litros2=var_litros*1
var_litros3=var_litros*1
var_litros4=var_litros*12

if var_gasolina == 1:
    print("el precio es: ",var_litros1)
    
elif var_gasolina== 2:
    print("el precio es: ",var_litros2,"y con el descuento queda: ",var_litros2/10)

elif var_gasolina==3:
    print("el precio es: ",var_litros3)

elif var_gasolina==4:
     print("el precio es: ",var_litros4 ,"y con el descuento queda en: ",var_litros4/12)