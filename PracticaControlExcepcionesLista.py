premios= [1000000, 250000, 180000, 125000, 15000, 12000, 25000]
numero= int(input("Introduce el primer,segundo, tercer, cuarto, etc...del  premio "))
try :
    print(f"El valor del premio es {premios[numero]}")
except TypeError:
    print("No existe ese premio, elija otro orden")
finally:
    print("Gracias por participar")



