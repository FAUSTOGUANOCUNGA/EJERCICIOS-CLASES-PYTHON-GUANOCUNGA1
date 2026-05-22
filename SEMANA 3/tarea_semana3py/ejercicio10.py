# Ejercicio 10: Validador de dirección IPv4 (integrador)

# Lista con todas las IPs de la salida esperada para probarlas juntas
ips_a_probar = [
    "192.168.1.1",
    "10.0.0.255",
    "256.1.1.1",
    "192.168.1",
    "192.168.a.1"
]

# Recorremos cada IP de la lista de pruebas
for ip in ips_a_probar:
    # Paso 1: Separar la IP por sus puntos
    partes = ip.split(".")

    valida = True
    motivo = ""  # Variable para guardar el porqué es inválida

    # Paso 2: Verificar si faltan o sobran octetos
    if len(partes) != 4:
        valida = False
        motivo = " (faltan octetos)"
    else:
        # Paso 3: Validar cada octeto individualmente
        for octeto in partes:
            # Verificar si no es un número entero positivo
            if not octeto.isdigit():
                valida = False
                motivo = " (no numerico)"
                break  # Rompe el bucle de los octetos si encuentra texto

            # Verificar si está fuera del rango 0 a 255
            else:
                numero = int(octeto)
                if numero < 0 or numero > 255:
                    valida = False
                    motivo = " (octeto fuera de rango)"
                    break  # Rompe el bucle si se pasa del rango

    # Imprimir el resultado final con el formato exacto de la salida esperada
    if valida:
        print(f"{ip:<15} -> Valida")
    else:
        print(f"{ip:<15} -> Invalida{motivo}")