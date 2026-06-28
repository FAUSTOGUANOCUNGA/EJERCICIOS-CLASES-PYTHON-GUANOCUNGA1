
def validar_ip(ip: str) -> bool:
    partes = ip.split(".")
    if len(partes) != 4:
        return False
    for parte in partes:
        if not parte.isdigit():
            return False
        numero = int(parte)
        if numero < 0 or numero > 255:
            return False
    return True


class Dispositivo:
    def __init__(self, nombre: str, ip: str, estado: str = "apagado"):
        self.nombre = nombre
        self.ip = ip
        self.estado = estado

    def encender(self):
        self.estado = "encendido"

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"IP: {self.ip}")
        print(f"Estado: {self.estado}")


# Ejemplo de uso
if __name__ == "__main__":
    # Crear dispositivo
    dispositivo1 = Dispositivo("Router Principal", "192.168.1.1")
    dispositivo1.encender()
    dispositivo1.mostrar_info()

    # Probar función de validación de IP
    ip_valida = "192.168.0.100"
    ip_invalida = "300.168.1.1"

    print(f"¿{ip_valida} es válida?: {validar_ip(ip_valida)}")
    print(f"¿{ip_invalida} es válida?: {validar_ip(ip_invalida)}")

