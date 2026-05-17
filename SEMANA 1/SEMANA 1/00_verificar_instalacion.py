# ============================================================
# EJERCICIO 0 — Verificación de instalación
# Semana 1 — Lenguaje de Programación Python
# Carrera: Infraestructura de Redes y Ciberseguridad
# ============================================================
#
# OBJETIVO:
#   Confirmar que Python 3 está correctamente instalado y que
#   VS Code puede ejecutar archivos .py.
#
# CÓMO EJECUTARLO:
#   1. Abre este archivo en VS Code.
#   2. Clic derecho sobre el editor → "Run Python File in Terminal".
#      (o en la terminal: python 00_verificar_instalacion.py)
#
# RESULTADO ESPERADO:
#   Debe imprimirse la versión de Python y un mensaje de éxito.
#   Si ves Python 3.13.x (o similar), todo está correcto.
# ============================================================

import sys

print("Verificando tu instalación de Python...")
print("-" * 45)
print(f"Versión de Python: {sys.version.split()[0]}")
print(f"Sistema operativo: {sys.platform}")
print("-" * 45)
print("¡Tu entorno está listo para el ciclo 2026-1!")