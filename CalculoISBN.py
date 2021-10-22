import sys
numeroISBN = input("Introduce el número ISBN")
parcial = 0
while len(numeroISBN) != 10:
    numeroISBN = input("Introduce el número ISBN :  ")
    print("Debes introducir 10 dígitos o no puedo calcularlo")
for i in range(0,len(numeroISBN)):
    strNumeroCalcular = numeroISBN[i: i + 1]
    intNumeroCalcular = int(strNumeroCalcular)
    print(f" Voy a multiplicar el valor : {strNumeroCalcular} , con el valor {i+1} para que me de {(i+1)*intNumeroCalcular}")

    parcial = parcial + (intNumeroCalcular*(i+1))
print(f" {parcial}")
if parcial%11==0:
    print("El número ISBN es correcto")
    sys.exit()
else:
    print("El número ISBN NO es Correcto")

print("Vamos a poner 2 elevado a 3")
print(pow(2,3))

print("Vamos a poner 2 elevado a 4")

print(pow(2,4))