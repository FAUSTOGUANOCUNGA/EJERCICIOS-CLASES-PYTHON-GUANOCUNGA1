class Impresora:
    def __init__(self, ip, modelo):
        self.ip = ip
        self.modelo = modelo
        self.paginas_impresas =  0

    def imprimir(self, cantidad):
        if cantidad > 0:
            self.paginas_impresas += cantidad
        else:
            print("Error: La cantidad de páginas a imprimir debe ser mayor a 0. ")

        def reportar(self):
            print(f"IP: {self.ip},")
            print(f"Modelo: {self.modelo},")
            print(f"Paginas: {self.paginas_impresas},")

    if __name__ == "__main__":
    imp = Impresora("10.0.0.50", "HP-LaserJef")
    imp.imprimir(3)
    imp.imprimir(5)
    imp.imprimir(5)

    print("-" * 20)
