# 1. Definimos la variable puerto (puedes cambiar este número para probar)
puerto = 443

# 2. Estructura if / elif / else para asignar el servicio
if puerto == 22:
    servicio = "SSH"
elif puerto == 80:
    servicio = "HTTP"
elif puerto == 443:
    servicio = "HTTPS"
elif puerto == 3306:
    servicio = "MySQL"
elif puerto == 3389:
    servicio = "RDP"
else:
    servicio = "Servicio desconocido"

# 3. Imprimimos el resultado final usando la variable 'servicio'
print(f"Puerto {puerto}: {servicio}")