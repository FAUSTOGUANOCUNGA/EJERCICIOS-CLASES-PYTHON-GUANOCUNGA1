# ============================================================================
# EJERCICIOS DE LISTAS Y DICCIONARIOS - SEMANA 2
# ============================================================================
# Este archivo contiene ejemplos y ejercicios prácticos sobre:
# - Listas (arrays)
# - Diccionarios (objetos/mapas)
# - Acceso a elementos
# - Operaciones básicas
# ============================================================================

print("=" * 70)
print("PARTE 1: CREACIÓN DE LISTAS")
print("=" * 70)

# Una lista es una colección ordenada de elementos
# Se define con corchetes [ ]
lista_frutas = ["MANZANA", "PERA", "NARANJA", "BANANA"]
lista_bebidas = ["COCACOLA", "PEPSI", "AGUA"]

print("\n✓ Lista de frutas:", lista_frutas)
print("✓ Lista de bebidas:", lista_bebidas)
print(f"✓ Total de frutas: {len(lista_frutas)}")
print(f"✓ Total de bebidas: {len(lista_bebidas)}")

# ============================================================================
print("\n" + "=" * 70)
print("PARTE 2: ACCESO A ELEMENTOS POR ÍNDICE")
print("=" * 70)
# En Python, el índice comienza en 0
# lista[0] = primer elemento
# lista[1] = segundo elemento
# lista[-1] = último elemento

print("\n✓ Primera fruta (índice 0):", lista_frutas[0])
print("✓ Segunda fruta (índice 1):", lista_frutas[1])
print("✓ Tercera fruta (índice 2):", lista_frutas[2])
print("✓ Última fruta (índice -1):", lista_frutas[-1])

# ============================================================================
print("\n" + "=" * 70)
print("PARTE 3: DICCIONARIOS (Pares clave-valor)")
print("=" * 70)

# Un diccionario almacena datos como pares clave: valor
# Se define con llaves { }
diccionario = {
    "FRUTAS": lista_frutas,
    "BEBIDAS": lista_bebidas,
    "Total de categorías": 2,
    "País de origen": "España"
}

print("\n✓ Diccionario completo:", diccionario)
print("\n✓ Acceso a 'FRUTAS':", diccionario['FRUTAS'])
print("✓ Acceso a 'BEBIDAS':", diccionario['BEBIDAS'])
print("✓ Valor numérico:", diccionario['Total de categorías'])
print("✓ País:", diccionario['País de origen'])

# ============================================================================
print("\n" + "=" * 70)
print("PARTE 4: LISTA DE LISTAS (Matriz)")
print("=" * 70)

lista_de_listas = [lista_frutas, lista_bebidas]
print("\n✓ Lista de listas:", lista_de_listas)
print("✓ Primera sublista:", lista_de_listas[0])
print("✓ Segunda sublista:", lista_de_listas[1])
print("✓ Elemento [0][3] (4ta fruta):", lista_de_listas[0][3])
print("✓ Elemento [1][1] (2da bebida):", lista_de_listas[1][1])

# ============================================================================
print("\n" + "=" * 70)
print("PARTE 5: OPERACIONES CON LISTAS")
print("=" * 70)

# Agregar elementos
lista_ejemplo = ["A", "B", "C"]
print(f"\n✓ Lista original: {lista_ejemplo}")
lista_ejemplo.append("D")
print(f"✓ Después de append('D'): {lista_ejemplo}")

# Insertar en una posición específica
lista_ejemplo.insert(1, "X")
print(f"✓ Después de insert(1, 'X'): {lista_ejemplo}")

# Eliminar un elemento
lista_ejemplo.remove("X")
print(f"✓ Después de remove('X'): {lista_ejemplo}")

# Contar elementos
print(f"✓ Cantidad de 'A': {lista_ejemplo.count('A')}")

# Ordenar
lista_numeros = [5, 2, 8, 1, 9]
print(f"\n✓ Lista desordenada: {lista_numeros}")
lista_numeros_ordenada = sorted(lista_numeros)
print(f"✓ Lista ordenada: {lista_numeros_ordenada}")

# ============================================================================
print("\n" + "=" * 70)
print("PARTE 6: RECORRER LISTAS")
print("=" * 70)

print("\n✓ Recorriendo frutas con FOR:")
for fruta in lista_frutas:
    print(f"   - {fruta}")

print("\n✓ Recorriendo con índice:")
for i in range(len(lista_frutas)):
    print(f"   Posición {i}: {lista_frutas[i]}")

# ============================================================================
print("\n" + "=" * 70)
print("EJERCICIOS PARA PRACTICAR EN CASA")
print("=" * 70)

print("""
EJERCICIO 1: Crea una lista llamada 'colores' con 4 colores diferentes
y imprime el segundo color.

EJERCICIO 2: Crea un diccionario con la información de tu persona favorita:
- nombre
- edad
- profesión
- país

EJERCICIO 3: Usa list_frutas y agrega 2 frutas más usando append()

EJERCICIO 4: Crea una lista de números del 1 al 10 y calcula la suma

EJERCICIO 5: Crea una matriz (lista de listas) 3x3 con números 
del 1 al 9 e imprime la diagonal principal

EJERCICIO 6: Recorre el diccionario e imprime cada clave y su valor
(Pista: usa .items())

EJERCICIO 7: Crea una lista de estudiantes y asigna una calificación
a cada uno usando un diccionario

¡Intenta resolver estos ejercicios y guarda tus soluciones!
""")
