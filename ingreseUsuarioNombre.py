nombres = []
nombre = ""
while nombre.lower() != "fin":
    nombre = input("Ingrese un nombre de persona (o 'fin' para terminar): ")
    if nombre.lower() != "fin":
        nombres.append(nombre)

print("Nombres ingresados:")
for nombre in nombres:
    print(nombre)
