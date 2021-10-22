strNumeroNarcisita= input("Por favor introduce un número : ")

potenciaDe= len(strNumeroNarcisita)
suma=0.0
print(f" Potencia de ", potenciaDe)

for i in range(0, potenciaDe):
    strParcial = strNumeroNarcisita[i: i + 1]
    suma = suma + pow(int(strParcial), potenciaDe)

if suma == int(strNumeroNarcisita):
    print("El número es narcisista")
else:
    print("El número no  es Narcisista")
