numberIn=int(input("Introduzca un numero   : "))
numberTemp=1
resultado= numberIn
while numberTemp !=numberIn:
    resultado *= numberTemp
    numberTemp += 1

print(f"El resultado del factorial del número {numberIn} es {resultado}")

from math import factorial
fact = factorial(numberIn)
print("El factorial es" ,fact )
print(f"El resultado del factorial \n del número {numberIn} \n es {fact}")
print(f"El resultado del factorial \t del número {numberIn} \t es {fact}")
