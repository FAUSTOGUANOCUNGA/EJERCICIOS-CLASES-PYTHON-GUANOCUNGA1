

from encapsulamiento import CuentaSinProtegida

class CuentaSinProteccion:
    """Esta clase NO usa encapsulamiento. Cualquiera puede romperla."""

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

# OBSERVACION: cualquiera puede cambiar el saldo sin control.
print("=== Sin encapsulamiento ===")
cuenta = CuentaSinProteccion("Hector", 500)
cuenta.saldo = -10000          # esto es legal y es un PROBLEMA
print(f"Saldo: {cuenta.saldo}") # -10000 (un saldo negativo absurdo)

# OBSERVACION DIDACTICA: en la vida real, un saldo bancario nunca puede ser
# tan negativo. Hay que poner limites.

