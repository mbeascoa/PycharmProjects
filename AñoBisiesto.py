strDNI=input("Introduzca el número del año, y le diremos si el año es bisiesto o no :  \n")
if int(strDNI)%4==0:
    divisiblepor100= (int(strDNI) % 100 != 0)
    print("Es divisible por 4 vamos a verificar si es divisible por 100, en cuyo caso no es bisiesto")
    if int(strDNI) % 100 != 0:
        print("Es divisible por 4 y no es divisible por 100")
        print("El año es bisiesto")
        if int(strDNI) % 400 == 0:
            print("Es divisible por 4 y  es divisible por 100, pero también  es divisible por 400 en cuyo caso es año bisiesto también")
    else :
        print("El año no es bisiesto")

else:
    print("El año no es bisiesto")


