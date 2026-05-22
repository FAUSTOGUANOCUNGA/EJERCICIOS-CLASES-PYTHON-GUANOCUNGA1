# Ejercicio 8: Filtrar IPs de la lista negra (uso de continue)

# 1. Datos iniciales provistos por el ejercicio
ips_log = ["10.0.0.5", "200.0.0.1", "10.0.0.8", "45.33.32.156", "10.0.0.10"]
blacklist = ["200.0.0.1", "45.33.32.156"]

# Pista: Inicializar un contador en 0 antes del bucle for
total = 0

# 2. Recorremos la lista de IPs
for ip in ips_log:

    # Pista: Si la IP está en la lista negra, usamos continue para saltarla
    if ip in blacklist:
        continue  # Salta el resto del código y va a la siguiente IP

    # Si la IP NO está en la lista negra, el código sigue de largo y la procesa:
    print(f"Procesando: {ip}")

    # Incrementamos el contador solo para las IPs aceptadas
    total += 1

# 3. Al final del bucle, imprimimos el total de IPs procesadas
print(f"Total procesadas: {total}")