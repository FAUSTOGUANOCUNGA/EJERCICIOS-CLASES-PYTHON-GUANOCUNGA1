# 1. Datos iniciales (Lista de dispositivos de red)
# Puedes cambiar estos nombres por los que aparezcan completos en tu pantalla
dispositivos = ["Router Cisco", "Switch HP", "Firewall Fortinet", "Servidor Dell"]

# 2. Recorremos la lista usando enumerate configurado para iniciar en 1
for indice, dispositivo in enumerate(dispositivos, start=1):
    # Imprimimos el número y el nombre del dispositivo
    print(f"{indice}. {dispositivo}")