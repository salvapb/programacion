# 80
def es_decimal(valor):
    try:
        if '.' in valor and float(valor) == float(valor):
            print("Es un número con decimales")
        else:
            print("No es un número con decimales")
    except ValueError:
        print("No es un número con decimales")

valores = ["12", "12.1", "Hola", "12.", "6.098", "6.09a", "4.34.2"]
for v in valores:
    es_decimal(v)

