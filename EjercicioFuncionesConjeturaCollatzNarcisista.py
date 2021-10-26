import sys

resultado = ""
strValores = ""
quieroSeguir = True



def quieroSeguir():
    print("------ ...................................-----------")
    print("------ Pero qué listo es el hombre blanco!!")
    seguir=input("Quiere seguir con la tarea  ? (S/N) para confirmar  : ")
    if seguir=="S" or seguir=="s":
          quieroSeguir=True
    else:
          quieroSeguir=False


def numeroNarcisista(strNumeroNarcisita):
    potenciaDe= len(strNumeroNarcisita)
    suma=0.0

    for i in range(0, potenciaDe):
        strParcial = strNumeroNarcisita[i: i + 1]
        suma = suma + pow(int(strParcial), potenciaDe)

    if suma == int(strNumeroNarcisita):
        mensaje= "El número es narcisista"
        return mensaje

    else:
        mensaje= "El número no  es Narcisista"
        return mensaje



def conjeturaCollatz(numero):
    chorroNumeros = ""
    temporal=numero
    # print(f"1 --> : {temporal}")
    chorroNumeros= chorroNumeros + "1 --> : " + str(temporal) + "\n"
    i=2
    while temporal != 1:
         if temporal%2 ==0:
              temporal=temporal/2
              chorroNumeros= chorroNumeros + str(i) + " --> : " + str(temporal) + "\n"
              #print(f"{i} --> : {temporal}")
              i +=1
         else:
              temporal=temporal*3+1
              chorroNumeros = chorroNumeros + str(i) + " --> : " + str(temporal) + "\n"
              #print(f"{i} --> : {temporal}")
              i += 1

    return chorroNumeros



while (quieroSeguir) :
    print("------------------------------------------------------------")
    print("1. - Número Narcisista")
    print("2.-  Conjetura de Collatz ")
    print("3.-  Salir")
    print("------------------------------------------------------------")
    opcionMenu= int(input("Introduzca el número de la opción elegida  : "))



    if opcionMenu==1:
        strNumeroNarcisita = input("Introduzca un número para calcular si es Narcisista : ")
        resultado = numeroNarcisista(strNumeroNarcisita)
        print(resultado)
        quieroSeguir()

    elif opcionMenu==2:
        numero = int(input("Introduce un número para calcular la conjetura de Collatz: "))
        strValores= conjeturaCollatz(numero)
        print(strValores)
        temporal = numero
        quieroSeguir()
    elif opcionMenu==3:
        sys.exit()


