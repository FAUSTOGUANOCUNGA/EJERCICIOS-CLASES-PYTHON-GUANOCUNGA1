# 1. Definimos la variable con el protocolo que queremos probar
# Puedes cambiar este valor para probar diferentes casos (ej. "Telnet", "FTP", "Bitcoin")
protocolo = "HTTPS"
protocolo = "Telnet"


# 2. Evaluamos si el protocolo es seguro
if protocolo == "HTTPS" or protocolo == "SSH" or protocolo == "SFTP":
    print(f"El protocolo {protocolo} es SEGURO")

# 3. Evaluamos si el protocolo es inseguro
elif protocolo == "HTTP" or protocolo == "Telnet" or protocolo == "FTP":
    print(f"El protocolo {protocolo} es INSEGURO")

# 4. Si no está en ninguna de las listas anteriores
else:
    print("Desconocido")