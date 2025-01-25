#56
print("MENU")
print("1. Bocadillo de calamares - 9 €")
print("2. Bocadillo de chistorra - 4.5 €")
print("3. Bikini de jamón - 2.5 €")
print("ACOMPAÑAMIENTO")
print("1. Patatas finas - 1.5 €")
print("2. Patatas gruesas - 1.75 €")
print("3. Patatas rústicas - 2 €")
print("BEBIDAS")
print("1. Coca cola - 2 €")
print("2. Acuarius - 1.5 €")
print("3. Agua - 1 €")

print("El pedido se compone de: bocadillo + acompañamiento + bebida.")


total_bocadillos = 0
total_acompañamiento = 0
total_bebidas = 0
num_pedidos = 0

num_pedidos = int(input("Introduce el número de pedidos que vas a hacer: "))
contador = 0

while contador < num_pedidos:

    bocadillos = int(input("Introduce el número del bocadillo que quieres: "))
    if bocadillos == 1:
        total_bocadillos += 9
    elif bocadillos == 2:
        total_bocadillos += 4.5
    elif bocadillos == 3:
        total_bocadillos += 2.5
 
    acompañamiento = int(input("Introduce el número del acompañamiento que quieres: "))
    if acompañamiento == 1:
        total_acompañamiento += 1.5
    elif acompañamiento == 2:
        total_acompañamiento += 1.75
    elif acompañamiento == 3:
        total_acompañamiento += 2

    # Solicitar bebida
    bebida = int(input("Introduce el número de la bebida que quieres: "))
    if bebida == 1:
        total_bebidas += 2
    elif bebida == 2:
        total_bebidas += 1.5
    elif bebida == 3:
        total_bebidas += 1
    

    contador += 1


precio_total = total_bocadillos + total_acompañamiento + total_bebidas


if num_pedidos == 1:
    print("Se ha realizado un pedido.")
else:
    print(f"Se han realizado {num_pedidos} pedidos.")

print(f"El precio total es: {precio_total} €")


iva = precio_total * 0.10
precio_con_iva = precio_total + iva
print(f"El precio con el IVA aplicado es: {precio_con_iva} €")

if 20 < precio_total <= 30:
    descuento = precio_total * 0.05
    precio_final = precio_total - descuento
    print(f"El precio final con un descuento del 5% es: {precio_final:} €")
elif precio_total > 30:
    descuento = precio_total * 0.15
    precio_final = precio_total - descuento
    print(f"El precio final con un descuento del 15% es: {precio_final:} €")
