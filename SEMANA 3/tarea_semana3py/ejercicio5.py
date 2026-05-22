# Ejercicio 5: Cuenta regresiva de apagado (bucle while)

# Pista 1: Inicializar el contador en 5 antes del while
contador = 5

# Pista 2: Condición para que se detenga al llegar a 1
while contador >= 1:
    # Imprimimos el valor actual siguiendo el formato de la salida esperada
    print(f"Apagado en: {contador}")

    # Pista 3: Actualizamos la variable de control restándole 1
    contador -= 1  # Esto es lo mismo que: contador = contador - 1

# Mensaje final fuera del bucle (cuando el while termina)
print("Apagando servidor...")