from typing import List

print(" --------------------Adivinamos si la letar introducida es vocal o consonante  --------------------")

vocales= [ "A", "E", "I", "O", "U"]
consonantes= ["B","C","D","F","G","H","J","K","L","M","N","Ñ","P","Q","R","S","T","V","X","Y","Z","W"]
numeros: list[str]=["1","2","3","4","5","6","7","8","9","0"]


letra=(input("----Introduce una letra : ")).upper()

while ((letra in vocales) or (letra in consonantes) or (letra in numeros)):
    if letra in vocales:
        print("La letra es una vocal")
    elif letra in consonantes:
        print("La letra es una consonante")
    elif letra in numeros:
        print("La letra es un numero")
    else:
       print("La letra es un caracter especial")
    letra=(input("----Introduce una letra : ")).upper()


do
    if letra in vocales:
        print("La letra es una vocal")
    elif letra in consonantes:
        print("La letra es una consonante")
    elif letra in numeros:
        print("La letra es un numero")
    else:
       print("La letra es un caracter especial")
    letra=(input("----Introduce una letra : ")).upper()
while ((letra in vocales) or (letra in consonantes) or (letra in numeros))