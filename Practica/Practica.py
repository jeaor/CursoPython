msg="""
    Bienvenido al Sistema de Productos
    1. Suma
    2. Creacion de Listado De Productos
    3. Agregar un nuevo producto
    4. Mostrar el producto de precio mas bajo
    5. Salir
"""

# productos=[
#     {
#         "nombre":"jabon",
#         "precio": 2.50
#     }
# ]

"PREGUNTA 1"
def suma(a,b):
    return a + b

"PREGUNTA 2"
prod = []
def crear_listado_productos():
    p = int(input("Indique cuantos productos desea agregar: "))
    for i in range(p):
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        prod.append({"nombre":nombre,"precio":precio})
    return prod

"PREGUNTA 3"
def agregar_producto(nombre,precio):
    prod.append({"nombre":nombre,"precio":precio})
    return prod

"PREGUNTA 4"
def producto_mas_bajo():
    if not prod:
        return None
    producto_bajo = prod[0]
    for producto in prod:
        if producto['precio'] < producto_bajo['precio']:
            producto_bajo = producto
    return producto_bajo



while True:
    print(msg)
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        a = float(input("Ingrese cualquier numero: "))
        b = float(input("Ingrese cualquier numero: "))
        print(f"La suma es: {suma(a,b)}")
        pass
    elif opcion == 2:
        crear_listado_productos()
        pass
    elif opcion == 3:
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        agregar_producto(nombre,precio)
        pass
    elif opcion == 4:
        producto_bajo = producto_mas_bajo()
        if producto_bajo:
            print(f"El producto de precio mas bajo es: {producto_bajo}")
        else:
            print("No hay productos en la lista.")
        pass
    elif opcion == 5:
        print("Cerrando el sistema...")
        break
    else:
        print("Opcion no valida")