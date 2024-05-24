# Definir la tasa de cambio del dólar (valor simulado)
tasa_cambio = 0.015  # 1 ARS = 0.015 USD (ejemplo)

# Solicitar al usuario que ingrese el monto en pesos ARS
monto_ars = float(input("Ingrese el monto en pesos ARS: "))

# Calcular el equivalente en dólares USD
monto_usd = monto_ars * tasa_cambio

# Mostrar el resultado al usuario
print("El equivalente en dólares es:", monto_usd)
