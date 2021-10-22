#NUMERO FIBONACCI

dondeQuieresLlegar= int(input("Cuantas secuencias de numero Fibonacci quieres sacar?"))
print("Has dicho que quieres sacar hasta la serie ", dondeQuieresLlegar)
strResultado=""
parcial=1
cero=0
for i in range(0, dondeQuieresLlegar):
    if i==0 :
        anterioranterior=0
        anterior=1
        strResultado = strResultado + str(anterior+anterioranterior) + " , "
    elif i==1:
        anterioranterior = 0
        anterior = 1
        strResultado =strResultado +  str(anterior+anterioranterior) + " , "
        anterioranterior=1

    elif i!=0 or i!=1:

        actual= anterior+anterioranterior
        anterioranterior= anterior
        anterior=actual


        print(f" {anterior}")
        strResultado =strResultado +  str(actual) + " , "
print(strResultado)