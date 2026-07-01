"""
Estudiante:  [Tu Nombre Completo]
Fecha:       30/06/2026
Asignatura:  Lenguaje de Programacion Python
Proposito:   Sistema de inventario de dispositivos de red aplicando POO y 5 tipos de funciones.
Declaración de Apoyo: Código desarrollado con asistencia de IA para fines didácticos y refinamiento de lógica de validación.
"""


# ---------------------------------------------------------------
# TIPO 1: FUNCION SUELTA  (fuera de cualquier clase)
# ---------------------------------------------------------------
def imprimir_banner():
    """Imprime un titulo decorativo del sistema. Sin parametros, sin retorno."""
    print("=" * 48)
    print("SISTEMA DE INVENTARIO DE DISPOSITIVOS")
    print("=" * 48)


# ---------------------------------------------------------------
# CLASE PRINCIPAL
# ---------------------------------------------------------------
class Dispositivo:

    def __init__(self, ip, modelo, ubicacion):
        """Constructor de la clase."""
        self.modelo = modelo
        self.ubicacion = ubicacion
        # Usar self.ip llama al setter de forma automatica para validar la IP inicial
        self.ip = ip

        # TIPO 3: @property (con validacion)

    @property
    def ip(self):
        """Getter: Devuelve el valor protegido de la IP."""
        return self._ip

    @ip.setter
    def ip(self, valor):
        """Setter: Valida que la IP tenga formato correcto (4 octetos 0-255)."""
        # Dividimos la cadena por puntos
        partes = valor.split('.')

        # Validacion 1: Deben ser exactamente 4 octetos
        if len(partes) != 4:
            raise ValueError(f"IP invalida: {valor}")

        # Validacion 2: Cada octeto debe ser numerico y estar en el rango de 0 a 255
        for parte in partes:
            if not parte.isdigit() or not (0 <= int(parte) <= 255):
                raise ValueError(f"IP invalida: {valor}")

        # Si pasa todas las validaciones, se asigna al atributo interno protegido
        self._ip = valor

    # TIPO 2: METODO NORMAL  (con self)
    def reportar(self):
        """Imprime la IP, modelo y ubicacion en formato estructurado."""
        print(f"\nDispositivo: {self.ip}")
        print(f"Modelo:      {self.modelo}")
        print(f"Ubicacion:   {self.ubicacion}")

    # TIPO 4: @staticmethod  (sin self, sin cls)
    @staticmethod
    def es_ip_privada(ip):
        """Determina si una IP pertenece a los rangos privados RFC 1918."""
        # Validacion simple por prefijo
        if ip.startswith('10.'):
            return True
        if ip.startswith('192.168.'):
            return True

        # Validacion del rango 172.16.x.x a 172.31.x.x
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
        """Parsea una linea CSV, limpia espacios y devuelve una instancia de la clase."""
        # Dividimos la linea por comas y desempaquetamos los elementos
        ip, modelo, ubicacion = linea.split(',')

        # Limpiamos los espacios en blanco a los extremos usando strip()
        ip = ip.strip()
        modelo = modelo.strip()
        ubicacion = ubicacion.strip()

        # Retornamos la nueva instancia llamando a cls (que equivale a Dispositivo)
        return cls(ip, modelo, ubicacion)


# ---------------------------------------------------------------
# PROGRAMA PRINCIPAL  (pruebas obligatorias)
# ---------------------------------------------------------------
if __name__ == "__main__":
    # 1. Llamar a la funcion suelta
    imprimir_banner()

    # 2. Crear un Dispositivo de forma normal
    dispositivo1 = Dispositivo('10.0.0.1', 'Cisco-2960', 'DC-A')

    # 3. Crear otro Dispositivo usando el metodo de clase (CSV)
    dispositivo2 = Dispositivo.desde_csv('192.168.1.1, MikroTik, Oficina')

    # 4. Llamar al metodo reportar() en ambos dispositivos
    dispositivo1.reportar()
    dispositivo2.reportar()

    print()  # Salto de linea para ordenar la salida

    # 5. Probar el metodo estatico de validacion de IP privada
    ip_prueba1 = '10.0.0.5'
    ip_prueba2 = '8.8.8.8'
    print(f"{ip_prueba1:<10} es privada?  {Dispositivo.es_ip_privada(ip_prueba1)}")
    print(f"{ip_prueba2:<10} es privada?  {Dispositivo.es_ip_privada(ip_prueba2)}")

    print()  # Salto de linea

    # 6. Probar que la asignacion de una IP invalida lance la excepcion adecuada
    try:
        dispositivo_malo = Dispositivo('999.0.0.1', 'X', 'Y')
    except ValueError as e:
        print('Error capturado:', e)