numero = int(input("Introduce un número : "))
temporal=numero
print(f"1 --> : {temporal}")
i=2
quieroSeguir=True
while quieroSeguir:
    while temporal != 1:
        if temporal%2 ==0:
            temporal=temporal/2
            print(f"{i} --> : {temporal}")
            i +=1
        else:
            temporal=temporal*3+1
            print(f"{i} --> : {temporal}")
            i += 1
    print("------ ...................................-----------")
    print("------ Pero qué listo es el hombre blanco!!")
    seguir=input("Quiere seguir con la tarea  ? (S/N) para confirmar  : ")
    if seguir=="S" or seguir=="s":
        quieroSeguir=True
        numero = int(input("Introduce un número : "))
        temporal = numero
    else:
        quieroSeguir=False