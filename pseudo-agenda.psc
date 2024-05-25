Algoritmo Agenda_Telefonica_Simple
    Crear un diccionario vacío llamado agenda

    Mientras siempre hacer
        Mostrar menú de opciones
        Leer opción

        Si la opción es 1 entonces
            Pedir DNI
            Pedir nombre
            Pedir teléfono
            Agregar a la persona al diccionario

        Sino si la opción es 2 entonces
            Pedir DNI
            Si el DNI está en la agenda entonces
                Pedir nuevo nombre
                Pedir nuevo teléfono
                Actualizar los datos en la agenda
            Sino
                Mostrar mensaje de error

        Sino si la opción es 3 entonces
            Pedir DNI
            Si el DNI está en la agenda entonces
                Eliminar a la persona de la agenda
            Sino
                Mostrar mensaje de error

        Sino si la opción es 4 entonces
            Mostrar todos los contactos de la agenda

        Sino si la opción es 5 entonces
            Salir del programa

        Sino
            Mostrar mensaje de opción no válida
        Fin Si
    Fin Mientras
Fin Algoritmo
