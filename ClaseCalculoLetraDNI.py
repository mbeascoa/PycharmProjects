from ClaseDNI import DNI
vocales= [ "A", "E", "I", "O", "U"]
consonantes= ["B","C","D","F","G","H","J","K","L","M","N","Ñ","P","Q","R","S","T","V","X","Y","Z","W"]
numeros: list[str]=["1","2","3","4","5","6","7","8","9","0"]
strDNI=input("Introduzca el número del DNI sin la letra :  \n")
quiereIntentarlo=True
resultadoLetra=""

while quiereIntentarlo :
    while len(strDNI) != 8:
            print("Vuelva a intentarlo")
            strDNI = input("Introduzca el número del DNI sin la letra :  \n")

    dniInst= DNI()
    resultadoLetra = dniInst.calculoLetra(strDNI)


    print("La letra del DNI es , ", resultadoLetra)
    print(" ----------------------------------------------")
    intento = input("¿Quiere volver a intentarlo? (S/N)").upper()
    if intento=="S":
        quiereIntentarlo=True
        strDNI = input("Introduzca el número del DNI sin la letra :  \n")
    else:
        quiereIntentarlo=False


