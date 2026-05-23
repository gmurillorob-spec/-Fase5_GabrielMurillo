# Nombre del estudiante: Gabriel Murillo Robayo
# Grupo: 213022_316
# Programa: Ingenieria de Sistemas
# Curso: Fundamentos de Programacion
# Fase 5 - Evaluacion Final POA
# Problema 2: Promocion de precios en menu de restaurante


# Matriz con el menu del restaurante
# Cada fila tiene: nombre, categoria, precio base
menu = [
    ["Pizza Margarita", "Comida", 35000],
    ["Lasagna de carne", "Comida", 42000],
    ["Hamburguesa", "Comida", 28000],
    ["Jugo de mora", "Bebida", 8000],
    ["Limonada de coco", "Bebida", 12000],
    ["Brownie con helado", "Postre", 15000],
    ["Cheesecake", "Postre", 18000]
]

# Variables
categoria_objetivo = "Comida"
umbral_precio = 30000
descuento = 0.15


def calcular_precio_final(producto):
    # Si la categoria coincide y el precio base es mayor al umbral,
    # le aplica el descuento, si no se queda con el precio normal.
    categoria = producto[1]
    precio_base = producto[2]

    if categoria == categoria_objetivo and precio_base > umbral_precio:
        rebaja = precio_base * descuento
        precio_final = precio_base - rebaja
    else:
        precio_final = precio_base

    return precio_final


# Programa principal
print("Menu del restaurante - Promocion")
print("Categoria en promocion: " + categoria_objetivo)
print("Aplica 15% de descuento si el precio base es mayor a $" + str(umbral_precio))
print("")

for producto in menu:
    nombre = producto[0]
    precio_base = producto[2]
    precio_final = calcular_precio_final(producto)

    if precio_final < precio_base:
        estado = "Con descuento"
    else:
        estado = "Sin descuento"

    print("Producto: " + nombre)
    print("  Precio base:  $" + str(precio_base))
    print("  Precio final: $" + str(int(precio_final)) + "  (" + estado + ")")
    print("")
