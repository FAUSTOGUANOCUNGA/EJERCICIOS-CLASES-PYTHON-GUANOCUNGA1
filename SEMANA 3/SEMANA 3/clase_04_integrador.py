# =============================================================================
#  CLASE - INTEGRADOR (condicionales + bucles + controles)
#
#  Cada ejercicio esta dentro de su propia funcion. main() los llama en
#  orden. Comente las llamadas que NO vaya a ejecutar en clase.
# =============================================================================


# =============================================================================
#  NOTA DIDACTICA
# =============================================================================
#  Estos ejercicios COMBINAN todo lo visto en la semana:
#     - Condicionales (if / elif / else, operadores logicos)
#     - Bucle for (con range, enumerate, sobre cadenas)
#     - Bucle while (validacion)
#     - Controles finos (break, continue, return temprano)
#
#  Son ejemplos realistas de redes y ciberseguridad. Aunque las funciones
#  formales se ven en la Unidad 2, aqui se introducen porque permiten
#  encapsular logica reutilizable.
# =============================================================================


def validar_ip(ip):
    """Devuelve True si 'ip' es una IPv4 valida (0-255 en cada octeto)."""
    # COMBINA: condicionales + for + return temprano (similar a break).
    partes = ip.split(".")

    if len(partes) != 4:
        return False

    for octeto in partes:
        if not octeto.isdigit():
            return False
        valor = int(octeto)
        if valor < 0 or valor > 255:
            return False

    return True


def ejercicio_5_1():
    """Validador de IPv4 - condicionales + for + funcion."""
    print("\n--- Ejercicio 5.1: Validador de IPv4 ---")
    # OBSERVACION: La funcion validar_ip() encapsula la logica. El bucle
    # principal solo se preocupa de mostrar los resultados.

    direcciones = [
        "192.168.1.1",     # valida
        "10.0.0.255",      # valida
        "256.1.1.1",       # invalida (256 > 255)
        "192.168.1",       # invalida (solo 3 partes)
        "192.168.a.1",     # invalida (letra)
        "0.0.0.0",         # valida
    ]

    for direccion in direcciones:
        if validar_ip(direccion):
            print(f"  [OK]    {direccion}")
        else:
            print(f"  [ERROR] {direccion}")

    # DIDACTICA: Note como "return False" dentro de validar_ip cumple el
    # mismo rol que un break: detiene la ejecucion en cuanto se sabe que
    # la IP es invalida.


def ejercicio_5_2():
    """Analizador de logs - for + condicionales + contadores."""
    print("\n--- Ejercicio 5.2: Analizador de logs ---")
    # OBSERVACION: Recorrer logs y extraer eventos importantes es tarea
    # diaria en ciberseguridad. Combinamos for + if/elif + contadores.

    logs = [
        "INFO  2026-05-04 08:00 inicio del servicio",
        "ERROR 2026-05-04 08:15 fallo de autenticacion de admin",
        "INFO  2026-05-04 08:20 conexion aceptada de 192.168.1.10",
        "ERROR 2026-05-04 08:25 fallo de autenticacion de root",
        "WARN  2026-05-04 08:30 uso elevado de CPU",
        "ERROR 2026-05-04 08:45 acceso denegado a 200.0.0.5",
        "INFO  2026-05-04 09:00 backup completado",
    ]

    errores = 0
    warnings = 0

    print("\nEventos criticos detectados:")
    for linea in logs:
        if linea.startswith("ERROR"):
            print(f"  [E] {linea}")
            errores += 1
        elif linea.startswith("WARN"):
            print(f"  [W] {linea}")
            warnings += 1
        # Los INFO se ignoran (no hay rama para ellos)

    print(f"\nResumen: {errores} errores, {warnings} advertencias")

    # TECNICA: .startswith() devuelve True si la cadena empieza por el
    # texto indicado. Es ideal para filtrar lineas de log por severidad.


def evaluar_contrasena(clave):
    """Devuelve un nivel de fortaleza segun los caracteres que contenga."""
    tiene_mayus  = False
    tiene_minus  = False
    tiene_num    = False
    tiene_simb   = False
    simbolos = "!@#$%^&*()_-+=[]{};:,.<>?/|"

    for c in clave:
        if c.isupper():
            tiene_mayus = True
        elif c.islower():
            tiene_minus = True
        elif c.isdigit():
            tiene_num = True
        elif c in simbolos:
            tiene_simb = True

    if len(clave) < 8:
        return "DEBIL (menos de 8 caracteres)"
    elif tiene_mayus and tiene_minus and tiene_num and tiene_simb:
        return "FUERTE"
    elif tiene_mayus and tiene_minus and tiene_num:
        return "MEDIA (falta un simbolo)"
    else:
        return "DEBIL (faltan tipos de caracteres)"


def ejercicio_5_3():
    """Fortaleza de contrasena - for sobre cadena + logica combinada."""
    print("\n--- Ejercicio 5.3: Fortaleza de contrasena ---")
    # OBSERVACION: Integra for sobre cadena, condicionales multiples y
    # operadores logicos. Aplicable a politicas de contrasena reales.

    pruebas = [
        "abc123",
        "abcdefgh",
        "Abcdefg1",
        "Abcdefg1!",
        "P@ssw0rd2026",
    ]

    for clave in pruebas:
        nivel = evaluar_contrasena(clave)
        print(f"  '{clave:<15}' -> {nivel}")

    # CIERRE: Este ejercicio integra TODOS los temas de la semana.
    # Buen punto de conexion con la Unidad 2 (funciones formales).


# =============================================================================
#  MAIN
# =============================================================================
def main():
    print("=" * 60)
    print("CLASE - SEMANA 3 - PARTE 4: INTEGRADOR")
    print("=" * 60)

    ejercicio_5_1()
    ejercicio_5_2()
    ejercicio_5_3()

    print("\n" + "=" * 60)
    print("FIN DE LOS EJERCICIOS DE LA SEMANA 3")
    print("Tema: Estructuras condicionales y bucles")
    print("=" * 60)

    # RECORDATORIO:
    # - La indentacion en Python es OBLIGATORIA, no decorativa.
    # - Use 4 espacios por nivel (nunca mezcle tabs y espacios).
    # - Los dos puntos ":" al final de if, for y while son obligatorios.
    # - Para el TAU1 deberan aplicar estos conceptos en un ejercicio
    #   integrador. Revisar instrucciones en Moodle.


if __name__ == "__main__":
    main()
