# =============================================================================
#  CLASE - CONDICIONALES (if / elif / else)
#
#  Cada ejercicio esta dentro de su propia funcion. main() los llama en
#  orden. Comente las llamadas que NO vaya a ejecutar en clase.
# =============================================================================


# =============================================================================
#  NOTA TEORICA RAPIDA - ESTRUCTURAS CONDICIONALES
# =============================================================================
#  if   <condicion>: ......  un solo camino
#  if / else        ......  dos caminos posibles
#  if / elif / else ......  varios caminos (se ejecuta SOLO la primera coincidencia)
#
#  Operadores logicos:
#     and  ->  todas las condiciones deben ser verdaderas
#     or   ->  basta con UNA condicion verdadera
#     not  ->  invierte el valor de verdad
#
#  Importante:
#     - Los dos puntos ":" al final son OBLIGATORIOS.
#     - La indentacion es 4 espacios (no decorativa, es sintactica).
#     - Evaluacion en corto circuito: en "and" si la primera es False, las
#       demas no se evaluan (util para condiciones seguras).
# =============================================================================


def ejercicio_1_1():
    """If simple - una sola condicion, sin else."""
    print("\n--- Ejercicio 1.1: Puerto seguro ---")
    # OBSERVACION: El if mas simple posible. Si la condicion es verdadera,
    # ejecuta el bloque indentado. Si es falsa, no hace nada.

    puerto = int(input("Ingrese el puerto del servicio: "))

    if puerto == 22:
        print("Servicio detectado: SSH (acceso remoto cifrado)")
    elif puerto == 80:
        print("Servicio detectado: HTTP (navegacion web sin cifrado)")
    elif puerto == 443:
        print("Servicio detectado: HTTPS (navegacion web cifrada)")
    else:
        print("Servicio desconocido o no seguro")
    # CIERRE: Cambie el valor de "puerto" a 80 y vuelva a correr. No hay
    # rama "else", el programa continua sin imprimir nada.


def ejercicio_1_2():
    """If / else - dos caminos, solo uno se ejecuta."""
    print("\n--- Ejercicio 1.2: Control de intentos ---")
    # OBSERVACION: "if/else" garantiza que SIEMPRE se ejecuta exactamente
    # una de las dos ramas, nunca las dos, nunca ninguna.

    intentos_fallidos = 5
    limite = 3

    if intentos_fallidos < limite:
        print(f"Acceso permitido. Intentos: {intentos_fallidos}/{limite}")
    else:
        print(f"CUENTA BLOQUEADA. Se excedieron los {limite} intentos.")

    # DIDACTICA: Pregunte que pasa si intentos_fallidos == 3.
    # Como el operador es "<" estricto, 3 NO es menor que 3 -> entra al else.


def ejercicio_1_3():
    """If / elif / else - varios caminos."""
    print("\n--- Ejercicio 1.3: Identificar servicio ---")
    # OBSERVACION: Python evalua de arriba hacia abajo y se queda con la
    # PRIMERA condicion verdadera. El "else" final atrapa cualquier caso
    # que no haya coincidido.

    puerto = 443

    if puerto == 22:
        servicio = "SSH"
    elif puerto == 80:
        servicio = "HTTP"
    elif puerto == 443:
        servicio = "HTTPS"
    elif puerto == 3306:
        servicio = "MySQL"
    elif puerto == 3389:
        servicio = "RDP"
    else:
        servicio = "Desconocido"

    print(f"Puerto {puerto} corresponde a: {servicio}")

    # DIDACTICA: El orden de los elif importa. Si dos condiciones podrian
    # ser verdaderas a la vez, Python ejecuta SOLO la primera.


def ejercicio_1_4():
    """Operadores logicos - and / or / not."""
    print("\n--- Ejercicio 1.4: Validacion combinada ---")
    # OBSERVACION: Combinamos varias condiciones en un solo if.
    #   and -> todas verdaderas
    #   or  -> al menos una verdadera
    #   not -> invierte el valor

    usuario_activo = True
    tiene_permiso = True
    cuenta_bloqueada = True
    print(f"Usuario activo: {usuario_activo}, Tiene permiso: {tiene_permiso}, Cuenta bloqueada: {cuenta_bloqueada}")
    print("Validando acceso al sistema...")
    print(f"Si cuenta bloqueada es not {cuenta_bloqueada} == True")
    if usuario_activo and tiene_permiso and not cuenta_bloqueada:
        print("Acceso autorizado al sistema")
    else:
        print("Acceso denegado")

    # TECNICA: Corto circuito. En "and", si la primera es False ya no
    # se evaluan las demas. Ejemplo seguro:
    #     if usuario and usuario.activo:   # no falla si usuario es None


def ejercicio_1_5():
    """If anidado - un if dentro de otro if."""
    print("\n--- Ejercicio 1.5: Condicionales anidadas ---")
    # OBSERVACION: Un if puede contener otros if dentro. Cada nivel suma
    # 4 espacios mas de indentacion.

    ip_asignacion = "192.168.1.10"
    estado_host = "activo"

    if ip_asignacion.startswith("192.168."):
        print("Host esta en la LAN")

        if estado_host == "activo":
            print("  -> Operativo, se puede establecer conexion")
        else:
            print("  -> Inactivo, no responde")
    else:
        print("Host esta fuera de la LAN")

    # DIDACTICA: No abusar del anidamiento. A partir de 3 o 4 niveles,
    # conviene reorganizar el codigo (Unidad 2 - funciones).


# =============================================================================
#  MAIN - llamada de ejercicios
# =============================================================================
#  Para usar en clase: comente las llamadas que NO se vayan a ejecutar y
#  deje solo la del ejercicio que se va a explicar en ese momento.
# =============================================================================
print("=" * 60)
print("CLASE - SEMANA 3 - PARTE 1: CONDICIONALES")
print("=" * 60)

# ejercicio_1_1()
# ejercicio_1_2()
# ejercicio_1_3()
# ejercicio_1_4()
ejercicio_1_5()

# print("\n" + "=" * 60)
# print("FIN - Continuar con: clase_02_bucles_for.py")
# print("=" * 60)

