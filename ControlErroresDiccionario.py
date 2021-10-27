colores = dict()
colores={
    "Azul":"Blue",
    "Rojo":"Red",
    "Amarillo":"Yellow",
    "Blanco":"White",
    "Negro":"Black"
}
quieroSeguir=True
while quieroSeguir:
    colorIn=input("Introduce un color para ver si está en el diccionario")
    try:
        dato=colores[colorIn]
        print(dato)
    except TypeError:
        print("Es un error de tipeado mal de la función")
    except KeyError:
        print("El valor no está en el diccionario")
    finally:
        strSeguir=input("Quiere Seguir?? (S/N) " )
        if strSeguir == "S" or strSeguir=="s" :
            quieroSeguir=True
        else:
            quieroSeguir=False
