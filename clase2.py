# #mini proyecto inmobiliario
# "COLECCION DE DATOS"
# propertys= ["casa nr1 ","casa nr2","casa nr3","casa nr4"]
# direcciones = ("calle 1", "calle 2","calle 3","calle 4")

# countPropertys = len(propertys)

# #diccionario
# propertys_v2 = {
#     "propiedades": [
#         {
#          "id":1,   
#          "nombre":"casa blanca",
#          "direccion":("av. siempre viva","lima"),
#          "precio":12345,
#          "moneda": "USD",
#          "disponible": False
#         },
#         {
#          "id":2,
#          "nombre":"casa azul",
#          "direccion":("av. siempre","huacho"),
#          "precio":15854,
#          "moneda": "SOL",
#          "disponible": True
#         },
#     ]    
# }

# while True:
#     msg="""
#         ==Bienvenido a Sistema Inmobiliario==
#         1. Mostrar Propiedades
#         2. Ver cantidad de propiedades
#         3. Ver primera y ultima propiedad
#         4. Agregar una propiedad
#         5. Salir    
#     """
#     print(msg)

#     option = int(input("Seleccione una opcion: "))
#     if option == 1:
#         print(propertys_v2["propiedades"])
#     elif option == 2:
#         print(len(propertys_v2["propiedades"]))
#     elif option == 3:
#         primera = propertys[0]
#         ultima = propertys[-1]
#         print(f"La primera es: {primera,direcciones[0]} y la ultima es: {ultima,direcciones[-1]}")
#     elif option == 4:
#         #SIN DICCIONARIO
#         #----------------
#         # nueva_property = input("Ingrese una nueva casa: ")
#         # propertys.append(nueva_property)
#         # print(propertys)
#         #CON DICCIONARIO
#         #----------------
#         id_nuevo = len(propertys_v2["propiedades"]) + 1
#         new_property = {}
#         new_property_2 = {}
#         new_property["id"] = id_nuevo
#         name = input("Ingrese el nombre: ")
#         new_property["nombre"] = name
#         direcciones1 = input("Ingrese la direccion 1: ")
#         direcciones2 = input("Ingrese la direccion 2: ")
#         new_property["direccion"] = (direcciones1,direcciones2)
#         new_property["precio"] = float(input("Ingrese el precio: "))
#         propertys_v2["propiedades"].append(new_property)
#         print(propertys_v2["propiedades"])    
#     elif option == 5:
#         print("Cerrando...")
#         break
#     else:
#         print("Opcion no valida")
    
"ESTRUCTURAS DE CONTROL ITERATIVAS"
# for i in range(5,10,3): #el 5 significa que comienza y el 10 termina,#el 3 es el paso osea de cuanto a cuanto va a saltar
#     print(i)
#--------------------------------------------------------------------------------------------------------------------------
# while True:
#     cantidad = int(input("Ingrese la cantidad de iteraciones : "))   
#     for i in range(1,cantidad+1):
#         print(i)
 
"FUNCIONES BASICAS"
# def saludar():
#     print("Hola Mundo")
# saludar()
#----------------O-------------------
#def saludar(name):
#    print("Hola",name)
#saludar("jean")
#----------------O-------------------
# def salidarv2(name):
#     return f"Hola {name}"
# saludo = salidarv2("Jean")

# if len(saludo)>10:
#     print("El saludo es muy largo")
# else:
#     print("No se puedo enviar el mesg")
#----------------O-------------------
# def registrarCliente():
#     print("Agregando Cliente")
# def enviarCorreo():
#     print("Enviando Correo")
#     pass
    
# while True:
#     option = int(input("Seleccione una opcion: "))
#     if option == 1:
#         enviarCorreo()
#     elif option == 2:
#         registrarCliente()
#     else:
#         print("Opcion Invalidad...")
#         break