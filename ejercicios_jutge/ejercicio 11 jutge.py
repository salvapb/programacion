letra = input()

if letra.isalpha() and len(letra) == 1:
    letra_cambiada = letra.lower() if letra.isupper() else letra.upper()
    print(letra_cambiada)
