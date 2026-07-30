class ImpresoraRed:
    def __init__(self, ip, modelo):
        # Atributos iniciales de la impresora
        self.ip = ip
        self.modelo = modelo
        self.paginas_impresoras = 0
        self.limite_impresion = 5

    def imprimir(self, paginas):
        # Validación opcional para el reto EXTRA: evitar números negativos
        try:
            if paginas > 0:
                self.paginas_impresoras += paginas
                if self.paginas_impresoras >= self.limite_impresion:
                    print("limite de impresion alcanzado, por favor recargue papel")
            else:
                raise NameError("Cantidad no valida")
        except Exception as e:
            print(e)

    def reportar(self):
        print(f"Modelo: {self.modelo}, IP: {self.ip}, Paginas: {self.paginas_impresoras}")


imp = ImpresoraRed("10.0.0.50", "HP-LaserJet")
imp.imprimir(3)
imp.imprimir(1)
imp.reportar()

# Prueba del reto EXTRA:
# imp.imprimir(-3)