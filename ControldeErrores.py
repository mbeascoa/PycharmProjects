

#Nos dice claramente que no puede convertir una cadena (Hola) a entero.
# Tenemos que fijarnos en el nombre de la excepción que se ha producido (ValueError)
#     • Para que nuestro código sea totalmente correcto tenemos que tratar el error,
#       mostraremos un mensaje al usuario para avisarle de lo sucedido.

import sys


def controlErroresDIV():
    try:
        dividendo = int(input("Introduce dividendo:"))
        divisor = int(input("Introduce divisor:"))
        resultado = dividendo / divisor
        print(f"Resultado división: {resultado}")
    except ValueError:
        print("Error, debes introducir un número")
        controlErroresDIV()
    # except ZeroDivisionError:
        print("¡¡¡Error!!!. El divisor no puede ser cero")
        controlErroresDIV()
    except :
        print(f"¡¡¡Error General tipo de error {sys.exc_info()}")
    finally:
        print("ENTRA")

controlErroresDIV()

