# Ejercicio 3: Listar IPs de una subred (bucle for con range)

# range(8) genera números automáticamente desde el 0 hasta el 7 (8 números en total)
for i in range(8):
    # Usamos un f-string para incrustar el valor de 'i' al final de la IP
    print(f"192.168.1.{i}")