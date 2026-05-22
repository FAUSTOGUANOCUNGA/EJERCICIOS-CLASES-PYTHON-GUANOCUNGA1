# Ejercicio 6: Reintento de conexión (while con condición compuesta)

# Pista 1: Inicializar las dos variables antes del bucle
intento = 1
conectado = False

# Pista 2: Condición compuesta (mientras no pasemos los 5 intentos Y no estemos conectados)
while intento <= 5 and not conectado:

    # Pista 3: Suponer que se conecta de forma exitosa exactamente en el intento 3
    if intento == 3:
        conectado = True
        print(f"Intento {intento}: CONECTADO")
    else:
        # Si no es el intento 3, la conexión falla
        print(f"Intento {intento}: sin respuesta")

    # IMPORTANTE: Incrementamos el contador de intentos en cada vuelta
    intento += 1