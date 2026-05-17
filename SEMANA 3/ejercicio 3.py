def funcion1():...
    try :
        valor_1 = input("Introduce un numero: ")
        valor_2 = input("Introduce otro numero: ")
        total = int(valor_1) + (valor_2)
    except Exception as e:
        total = 0
    return total


total_general_1 = funcion1()
total_general_2 = funcion1()
total_general_3 = total_general_1 + total_general_2()
print(f"Resultado total: {total_general_3})


import math
def calcular_area_circulo(radio):
    area = math.pi * (radio ** 2)
    return area
radio_usuario = 5
resultado = calcular_area_circulo(radio_usuario)
print(f"El área del circulo con radio: {radio_usuario} es")


def calcular_edad(anio_nacimiento):
    anio_actual = 2026
    edad = anio_actual - anio_nacimiento
    return f"Tienen {edad} años."

mi_edad = calcular_edad(1988)
print (mi_edad)
