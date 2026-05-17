

def funcion1():
    try :
        valor_1 = input("Introduce un numero: ")
        valor_2 = input("Introduce otro numero: ")
        total = int(valor_1) + int(valor_2)
    except Exception as e:
        total = 0
    return total

total_general_1 = funcion1()
total_general_2 = funcion1()
total_general_3 = total_general_1 + total_general_2
print(f"Resultado total:{total_general_3}")



def calcular_edad():
    try :
        edad_1 = input("Introduce un numero: ")
        edad_2 = input("Introduce otro numero: ")
        total = int(edad_1) + int(edad_2)
    except Exception as e:
        total = 0
    return total

total_general_11 = calcular_edad()
total_general_22 = calcular_edad()
total_general_33 = total_general_11 + total_general_22
print(f"Resultado total:{total_general_33}")
