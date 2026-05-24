# 1. Crear la matriz (lista de listas) con al menos 6 productos
# Cada fila: [Nombre del Producto, Categoría, Precio Base]
menu = [
    ["Pizza Margarita", "Plato Principal", 25000],
    ["Ensalada César", "Entrada", 18000],
    ["Brownie con Helado", "Postre", 12000],
    ["Lasaña Boloñesa", "Plato Principal", 32000],
    ["Jugo Natural", "Bebida", 8000],
    ["Tarta de Limón", "Postre", 15000]
]

# 2. Definir parámetros de la promoción
categoria_objetivo = "Postre"       # Categoría que recibirá descuento
umbral_precio = 13000               # Precio mínimo para aplicar descuento
descuento = 0.15                    # 15% de descuento

# 3. Función módulo para calcular precio final de un producto
def calcular_precio_final(producto, categoria_obj, umbral, tasa_dcto):
    """
    Recibe un producto (lista con [nombre, categoria, precio_base])
    Aplica 15% descuento si categoría es objetivo y precio_base > umbral.
    Retorna el precio final (float).
    """
    # Extraer datos del producto
    nombre = producto[0]          # Nombre (no se usa en cálculo pero se puede mostrar)
    categoria = producto[1]       # Categoría del producto
    precio_base = producto[2]     # Precio base

    # Verificar condiciones: misma categoría Y precio base mayor al umbral
    if categoria == categoria_obj and precio_base > umbral:
        precio_final = precio_base * (1 - tasa_dcto)   # Aplicar descuento
    else:
        precio_final = precio_base                     # Mantener precio base

    return precio_final

# 4. Procesar y mostrar cada producto con precios
print("=== RESULTADOS DE PROMOCIÓN ===")
print("Promoción: ", descuento*100, "% descuento en categoría '", categoria_objetivo, "'")
print("Condición: precio base > $", format(umbral_precio, ",.0f"), "\n")

# Recorrer toda la matriz del menú
for producto in menu:
    # Obtener nombre y precio base
    nombre = producto[0]
    precio_base = producto[2]

    # Calcular precio final llamando a la función
    # Pasamos los parámetros correctos: producto, categoría objetivo, umbral y descuento
    precio_final = calcular_precio_final(producto, categoria_objetivo, umbral_precio, descuento)

    # Mostrar resultado formateado
    print("Producto: ", nombre)
    print("  Precio base: $", format(precio_base, ",.0f"))
    print("  Precio final: $", format(precio_final, ",.0f"))
    print("-" * 30)
