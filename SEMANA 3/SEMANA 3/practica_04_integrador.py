# =============================================================================
#  PRACTICA - INTEGRADOR (condicionales + bucles + controles)
#
#  Cada ejercicio es una funcion con un  "# TODO: ..."  donde debe escribir
#  su codigo. Comente la llamada en main() para ejercicios no terminados.
# =============================================================================


def ejercicio_5_1():
    """Reporte de uso de ancho de banda (total, hora pico, horas > 100 MB)."""
    # DESCRIPCION:
    #   1. Calcular el total de MB del dia (sumar todos).
    #   2. Encontrar la hora pico (la de mayor consumo).
    #   3. Contar cuantas horas superaron 100 MB.
    # PISTA: for con enumerate. Para la hora pico, mantenga max_mb y
    #        hora_pico, y actualicelas si encuentra un valor mayor.
    print("\n--- Ejercicio 5.1: Ancho de banda ---")

    mb_por_hora = [
        20,  15,  18,  10,   5,   8,   # horas 0-5
        25,  60, 120, 150, 180, 200,   # horas 6-11
        195, 175, 140, 110,  95,  85,  # horas 12-17
       130, 145, 110,  70,  40,  25,   # horas 18-23
    ]

    # TODO: complete el codigo aqui
    # total_mb = ...
    # max_mb = ...
    # hora_pico = ...
    # horas_sobre_100 = ...

    # SALIDA ESPERADA:
    # Total del dia:        2234 MB
    # Hora pico:            11:00 con 200 MB
    # Horas con > 100 MB:   12


def ejercicio_5_2():
    """Verificador de fortaleza de contrasena (simple)."""
    # DESCRIPCION:
    #   Verifique que la contrasena cumpla TODAS:
    #     - longitud >= 8
    #     - al menos una mayuscula
    #     - al menos un numero
    #   Imprima "Contrasena valida" o "Contrasena debil: <motivo>".
    # PISTA: for sobre la cadena; dos boolean (tiene_mayus, tiene_numero);
    #        len(contrasena) para la longitud.
    print("\n--- Ejercicio 5.2: Fortaleza contrasena ---")

    contrasena = "Ister2026"   # pruebe tambien con "abc", "abcdefgh", "AbCdEfGh"

    # TODO: complete el codigo aqui

    # SALIDA ESPERADA con contrasena = "Ister2026":
    # Contrasena valida
    #
    # SALIDA ESPERADA con contrasena = "abc":
    # Contrasena debil: longitud insuficiente
    #
    # SALIDA ESPERADA con contrasena = "abcdefgh":
    # Contrasena debil: falta mayuscula o numero


def ejercicio_5_3():
    """Mini-escaner de hosts activos (red /29)."""
    # DESCRIPCION:
    #   1. Imprima cada IP con su estado (activo/inactivo).
    #   2. Cuente activos e inactivos.
    #   3. Calcule el porcentaje de activos.
    #   4. Si activos < 50%, imprima "ALERTA: red degradada".
    # PISTA: for con enumerate, condicionales y contadores.
    print("\n--- Ejercicio 5.3: Escaner de hosts ---")

    # Resultados simulados de ping a 192.168.1.0 hasta 192.168.1.7
    # 1 = activo, 0 = inactivo
    resultado_ping = [1, 1, 0, 1, 0, 0, 1, 0]

    # TODO: complete el codigo aqui

    # SALIDA ESPERADA:
    # 192.168.1.0: activo
    # 192.168.1.1: activo
    # 192.168.1.2: inactivo
    # 192.168.1.3: activo
    # 192.168.1.4: inactivo
    # 192.168.1.5: inactivo
    # 192.168.1.6: activo
    # 192.168.1.7: inactivo
    #
    # Hosts activos:   4 de 8 (50.0%)
    # Hosts inactivos: 4 de 8


# =============================================================================
#  AUTOEVALUACION GENERAL
# =============================================================================
#  Marque con una X los que pudo completar SIN ayuda en TODA la practica:
#
#  Parte 1 - Condicionales:   [_] 1.1 [_] 1.2 [_] 1.3 [_] 1.4 [_] 1.5
#  Parte 2 - Bucle for:       [_] 2.1 [_] 2.2 [_] 2.3 [_] 2.4 [_] 2.5
#  Parte 2 - Controles:       [_] break [_] continue [_] else [_] pass
#  Parte 3 - Bucle while:     [_] 4.1 [_] 4.2 [_] 4.3 [_] 4.4
#  Parte 4 - Integradores:    [_] 5.1 [_] 5.2 [_] 5.3
#
#  GUIA DE INTERPRETACION:
#  - 18 o mas resueltos: Excelente. Listo para el TAU1.
#  - 14 a 17 resueltos:  Bien. Revise los ejercicios donde dudo.
#  - 10 a 13 resueltos:  Regular. Vuelva a estudiar el material de clase.
#  - Menos de 10:        Insuficiente. Solicite tutoria al docente ANTES
#                        de empezar el TAU1.
# =============================================================================


# =============================================================================
#  MAIN
# =============================================================================
def main():
    print("=" * 60)
    print("PRACTICA - SEMANA 3 - PARTE 4: INTEGRADOR")
    print("=" * 60)

    ejercicio_5_1()
    ejercicio_5_2()
    ejercicio_5_3()

    print("\n" + "=" * 60)
    print("FIN DE LA PRACTICA - SEMANA 3")
    print("Tema: Estructuras condicionales y bucles")
    print("=" * 60)
    print()
    print("Recuerde: ahora puede empezar el TAU1 con mas confianza.")
    print("Fecha de entrega del TAU1: 17 de mayo de 2026")


if __name__ == "__main__":
    main()
