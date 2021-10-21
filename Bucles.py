print("--------------BUCLE WHILE-------------")
# se pone {con la variable dentro} pero antes se pone una f""
i = 1
while i <= 10:
    print(f"El valor de i es :{i}")
    i += 1

print("--------------BUCLE WHILE-------------")

i = 1
while i <= 10:
    print(f"El valor de i es :{i}")
    i += 1
    if i == 3:
        break


print("--------------BUCLE WHILE-------------")

i = 1
while i <= 10:
    i += 1
    if i == 3:
        continue
    print(f"El valor de i es :{i}")


