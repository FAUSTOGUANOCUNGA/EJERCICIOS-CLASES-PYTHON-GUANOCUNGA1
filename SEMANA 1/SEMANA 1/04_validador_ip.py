# ============================================================
# EJERCICIO 4 — Mini-validador de dirección IP
# Semana 1 — Combinando input() y print() con lógica simple
# ============================================================
#
# OBJETIVO:
#   Leer una dirección IP del usuario, intentar resolverla
#   a un nombre de host y mostrar el resultado.
#
# CONTEXTO DE RED:
#   Resolver una IP a un nombre (DNS reverso) es algo que se
#   hace todos los días en administración de redes y forense
#   digital. Python lo hace en UNA línea con socket.
#
# NOTA: Aún no hemos visto if/else formalmente — eso es
#       Semana 3. Aquí solo usamos lo que ya presentamos hoy
#       (input, print, f-strings, módulos).
#
# CÓMO EJECUTARLO:
#   Clic derecho → "Run Python File in Terminal"
# ============================================================

import socket

print("=" * 45)
print("   MINI-RESOLUTOR DE DIRECCIÓN IP")
print("=" * 45)

ip_ingresada = input("Ingresa una dirección IP (ej: 8.8.8.8): ")

print(f"\nConsultando {ip_ingresada}...")

try:
    # gethostbyaddr hace DNS reverso: de IP a nombre
    info = socket.gethostbyaddr(ip_ingresada)
    nombre_host = info[0]
    print(f"Nombre del host: {nombre_host}")
except socket.herror:
    print("No se pudo resolver el nombre (la IP no tiene DNS reverso).")
except socket.gaierror:
    print("Dirección IP inválida o sin conexión a internet.")

print("=" * 45)

# ============================================================
# PRUEBA CON ESTAS IPs:
#   8.8.8.8          → DNS público de Google
#   1.1.1.1          → DNS público de Cloudflare
#   200.107.60.10    → Servidor típico de Ecuador (CNT)
#   192.168.1.1      → Probablemente tu router (no tiene DNS reverso)
# ============================================================
