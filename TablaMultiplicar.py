#Tabla de multiplicar utilizando el for
variableStringAcumulada=""
numero=int(input("Introduzca un número :"))
print("Ha introducido el valor ,", numero ,"\n")
print("----------------------------------------------------------------")
for i in range(1,11):
    print(f" multiplicando el valor de : \t{i} por el número \t {numero} \tsale = \t {i*numero}")
    print(" --------------------------------------------------------------------")
    parcial = i*numero
    variableStringAcumulada = variableStringAcumulada + " multiplicando el valor de : \t" + str(i) + " por el número \t " + str(numero) + "\tsale = \t " + str(i*numero) + "  , \n"
print("--------------------------------------------------------------------\n")
print(" ***************************************************************************")
print(" ***************************************************************************")
print(f" ** Ahora imprimos la tabla de multiplicar del 1 al 100, por el número {numero} **")
print(" ***************************************************************************")
print(" ***************************************************************************")
for i in range(1, 101):
        print(f" multiplicando el valor de : \t{i} por el número \t {numero} \tsale = \t {i * numero}")
        print(" ***************************************************************************")

print(" *************Vamos acumulando los valores en una cadena**************************")
print(f" La variable acumulada es {variableStringAcumulada}")
print(" *************Vamos impresos porque estaban acumulados los valores en una cadena**************************")