"""
Estudiante:  Fausto Guanocunga
Fecha:       30/06/2026
Asignatura:  Lenguaje de Programacion Python
Proposito:   Sistema de inventario de dispositivos de red aplicando POO y 5 tipos de funciones.
Declaración de Apoyo: Utilice IA para corregir errores.
"""


# ---------------------------------------------------------------
# TIPO 1: FUNCION SUELTA  (fuera de cualquier clase)
# ---------------------------------------------------------------
def imprimir_banner():
    print("=" * 48)
    print("SISTEMA DE INVENTARIO DE DISPOSITIVOS DE RED")
    print("=" * 48)

# ---------------------------------------------------------------
# CLASE PRINCIPAL
# ---------------------------------------------------------------
class Dispositivo:

    def __init__(self, ip, modelo, ubicacion):
        self.modelo = modelo
        self.ubicacion = ubicacion
        self.ip = ip

# TIPO 3: @property (con validacion)

    @property
    def ip(self):
        return self._ip

    @ip.setter
    def ip(self, valor):

        partes = valor.split('.')

        if len(partes) != 4:
            raise ValueError(f"IP invalida: {valor}")

        for parte in partes:
            if not parte.isdigit() or not (0 <= int(parte) <= 255):
                raise ValueError(f"IP invalida: {valor}")

        self._ip = valor

    # TIPO 2: METODO NORMAL  (con self)
    def reportar(self):
        print(f"\nDispositivo: {self.ip}")
        print(f"Modelo:      {self.modelo}")
        print(f"Ubicacion:   {self.ubicacion}")

    # TIPO 4: @staticmethod  (sin self, sin cls)
    @staticmethod
    def es_ip_privada(ip):
        if ip.startswith('10.'):
            return True
        if ip.startswith('192.168.'):
            return True

        if ip.startswith('172.'):
            partes = ip.split('.')
            if len(partes) >= 2 and partes[1].isdigit():
                segundo_octeto = int(partes[1])
                if 16 <= segundo_octeto <= 31:
                    return True

        return False

    # TIPO 5: @classmethod  (constructor alternativo)
    @classmethod
    def desde_csv(cls, linea):
        ip, modelo, ubicacion = linea.split(',')

        ip = ip.strip()
        modelo = modelo.strip()
        ubicacion = ubicacion.strip()

        return cls(ip, modelo, ubicacion)


# ---------------------------------------------------------------
# PROGRAMA PRINCIPAL  (pruebas)
# ---------------------------------------------------------------
if __name__ == "__main__":
    imprimir_banner()

    dispositivo1 = Dispositivo('10.0.0.1', 'Cisco-2960', 'DC-A')

    dispositivo2 = Dispositivo.desde_csv('192.168.1.1, MikroTik, Oficina')

    dispositivo1.reportar()
    dispositivo2.reportar()

    print()

    ip_prueba1 = '10.0.0.5'
    ip_prueba2 = '8.8.8.8'
    print(f"{ip_prueba1:<10} es privada?  {Dispositivo.es_ip_privada(ip_prueba1)}")
    print(f"{ip_prueba2:<10} es privada?  {Dispositivo.es_ip_privada(ip_prueba2)}")

    print()

    try:
        dispositivo_malo = Dispositivo('999.0.0.1', 'X', 'Y')
    except ValueError as e:
        print('Error capturado:', e)