# ============================================================
# EJERCICIO 1 — Hola, Red Segura
# Semana 1 — Ejercicio clave de la clase (Diapositiva 13)
# ============================================================
#
# OBJETIVO:
#   Escribir tu primer script profesional en Python.
#   Saluda al usuario, muestra la versión de Python y obtiene
#   la IP local del equipo.
#
# CONCEPTOS QUE USAMOS:
#   - import (traer módulos)
#   - print() (mostrar texto)
#   - input() (leer del usuario)
#   - f-strings (combinar texto y variables)
#   - socket.gethostname() y socket.gethostbyname() (info de red)
#
# CÓMO EJECUTARLO:
#   Clic derecho → "Run Python File in Terminal"
# ============================================================

import sys
import socket

# --- Bienvenida ---
print("=" * 45)
print("   BIENVENIDO A LA RED SEGURA CON PYTHON")
print("=" * 45)

nombre = input("¿Cuál es tu nombre, analista? ")

# --- Información del sistema ---
version_python = sys.version.split()[0]
nombre_host = socket.gethostname()

# socket.gethostbyname puede fallar en redes corporativas.
# Por eso lo envolvemos en try/except (lo veremos a fondo más adelante).
try:
    ip_local = socket.gethostbyname(nombre_host)
except socket.gaierror:
    ip_local = "127.0.0.1"  # fallback local si la red no resuelve el hostname

# --- Salida personalizada ---
print(f"\nHola, {nombre}!")
print(f"Estás corriendo Python {version_python}")
print(f"Tu equipo se llama: {nombre_host}")
print(f"Tu IP local es:    {ip_local}")
print("\n¡Listo para automatizar la red!")
