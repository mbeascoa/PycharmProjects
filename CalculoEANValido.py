from ClaseCodigoEAN import EAN
vocales= [ "A", "E", "I", "O", "U"]
consonantes= ["B","C","D","F","G","H","J","K","L","M","N","Ñ","P","Q","R","S","T","V","X","Y","Z","W"]
numeros: list[str]=["1","2","3","4","5","6","7","8","9","0"]
strEAN=input("Introduzca el número del EAN, una cifra de 8 o 13 números:  \n")
quiereIntentarlo=True
resultadoEAN=False
tipo= 1

while quiereIntentarlo :
    while len(strEAN) != 8 and len(strEAN) !=13 :
            print("Vuelva a intentarlo")
            strEAN = input("Introduzca el número del EAN nuevamente, un númeo de 8 o 13 cifras :  \n")

    eanInst= EAN()
    tipo= len(strEAN)
    resultadoEAN = eanInst.calcularValidezEAN(strEAN, tipo)
    print(" Es válido el EAN ?" , resultadoEAN)
    #resultadoBoolStr = "válido" if resultadoEAN == True else "erróneo"
    if  resultadoEAN == True:
        resultadoBoolStr = "válido"
    else:
        resultadoBoolStr = "erróneo"

    #saludo = 'HOLA' if lang=='es' else 'HI'

    print(f"La numeración correspondiente al EAN {strEAN}  es  {resultadoBoolStr}")
    print(" ----------------------------------------------")
    intento = input("¿Quiere volver a intentarlo? (S/N)").upper()
    if intento=="S":
        quiereIntentarlo=True
        strEAN = input("Introduzca el número del EAN :  \n")
    else:
        quiereIntentarlo=False
