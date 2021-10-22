dimensionArray=int(input("Cuántos valores quieres introducir en el array ? "))
array = []
for i in range(dimensionArray):
    x = int(input('valores: '))
array.append(x)
ordered_array = array.sort()
print(ordered_array)
print(array)
if array==ordered_array:
    print("Ordenado")
else:
    print("Sin ordenar")