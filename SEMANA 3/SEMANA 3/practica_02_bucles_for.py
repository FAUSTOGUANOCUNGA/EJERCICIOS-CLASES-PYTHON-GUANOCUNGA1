# =============================================================================
#  PRACTICA - BUCLE FOR + CONTROLES
#
#  Cada ejercicio es una funcion con un  "# TODO: ..."  donde debe escribir
#  su codigo. Comente la llamada en main() para ejercicios no terminados.
#
#  Recordatorio - controles finos:
#     break    -> SALE del bucle.
#     continue -> SALTA al siguiente elemento.
#     pass     -> NO HACE NADA (placeholder).
#     else     -> se ejecuta si el bucle termino SIN break.
# =============================================================================


# =============================================================================
#  BLOQUE A - BUCLE FOR BASICO
# =============================================================================

def ejercicio_2_1():
    """Listar IPs de la subred 192.168.1.0/29 (8 direcciones)."""
    # PISTA: bucle for con range, f-string para construir cada IP.
    print("\n--- Ejercicio 2.1: IPs de una subred ---")

    # TODO: complete el codigo aqui

    # SALIDA ESPERADA:
    # 192.168.1.0
    # 192.168.1.1
    # 192.168.1.2
    # 192.168.1.3
    # 192.168.1.4
    # 192.168.1.5
    # 192.168.1.6
    # 192.168.1.7


def ejercicio_2_2():
    """Imprimir cada dispositivo con un guion delante."""
    # PISTA: recorra la lista con for y use un print con prefijo "  - ".
    print("\n--- Ejercicio 2.2: Inventario ---")

    dispositivos = [
        "Router Cisco 2901",
        "Switch HP ProCurve",
        "Firewall Fortinet",
        "Access Point Ubiquiti",
        "Servidor Dell PowerEdge",
    ]

    # TODO: complete el codigo aqui

    # SALIDA ESPERADA:
    #   - Router Cisco 2901
    #   - Switch HP ProCurve
    #   - Firewall Fortinet
    #   - Access Point Ubiquiti
    #   - Servidor Dell PowerEdge


def ejercicio_2_3():
    """Contar activos vs inactivos."""
    # PISTA: dos variables contador y un if dentro del for.
    print("\n--- Ejercicio 2.3: Estado de dispositivos ---")

    estados = ["activo", "activo", "inactivo", "activo", "inactivo",
               "activo", "activo", "inactivo", "activo", "activo"]

    # TODO: complete el codigo aqui

    # SALIDA ESPERADA:
    # Dispositivos activos:   7
    # Dispositivos inactivos: 3
    # Total:                  10


def ejercicio_2_4():
    """Listado numerado con enumerate (start=1)."""
    print("\n--- Ejercicio 2.4: Listado numerado ---")

    hosts = ["servidor-web", "servidor-bd", "servidor-mail", "servidor-dns"]

    # TODO: complete el codigo aqui

    # SALIDA ESPERADA:
    # Host 1: servidor-web
    # Host 2: servidor-bd
    # Host 3: servidor-mail
    # Host 4: servidor-dns


def ejercicio_2_5():
    """Emparejar IP con hostname usando zip."""
    print("\n--- Ejercicio 2.5: Tabla IP-Hostname ---")

    ips     = ["10.0.0.1",  "10.0.0.2",  "10.0.0.3",  "10.0.0.4"]
    nombres = ["gateway",   "dns",       "web",       "mail"]

    print("IP            Hostname")
    print("-" * 30)

    # TODO: complete el codigo aqui

    # SALIDA ESPERADA:
    # IP            Hostname
    # ------------------------------
    # 10.0.0.1      gateway
    # 10.0.0.2      dns
    # 10.0.0.3      web
    # 10.0.0.4      mail


# =============================================================================
#  BLOQUE B - CONTROLES FINOS DEL BUCLE
# =============================================================================

def ejercicio_3_1_break():
    """break: detenerse en el PRIMER puerto cerrado."""
    # PISTA: enumerate para tener numero del puerto + estado; break al
    # detectar el primer "cerrado".
    print("\n--- Ejercicio break: Primer puerto cerrado ---")

    puertos        = [21,         22,        23,        25,        80,        443]
    estado_puertos = ["abierto", "abierto", "abierto", "cerrado", "abierto", "abierto"]

    # TODO: complete el codigo aqui

    # SALIDA ESPERADA:
    # Puerto 21: abierto
    # Puerto 22: abierto
    # Puerto 23: abierto
    # Primer puerto cerrado encontrado: 25
    # (deteniendo escaneo)


def ejercicio_3_2_continue():
    """continue: saltar IPs de la blacklist."""
    # PISTA: "if ip in ips_blacklist: continue" justo al inicio del for.
    # Lleve dos contadores: procesadas y saltadas.
    print("\n--- Ejercicio continue: Filtrar blacklist ---")

    ips_log = ["10.0.0.5", "200.0.0.1", "10.0.0.8", "45.33.32.156",
               "10.0.0.9", "200.0.0.1", "10.0.0.10"]
    ips_blacklist = ["200.0.0.1", "45.33.32.156"]

    # TODO: complete el codigo aqui

    # SALIDA ESPERADA:
    # Procesando: 10.0.0.5
    # Procesando: 10.0.0.8
    # Procesando: 10.0.0.9
    # Procesando: 10.0.0.10
    #
    # IPs procesadas: 4
    # IPs saltadas:   3


def ejercicio_3_3_else():
    """else del for: reportar 'no encontrado' sin bandera auxiliar."""
    # PISTA: enumerate + break al encontrar, else despues del for.
    print("\n--- Ejercicio else: Buscar dispositivo ---")

    inventario = ["Router-01", "Switch-A", "Firewall-FW1",
                  "Switch-B", "Servidor-Web", "Access-Point-1"]

    buscar = "Firewall-FW1"   # pruebe tambien con "Switch-Z" (no existe)

    # TODO: complete el codigo aqui

    # SALIDA ESPERADA con buscar = "Firewall-FW1":
    # Encontrado en posicion 2: Firewall-FW1
    #
    # SALIDA ESPERADA con buscar = "Switch-Z":
    # No encontrado en el inventario


def ejercicio_3_4_pass():
    """pass: placeholder para usuarios que aun no procesaremos."""
    # PISTA: recorra los usuarios. Si el usuario es "root", use pass
    # (placeholder para futura auditoria). Para los demas, imprima
    # "Usuario procesado: <nombre>".
    print("\n--- Ejercicio pass: Placeholder ---")

    usuarios = ["admin", "invitado", "root", "soporte"]

    # TODO: complete el codigo aqui

    # SALIDA ESPERADA:
    # Usuario procesado: admin
    # Usuario procesado: invitado
    # Usuario procesado: soporte
    #
    # (note que "root" NO aparece - el pass no imprime nada)


# =============================================================================
#  AUTOEVALUACION
# =============================================================================
#  Marque con una X los que pudo completar SIN ayuda:
#     For basico:  [_] 2.1   [_] 2.2   [_] 2.3   [_] 2.4   [_] 2.5
#     Controles:   [_] break [_] continue [_] else [_] pass
# =============================================================================


# =============================================================================
#  MAIN
# =============================================================================
def main():
    print("=" * 60)
    print("PRACTICA - SEMANA 3 - PARTE 2: BUCLE FOR + CONTROLES")
    print("=" * 60)

    # For basico
    ejercicio_2_1()
    ejercicio_2_2()
    ejercicio_2_3()
    ejercicio_2_4()
    ejercicio_2_5()

    # Controles finos
    ejercicio_3_1_break()
    ejercicio_3_2_continue()
    ejercicio_3_3_else()
    ejercicio_3_4_pass()

    print("\n" + "=" * 60)
    print("FIN PRACTICA 2 - Continuar con: practica_03_bucles_while.py")
    print("=" * 60)


if __name__ == "__main__":
    main()
