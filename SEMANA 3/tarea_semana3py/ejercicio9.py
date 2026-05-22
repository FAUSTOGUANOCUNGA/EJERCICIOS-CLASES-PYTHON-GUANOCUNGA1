# Ejercicio 9: Buscar dispositivo en inventario (else en bucle)

# 1. Datos iniciales provistos por el ejercicio
inventario = ["Router-01", "Switch-A", "Firewall-FW1", "Servidor-Web"]

# Puedes cambiar este valor por "Switch-Z" para probar el segundo caso
buscar = "Switch-Z"

# 2. Recorremos el inventario
for d in inventario:
    if d == buscar:
        print("Encontrado")
        break  # Rompe el bucle de inmediato porque ya lo encontramos

# 3. Pista: El else debe estar al mismo nivel de alineación que el 'for'
else:
    # Este bloque solo se ejecuta si el bucle for recorrió TODO sin encontrar un 'break'
    print("No encontrado en el inventario")