Algoritmo Mostrar_Nombres
    nombres = []
    nombre = ""

    Mientras nombre no sea "fin", hacer
        Escribir "Ingrese un nombre de persona (o 'fin' para terminar):"
        Leer nombre
        Si nombre no es "fin", entonces
            Agregar nombre a la lista nombres
        Fin Si
    Fin Mientras

    Escribir "Nombres ingresados:"
    Para cada nombre en nombres, hacer
        Escribir nombre
    Fin Para
Fin Algoritmo
