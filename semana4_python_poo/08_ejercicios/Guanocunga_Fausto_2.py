class Router:

    def __init__(self, ip, modelo):

        self.ip = ip
        self.modelo = modelo
        self.rutas_configuradas = 0

    def agregar_ruta(self, cantidad):
        self.rutas_configuradas += cantidad

    def reportar(self):
        print(f"IP: {self.ip}, Modelo: {self.modelo}, Rutas: {self.rutas_configuradas}")



# 1. Crear el objeto router con IP y Modelo
mi_router = Router("192.168.1.1", "Cisco-2960")

# 2. Agregar rutas según las instrucciones
mi_router.agregar_ruta(2)
mi_router.agregar_ruta(4)
mi_router.agregar_ruta(1)

# 3. Mostrar el reporte en consola
mi_router.reportar()