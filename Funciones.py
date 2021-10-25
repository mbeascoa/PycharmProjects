# En Python podemos crear funciones utilizando la palabra reservada “def” seguido del
# nombre la función.  Las funciones se pueden crear en cualquier lugar de un programa.
#Imaginemos que en muchos bloques de código necesitamos añadir IVA a los precios de
# nuestros productos. Lo ideal sería crear una función par no repetir ese código en varios puntos.
#En el siguiente ejemplo crearemos una función donde pediremos el precio de un producto
# y añadiremos el 21% de Iva al precio introducido.

def calcularIVA():
    importe = int(input("Precio del producto: "))
    total = importe* 1.21
    print (f"IVA incluido (21%): {total}")
    return

print("LLAMANDO A LA FUNCIÓN")
calcularIVA()


#Funciones con parámetros
#Podemos incluir parámetros en la definición de un método. Si se incluyen más de uno deben ir separados por coma.
#Def NombreFuncion (parametro1)
# Def NombreFuncion (parametro1, parametro2)
# Vamos a modificar el ejemplo del cálculo del IVA para que reciba el importe del producto como parámetro.

def calcularIVA(importe):
    print (f"Precio del producto: {importe}")
    total = importe* 1.21
    print (f"IVA incluido (21%): {total}")


print("LLAMANDO A LA FUNCIÓN")
calcularIVA(600)

# Funciones que retorna valor
# Si la función no retorna ningún valor (como los ejemplos anteriores) no es necesario poner la palabra reserva return.
# Si será necesario incluir la palabra reservada return en los casos en los que la función tenga que devolver un valor.
# Modificamos el ejemplo del cálculo de IVA para que retorne el importe con IVA.

def calcularIVA(importe):
    print (f"Precio del producto: {importe}")
    total = importe* 1.21
    return total


print("LLAMANDO A LA FUNCIÓN")
result=calcularIVA(1000)
print(f"IVA incluido (21%): {result}")


#Se puede retornar más de un valor separado por coma.
def calcularIVA(importe):
    total = importe* 1.21
    return importe,total


print("LLAMANDO A LA FUNCIÓN")
precio,result=calcularIVA(2000)

print(f"Precio del producto: {precio}")
print(f"IVA incluido (21%): {result}")
