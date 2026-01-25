# import os
# class PropiedadInmobiliaria:
#     def __init__(self, name: str, address: str, dimensiones: str,
#                  withSize: float, heightSize: float, precioUnit: float):
#         self.name = name
#         self.address = address
#         self.dimensiones = dimensiones
#         self.withSize = withSize
#         self.heightSize = heightSize
#         self.precioUnit = precioUnit

#         self.enable = True
#         self.dimension = 0.0
#         self.precioPropiedad = 0.0

#     def getWith(self) -> float:
#         return float(self.dimensiones.split("*")[0])

#     def getHeight(self) -> float:
#         return float(self.dimensiones.split("*")[1])

#     def calcularDimensionesV1(self) -> float:
#         size = self.dimensiones.split("*")
#         return float(size[0]) * float(size[1])

#     def calcularDimensionesV2(self) -> float:
#         return self.withSize * self.heightSize

#     def calcularPrecioAprox(self):
#         self.dimension = self.calcularDimensionesV1()
#         self.precioPropiedad = self.precioUnit * self.dimension

#     def __str__(self):
#         disponibilidad = "Disponible" if self.enable else "No Disponible"
#         return (
#             f"{self.name} | {disponibilidad}\n"
#             f"Dirección: {self.address}\n"
#             f"Dimensiones: {self.dimensiones}\n"
#             f"Área total: {self.dimension:.2f} m2\n"
#             f"Precio aproximado: S/. {self.precioPropiedad:,.2f}\n"
#         )


# # ===== CREACIÓN DE PROPIEDADES =====
# pr1 = PropiedadInmobiliaria("Casa 1", "Calle 123", "10.1*20.0", 10.1, 20.0, 1500)
# pr2 = PropiedadInmobiliaria("Casa 2", "Calle 456", "6.8*20.0", 6.8, 20.0, 1500)
# pr3 = PropiedadInmobiliaria("Casa 3", "Calle 789", "10.1*18.0", 10.1, 18.0, 1500)
# pr4 = PropiedadInmobiliaria("Casa 4", "Av. Central", "9.5*22.0", 9.5, 22.0, 1500)
# pr5 = PropiedadInmobiliaria("Casa 5", "Jr. Lima", "8.0*15.0", 8.0, 15.0, 1500)

# listaProductos = [pr1, pr2, pr3, pr4, pr5]


# # ===== INMOBILIARIA =====
# class Inmobiliaria:
#     rutaReporte = "C://CURSO PYTHON//reporte.txt"
#     headers = ["Nombre", "Dirección", "Dimensiones", "Área", "Precio"]
#     def __init__(self, listaPropiedades: list[PropiedadInmobiliaria]):
#         self.listaProductos = listaPropiedades

#     def listarPropiedades(self):
#         for item in self.listaProductos:
#             item.calcularPrecioAprox()
#             print(item)
# #===========GENERAR REPORTE===========
#     def generarReporte(self):
#           with open(self.rutaReporte, mode='w', encoding="utf-8") as file:
#             # Escribir encabezado
#             file.write(",".join(self.headers) + "\n")

#             # Escribir datos
#             for item in self.listaProductos:
#                 item.calcularPrecioAprox()
#                 fila = (
#                     f"{item.name},"
#                     f"{item.address},"
#                     f"{item.dimensiones},"
#                     f"{item.dimension:.2f},"
#                     f"{item.precioPropiedad:.2f}\n"
#                 )
#                 file.write(fila)

# # ===== EJECUCIÓN =====
# inmobiliaria = Inmobiliaria(listaProductos)
# inmobiliaria.listarPropiedades()
# inmobiliaria.generarReporte()

# "abir rutas"
# ruta = "C://CURSO PYTHON//leer.txt"
# ruta2= "./leer.txt"
# with open(ruta2,mode='r') as file:
#     data = file.read()
#     print(data)

# "Añadir"
# with open("C://CURSO PYTHON//leer.txt",mode='a') as file:
#     file.write("\nHola Mundo")

# "para ver si el archivo existe"
# print(os.path.exists("C://CURSO PYTHON//leer.txt"))

# "para ver si el archivo es un archivo"
# print(os.path.isfile("C://CURSO PYTHON//leer.txt"))

# "para ver si el archivo es una carpeta"
# print(os.path.isdir("C://CURSO PYTHON//leer.txt"))

# "para ver si el archivo es un enlace simbolico"
# print(os.path.islink("C://CURSO PYTHON//leer.txt"))

    
