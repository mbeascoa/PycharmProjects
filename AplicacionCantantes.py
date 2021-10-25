import sys

print("APLICACIÓN CANTANTES")
cantantes= ["Miguel Beascoa","David Bisbal","Lola Flores","El Fary","Miguel Rios"]
quieraSeguir=True
while quieraSeguir :
        print ("-------------------------------------------")
        print ("1.- ALTA CANTANTE")
        print("2.- ELIMINAR CANTANTE")
        print("3.- LISTADO DE CANTANTES")
        print("4.- SALIR DE LA APLICACIÓN")
        print("--------------------------------------------")
        eleccion = int(input(" Indique su opción ....   :"))

        if eleccion == 1:

                addNombre = input(" Indique el Nombre del Cantante a Añadir  :")
                if addNombre in cantantes :
                        print("--------------------------------------------")
                        print("El cantante ya existe")
                        print("--------------------------------------------")
                        quieraSeguir = True
                else:
                         cantantes.append(addNombre)
                         print("--------------------------------------------")
                         print("El cantante ha sido añadido")
                         print("--------------------------------------------")
                         quieraSeguir = True

        elif eleccion== 2:

                deleteNombre = input(" Indique el Nombre del Cantante a borrar  :")
                if deleteNombre in cantantes:
                        cantantes.remove(deleteNombre)
                        quieraSeguir = True
                        print("--------------------------------------------")
                        print("El cantante ha sido borrado")
                        print("--------------------------------------------")
                else:
                        print("--------------------------------------------")
                        print("El cantante no existe y no se puede borrar")
                        print("--------------------------------------------")

        elif eleccion== 3:
                quieraSeguir=True
                i=1
                for valor in cantantes :
                        print("--------------------------------------------")
                        print(f" Orden {i} , {valor}")
                        i +=1

        elif eleccion== 4:
                quieraSeguir=False
                sys.exit()


