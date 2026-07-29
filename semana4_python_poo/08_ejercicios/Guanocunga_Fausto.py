class ImpresoraRed:
    def __init__(self, ip, modelo):
        # Atributos iniciales de la impresora
        self.ip = ip
        self.modelo = modelo
        self.paginas_impresas = 0  # Inicializa en 0 según las instrucciones

    def imprimir(self, cantidad):
        # Validación opcional para el reto EXTRA: evitar números negativos
        if cantidad > 0:
            self.paginas_impresas += cantidad
        else:
            print("Error: La cantidad de páginas a imprimir debe ser mayor a 0.")

    def reportar(self):
        # Muestra la información acumulada de la impresora
        print(f"IP: {self.ip}")
        print(f"Modelo: {self.modelo}")
        print(f"Paginas: {self.paginas_impresas}")


# --- PRUEBAS ---
imp = ImpresoraRed("10.0.0.50", "HP-LaserJet")
imp.imprimir(3)
imp.imprimir(5)
imp.reportar()

# Prueba del reto EXTRA:
# imp.imprimir(-3)