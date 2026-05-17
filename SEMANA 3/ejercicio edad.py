def calcular_edad(anio_nacimiento):
    anio_actual = 2026
    edad = anio_actual - anio_nacimiento
    return f"Tienen {edad} años."

mi_edad = calcular_edad(1988)
print (mi_edad)

import math

def calcular_area_circulo (radio):
    return math.pi * math.pow(radio, 2)
    area = math.pi * (radio ** 2)
    return area
radio_usuario = 5
resultado = calcular_area_circulo(radio_usuario)
print(f"El área del circulo con radio es: {radio_usuario} ")
