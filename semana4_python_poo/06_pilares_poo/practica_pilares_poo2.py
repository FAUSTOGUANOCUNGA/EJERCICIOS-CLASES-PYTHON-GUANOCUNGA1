
from semana4_python_poo.06_pilares_poo import EscanerPuertos


class EscanerPuertos:
    """Escanea puertos de un host. Detalles ocultos al usuario."""

    def __init__(self, host):
        self.host = host
        # OBSERVACION: lista de puertos comunes (oculto al usuario).
        self._puertos_comunes = [22, 23, 80, 443, 3306, 3389]
        self._timeout = 2

    # OBSERVACION: metodo PRIVADO (empieza con _). Detalle interno.
    def _intentar_conectar(self, puerto):
        """Detalle interno: simula intentar conectar a un puerto."""
        # En produccion aqui iria socket.connect_ex(...)
        # Simulamos: el 22 y el 443 estan abiertos.
        return puerto in (22, 443)

    # OBSERVACION: metodo PRIVADO. Otro detalle interno.
    def _formatear_resultado(self, puerto, abierto):
        """Detalle interno: como mostrar cada resultado."""
        estado = "ABIERTO " if abierto else "cerrado"
        return f"  Puerto {puerto:5} - {estado}"

    # OBSERVACION: este es el UNICO metodo que el usuario necesita conocer.
    def escanear(self):
        """Metodo publico SIMPLE. El usuario solo llama esto."""
        print(f"Escaneando {self.host}...")
        abiertos = []
        for puerto in self._puertos_comunes:
            if self._intentar_conectar(puerto):
                abiertos.append(puerto)
                print(self._formatear_resultado(puerto, True))
            else:
                print(self._formatear_resultado(puerto, False))
        return abiertos


print("=== Escaner de puertos (abstraccion) ===")
escaner = EscanerPuertos("10.0.0.1")
# OBSERVACION: el usuario solo llama escanear(). No necesita saber nada mas.
resultado = escaner.escanear()
print(f"\nPuertos abiertos: {resultado}")

# OBSERVACION DIDACTICA: el usuario NO sabe (ni necesita saber):
#   - como se intenta conectar
#   - cuales son los puertos comunes
#   - como se formatea la salida
# Solo sabe: "llamo escanear() y obtengo los puertos abiertos".
