#Comprobar que el código tiene 8 o 13 dígitos. De no ser así, no es correcto.
#ope1.-  Sumar los dígitos de lugares pares por un lado y los de los impares por otro,
# pero sin incluir el último dígito.

# Sumar el resultado de los pares y el de los impares y hallar el resto de la división por 10.
# Realizar la operación 10 menos ese resto y ese es el dígito de control.
# Si como resultado sale 10, entenderemos que el dígito de control es 0.
# Comprobar que el dígito de control que hemos calculado y el último dígito del código EAN coinciden

class EAN:
    valido = True
    tipoEAN = 0
    sumaPares = 0
    sumaImpares = 0

    def calcularValidezEAN(self , strNumEan, tipoEAN):
        digitoControl = strNumEan[tipoEAN-1: tipoEAN]
        print("EAN su digito de control extraido del numeroEAN facilitado es ", digitoControl)
        for valor in range(tipoEAN):
            try:
                parcial=int(strNumEan[valor-1: valor])
                print("Parcial:", valor+1, parcial)
                if parcial%2 == 0:
                    self.sumaPares += parcial
                else:
                    self.sumaImpares += parcial
            except ValueError:
                print("Error al calcular el parcial")


        if tipoEAN == 8:
            # Si el código es EAN8, es la suma de los impares la que se multiplica por 3.
            self.sumaImpares *=  3
        else:
            # Si el código es EAN13, multiplicar la suma de los pares por 3.
            self.sumaPares *= 3
            digitoControl = strNumEan[12:13]
            print("EAN13 su gigito de control es ", digitoControl)

        sumaParesImpares = self.sumaImpares+self.sumaPares
        print("La suma de los dígitos pares es ", self.sumaPares)
        print("La suma de los digitos impares es ", self.sumaImpares)
        print("La suma de los digitos pares e impares es ", sumaParesImpares)
        resto= sumaParesImpares % 10
        valor= 10-resto
        if valor == 10:
            digitoControlCalculado = 0
            print(f"El dígito de control calculado es {digitoControlCalculado}")
        else:
            digitoControlCalculado = valor
            print(f"El dígito de control calculado es {digitoControlCalculado}")

        if digitoControlCalculado == int(digitoControl):
            return True
        else:
            return False

