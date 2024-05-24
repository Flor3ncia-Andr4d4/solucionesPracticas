Algoritmo Convertir_Pesos_a_Dolares
    // Definir la tasa de cambio del dólar
    tasa_cambio = valor de la tasa de cambio actual

    // Solicitar al usuario que ingrese el monto en pesos ARS
    Escribir "Ingrese el monto en pesos ARS:"
    Leer monto_ars
    
    // Calcular el equivalente en dólares USD
    monto_usd = monto_ars / tasa_cambio
    
    // Mostrar el resultado al usuario
    Escribir "El equivalente en dólares es:", monto_usd
Fin Algoritmo
