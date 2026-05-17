# =============================================================================
#  PRACTICA - BUCLE WHILE
#
#  Cada ejercicio es una funcion con un  "# TODO: ..."  donde debe escribir
#  su codigo. Comente la llamada en main() para ejercicios no terminados.
#
#  REGLA DE ORO: la variable de control del while DEBE cambiar dentro del
#  bucle, o queda infinito (Ctrl+C para abortar).
# =============================================================================


def ejercicio_4_1():
    """Cuenta regresiva de apagado (5 -> 1)."""
    # PISTA: variable que decrementa con  -= 1.
    print("\n--- Ejercicio 4.1: Cuenta regresiva ---")

    # TODO: complete el codigo aqui

    # SALIDA ESPERADA:
    # Apagado en: 5
    # Apagado en: 4
    # Apagado en: 3
    # Apagado en: 2
    # Apagado en: 1
    # Apagando servidor...


def ejercicio_4_2():
    """Decremento de bateria IoT (15% por hora)."""
    # DESCRIPCION:
    #   Empieza con bateria = 100. Cada hora baja 15%. Mientras siga
    #   >= 20 imprima "Hora N: bateria al X%". Cuando baje del 20%,
    #   imprima la alerta.
    # PISTA: dos variables (bateria, hora). while bateria >= 20.
    print("\n--- Ejercicio 4.2: Bateria IoT ---")

    # TODO: complete el codigo aqui

    # SALIDA ESPERADA:
    # Hora 0: bateria al 100%
    # Hora 1: bateria al 85%
    # Hora 2: bateria al 70%
    # Hora 3: bateria al 55%
    # Hora 4: bateria al 40%
    # Hora 5: bateria al 25%
    # ALERTA: bateria por debajo del umbral. Cargar dispositivo.


def ejercicio_4_3():
    """Contar pings consecutivos exitosos hasta el primer fallo."""
    # DESCRIPCION:
    #   Recorra la lista con un INDICE (mientras respuestas[i] == 1).
    #   Cuente cuantos exitosos llevamos. Al primer 0, salga.
    #   Si fueron >= 5 -> "Host estable", sino "Host inestable".
    print("\n--- Ejercicio 4.3: Pings consecutivos ---")

    respuestas = [1, 1, 1, 1, 1, 1, 0, 1, 1, 0]   # 6 exitosos, luego fallo

    # TODO: complete el codigo aqui

    # SALIDA ESPERADA:
    # Pings consecutivos exitosos: 6
    # Host estable (al menos 5 pings exitosos seguidos)
    #
    # Si la lista empezara con [1, 1, 0, ...], la salida seria:
    # Pings consecutivos exitosos: 2
    # Host inestable


def ejercicio_4_4():
    """Espera de respuesta con timeout (intentos maximos)."""
    # DESCRIPCION:
    #   while (intento < intentos_max) AND (no se haya recibido respuesta).
    #   En el intento numero "intento_con_respuesta" se recibe respuesta
    #   (cambie el valor para probar).
    # PISTA: use bandera respuesta_recibida = False.
    print("\n--- Ejercicio 4.4: Espera con timeout ---")

    intentos_max = 6
    intento_con_respuesta = 4

    # TODO: complete el codigo aqui

    # SALIDA ESPERADA:
    # Intento 1: sin respuesta
    # Intento 2: sin respuesta
    # Intento 3: sin respuesta
    # Intento 4: RESPUESTA RECIBIDA
    # Conexion exitosa en el intento 4


# =============================================================================
#  AUTOEVALUACION
# =============================================================================
#  Marque con una X los que pudo completar SIN ayuda:
#     [_] 4.1   [_] 4.2   [_] 4.3   [_] 4.4
# =============================================================================


# =============================================================================
#  MAIN
# =============================================================================
def main():
    print("=" * 60)
    print("PRACTICA - SEMANA 3 - PARTE 3: BUCLE WHILE")
    print("=" * 60)

    ejercicio_4_1()
    ejercicio_4_2()
    ejercicio_4_3()
    ejercicio_4_4()

    print("\n" + "=" * 60)
    print("FIN PRACTICA 3 - Continuar con: practica_04_integrador.py")
    print("=" * 60)


if __name__ == "__main__":
    main()
