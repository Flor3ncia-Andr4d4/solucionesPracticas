agenda = {}

while True:
    print("Menú de opciones:")
    print("1. Agregar una persona")
    print("2. Modificar una persona")
    print("3. Eliminar una persona")
    print("4. Mostrar toda la agenda")
    print("5. Salir")
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        dni = input("Ingrese el DNI de la persona: ")
        nombre = input("Ingrese el nombre de la persona: ")
        telefono = input("Ingrese el teléfono de la persona: ")
        agenda[dni] = {"nombre": nombre, "telefono": telefono}
        print("Persona agregada.")

    elif opcion == "2":
        dni = input("Ingrese el DNI de la persona a modificar: ")
        if dni in agenda:
            nombre = input("Ingrese el nuevo nombre: ")
            telefono = input("Ingrese el nuevo teléfono: ")
            agenda[dni] = {"nombre": nombre, "telefono": telefono}
            print("Persona modificada.")
        else:
            print("DNI no encontrado.")

    elif opcion == "3":
        dni = input("Ingrese el DNI de la persona a eliminar: ")
        if dni in agenda:
            del agenda[dni]
            print("Persona eliminada.")
        else:
            print("DNI no encontrado.")

    elif opcion == "4":
        for dni, datos in agenda.items():
            print(f"DNI: {dni}")
            print(f"Nombre: {datos['nombre']}")
            print(f"Teléfono: {datos['telefono']}")
            print("----------")

    elif opcion == "5":
        print("Saliendo...")
        break

    else:
        print("Opción no válida.")
