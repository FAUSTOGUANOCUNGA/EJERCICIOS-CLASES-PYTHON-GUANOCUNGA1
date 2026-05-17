# ============================================================
# EJERCICIO 3 — Información del sistema
# Semana 1 — Exploración del módulo 'platform' y 'sys'
# ============================================================
#
# OBJETIVO:
#   Obtener información detallada del equipo donde corre este
#   script. Este es el primer paso de cualquier script de
#   reconocimiento en ciberseguridad.
#
# CONCEPTOS:
#   - Varios imports en un mismo archivo
#   - Uso de funciones de módulos estándar
#   - Presentación ordenada de datos
#
# CÓMO EJECUTARLO:
#   Clic derecho → "Run Python File in Terminal"
# ============================================================

import sys
import platform
import os

print("=" * 50)
print("     RECONOCIMIENTO BÁSICO DEL EQUIPO")
print("=" * 50)

# Datos del sistema operativo
print(f"Sistema operativo: {platform.system()}")
print(f"Versión del SO:    {platform.release()}")
print(f"Arquitectura:      {platform.machine()}")
print(f"Procesador:        {platform.processor()}")

print("-" * 50)

# Datos de Python
print(f"Python:            {sys.version.split()[0]}")
print(f"Ejecutable:        {sys.executable}")

print("-" * 50)

# Datos del usuario
# Nota: usamos getenv() en lugar de getlogin() porque es más robusto
# en distintos entornos (Windows, Linux, Mac, VS Code, terminales SSH, etc.)
usuario = os.getenv("USER") or os.getenv("USERNAME") or "desconocido"
print(f"Usuario actual:    {usuario}")
print(f"Directorio actual: {os.getcwd()}")

print("=" * 50)

# ============================================================
# REFLEXIÓN PARA EL ESTUDIANTE:
#   Un atacante que logra ejecutar un script así en un equipo
#   remoto ya tiene información valiosa: sistema operativo,
#   versión, usuario. Esto se llama "fingerprinting".
#   Por eso la primera línea de defensa es NO ejecutar scripts
#   de fuentes desconocidas.
# ============================================================
