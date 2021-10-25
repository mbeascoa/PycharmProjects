print("--------------LISTAS-------------")
#las listas van en corchetes y los elementos separados por comas,,,,, []

print("-----------------------------------------------------------------")
print("CREANDO LISTAS DE ENTEROS imprimimos los valores 1 y 2 de la lista")
edades = [20, 84, 18, 41, 36, 25]

print("imprimimos toda la lista")
print("Edad 1:", edades[0])
print("Edad 2:", edades[1])

print("-----------------------------------------------------------------")
print("CREANDO LISTAS DE CADENAS imprimimos los valores 4 y 5 de la lista")
nombre = ["Benito", "Floro", "Alex", "Andrea", "Rosa", "Sara"]

print("Nombre 4:", nombre[3])
print("Nombre 3:", nombre[2])


nombre.append("Pepito")
print(nombre) #Mostramos la cadena con todos los valores de la lista
print("Nombre 7:",nombre[6])

#Añadir un valor a la lista
print("-----------------------------------------------------------------")
print("CREANDO LISTAS DE CADENAS, añadimos a Pepito en la tercera posición")
print("Insert, Permite insertar elementos a la lista. Ese elemento se insertará en la posición que indiquemos en el primer argumento ")
print(" En el segundo argumento incluiremos el valor a insertar.")
nombre= ["Benito", "Floro", "Alex", "Andrea", "Rosa", "Sara"]
print(nombre)
nombre.insert(2,"Pepito")
print(nombre) #Mostramos la cadena con todos los valores de la lista
print("Nombre 3:",nombre[2])
#--------------------------------------------------------------------------------
#Borrar un valor de la lista
print("-----------------------------------------------------------------")
print("CREANDO LISTAS DE CADENAS, borramos a Sara")
print("Eliminará el primer elemento que coincida con el valor indicado como argumento Sara")
print("No borra todas las ocurrencias de Sara")
nombre= ["Benito", "Floro","Sara", "Alex", "Andrea", "Rosa", "Sara", "Sara"]

print(nombre)
nombre.remove("Sara")
print(nombre) #Mostramos la cadena con todos los valores de la lista
#--------------------------------------------------------------------------------
print("-----------------------------------------------------------------")
print("CREANDO LISTAS DE CADENAS borramos el quinto elemento de la lista")
print("borraremos el nombre de la posición 4:")
nombre= ["Benito", "Floro", "Alex", "Andrea", "Rosa", "Sara"]

print (nombre)
del nombre[4]
print(nombre) #Mostramos la cadena con todos los valores de la lista
#--------------------------------------------------------------------------------

print("LISTAS DE CADENAS borramos un rango de valores, del 0 ,1 y 2  sin inlcuir el 3 que sería el 4 en la posición")
print("borraremos desde la poción cero hasta la posición tres (no incluyendo el tercer elemento")
nombre= ["Benito", "Floro", "Alex", "Andrea", "Rosa", "Sara"]
print(nombre)
del nombre[0:3]
print(nombre) #Mostramos la cadena con todos los valores de la lista


# En el siguiente ejemplo borraremos desde el primer elemento hasta el último.


print(" LISTAS DE CADENAS borraremos desde el primer elemento hasta el último")
nombre= ["Benito", "Floro", "Alex", "Andrea", "Rosa", "Sara"]

print(nombre)
del nombre[1:]
print(nombre) #Mostramos la cadena con todos los valores de la lista
#--------------------------------------------------------------------------------

print("----------------------------------------")
print(" LISTAS DE CADENAS borraremos todos los elementos de la lista.")
nombre= ["Benito", "Floro", "Alex", "Andrea", "Rosa", "Sara"]

del nombre[:]
print(nombre) #Mostramos la cadena con todos los valores de la lista

#--------------------------------------------------------------------------------
print("LISTAS DE CADENAS:  len Devuelve el número de elementos que contiene la lista")
nombre= ["Benito", "Floro", "Alex", "Andrea", "Rosa", "Sara"]
numeroelementos=len(nombre)
print("Número de elementos:",numeroelementos)
#--------------------------------------------------------------------------------

print(" LISTAS DE CADENAS  Imprimimos todos los valores de la lista")

nombre= ["Benito", "Floro", "Alex", "Andrea", "Rosa", "Sara"]
print ("La lista nombre se compone de estos valores ," , nombre)
for valor in nombre:
        print(valor)
#--------------------------------------------------------------------------------

print(" LISTAS DE CADENAS  in : Podemos preguntar si un elemento existe en la lista")

nombre= ["Benito", "Floro", "Alex", "Andrea", "Rosa", "Sara"]
print ("La lista nombre se compone de estos valores ," , nombre)
print("Está Andrea en la lista nombre?")
print("Andrea" in nombre) #Preguntamos si el elemento Andrea existe en la lista
print("Está Pepito en la lista nombre?")
print("Pepito" in nombre) #Preguntamos si el elemento Pepito existe en la lista


print(" LISTAS DE CADENAS  Sort")

print("Sort : Permite ordenar la lista de forma ascendente o descendente.")

print("ORDENANDO LISTAS ASCENDENTE , 1,10,6,7,4,9")
notas= [1,10,6,7,4,9]
notas.sort()
print("Nota más baja:",notas[0])
print("Segunda nota más baja:",notas[1])


print("ORDENANDO LISTAS DESCENDENTE de la lista 1,10,6,7,4,9")
notas.sort(reverse=True)

print("Nota más alta:",notas[0])
print("Segunda nota más alta:",notas[1])

for valor in notas:
    print(valor)

#------------------------------------------------------------------------------
print("--------------LISTAS---Podemos ordenar con cadenas:----------")

print("ORDENANDO LISTAS ASCENDENTE")
alumnos= ["BENITO","FLORO","ALEX","ANDREA","ZAMORA"]
alumnos.sort()
print("Primer alumno de la lista:",alumnos[0])
print("Segundo alumno de la lista:",alumnos[1])
for valor in alumnos:
    print(valor)

print("ORDENANDO LISTAS DESCENDENTE")
alumnos.sort(reverse=True)

print("Último alumno de la lista:",alumnos[0])
print("Penúltimo alumno más alta:",alumnos[1])
for valor in alumnos:
    print(valor)

