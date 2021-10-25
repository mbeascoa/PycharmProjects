provincias = dict()

provincias = {
    924: "Badajoz",
    956: "Cádiz",
    958: "Granada",
    959: "Huelva",
    91: "Madrid",
    95: "Málaga",
    968: "Murcia",
    923: "Salamanca",
    954: "Sevilla",
    922: "Sta. Cruz de Tenerife",
    975: "Soria",
    96: "Valencia",
    976: "Zaragoza"
}
print(provincias)

# El método get permite obtener el valor de la clave que pasemos como parámetro.

dato = provincias.get(91)
print(dato)

#items
# Obtiene una lista de tuplas formadas por los pares clave:valor.
# Podemos recorrer todos los elementos con un bucle for.

for clave, valor in provincias.items():
    print("Prefijo: ", clave, "Provincia: ", valor)

# len Devuelve el número de elementos que tiene el diccionario.

print("Número de provincias:",len(provincias))
print("------------------------------------------")

# Podemos recuperar solo las claves(keys()) o solo los valores(values()).
for claves in provincias.keys():
    print("Prefijo: ", claves)
print("----------------------------------------------------------")
for valores in provincias.values():
    print("Provincia: ", valores)

# SetDefault Inserta un elemento en el diccionario clave:valor. Si la clave existe no lo inserta
print("----------------------------------------------------------")
provincias.setdefault(925, "Toledo")
print(provincias)
print("----------------------------------------------------------")
# Si la clave existe no lo insertará
provincias.setdefault(91, "Toledo")
print(provincias)

# clear Eliminar todos los elementos del diccionario.
print("----------------------------------------------------------")
provincias.clear()
print(provincias)

# pop  Elimina un elemento del diccionario.

provincias = dict()

provincias = {
    924: "Badajoz",
    956: "Cádiz",
    958: "Granada",
    959: "Huelva",
    91: "Madrid",
    95: "Málaga",
    968: "Murcia",
    923: "Salamanca",
    954: "Sevilla",
    922: "Sta. Cruz de Tenerife",
    975: "Soria",
    96: "Valencia",
    976: "Zaragoza"
}
provincias.pop(924)
print(provincias)

