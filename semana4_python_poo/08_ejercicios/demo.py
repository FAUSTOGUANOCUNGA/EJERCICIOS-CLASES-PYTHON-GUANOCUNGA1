



class Dispositivo:
    def __init__(self, ip, mac, color):
        self.ip = ip
        self.mac = mac
        self.color = color

    def reportar(self):
        print(f"IP: {self.ip}, MAC: {self.mac}, Color: {self.color}")

#Crear el objeto a usarlo:
d= Dispositivo("172.16.31.10", "AA.BB.CC", "azul")
d.reportar()
