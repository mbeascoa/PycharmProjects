diaSemana= ("Sabado", "Domingo", "Lunes", "Martes", "Miercoles", "Jueves", "Viernes")

dia= int(input("Introduce el día de tu nacimiento : "))
mes= int(input("Introduce el mes de tu nacimiento : "))
anio= int(input("Introduce el año de tu nacimiento : "))

if mes == 1:
    mes= 13
    anio= anio-1
elif mes== 2:
    mes=14
    anio=anio-1

# 1 .- multipa el mes mas 1 por 3 y dividirlo entre 5
operacion1= int((mes+1)*3 / 5)
print(f"operacion1  --->   {operacion1}")

# 2.- dividir año entre 4
operacion2= int(anio/4)

print(f"operacion2  --->   {operacion2}")

# 3.- dividir el año entre 100
operacion3 = int(anio/100)
print(f"operacion3  --->   {operacion3}")

# 4.- dividir el año entre 400
operacion4= int(anio/400)
print(f"operacion4  --->   {operacion4}")

# 5.- Sumar el dia, el doble del mes, el año, el resultado de la operación 1, el resultado de la operación 2, menos el resultado de
#la operación 3 más la operación 4 más 2.
# 15 + (6 * 2) + 1997 + 4 + 499 - 19 + 4 + 2  2514
operacion5= int(dia + (mes*2) + anio + operacion1 + operacion2 -operacion3 + operacion4 +2)
print(f"operacion5  --->   {operacion5}")

# 6.- Dividir el resultado anterior entre 7.
#2514 / 7  359
operacion6 = int(operacion5 / 7)
print(f"operacion6  --->   {operacion6}")

#7.- Restar el número del paso 5 con el número del paso 6 por 7.
# 2514 – (359 * 7)  1
operacion7 = int( operacion5 - (operacion6 * 7 ))
print(f"operacion7  --->   {operacion7}")
# # Miramos la tabla y vemos que el número 1 corresponde a DOMINGO
print(f"El día que naciste fue , {diaSemana[operacion7]}")