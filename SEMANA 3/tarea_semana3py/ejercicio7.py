# Ejercicio 7: Primer puerto cerrado (uso de break)

# 1. Datos iniciales provistos por el ejercicio
puertos = [21, 22, 23, 25, 80]
estados = ["abierto", "abierto", "abierto", "cerrado", "abierto"]

# 2. Pista: Usamos zip(puertos, estados) para recorrer ambas listas en paralelo
for puerto, estado in zip(puertos, estados):

    # Si el estado es "cerrado", imprimimos el mensaje especial y rompemos el bucle
    if estado == "cerrado":
        print(f"Primer puerto cerrado: {puerto}")
        break  # Sale del bucle for inmediatamente

    # Si no es cerrado (es decir, está abierto), imprime de forma normal
    else:
        print(f"Puerto {puerto}: {estado}")