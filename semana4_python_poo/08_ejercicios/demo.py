



class Dispositivo:
    def __init__(self, ip, mac, color):
        self.ip = ip
        self.mac = mac
        self.color = color

    def reportar(self):
        print(f"IP: {self.ip}, MAC: {self.mac}, Color: {self.color}")

#Crear el objeto a usarlo:
#d= Dispositivo("172.16.31.10", "AA.BB.CC", "azul")
#d.reportar()



class ImpresoraRed:
    def __init__(self, ip, modelo):
        self.ip = ip
        self.modelo = modelo
        self.paginas_impresas = 0

    def imprimir(self, cantidad):
        self.paginas_impresas += cantidad

    def reportar(self):
        print(f"IP: {self.ip}, Modelo: {self.modelo}, Paginas impresas: {self.paginas_impresas}")

imp = ImpresoraRed("172.16.31.10", "HP_LaserJet")
imp.imprimir(2)
imp.imprimir(12)
imp.reportar()