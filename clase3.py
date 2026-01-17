# msg ="""
#         BIENVENIDO A SISTEMA-DATUX
#         1. Login
#         2. Salir
# """
# usuario = [
#     {
#         'id': 1,
#         'username': 'jean',
#         'lastname': 'ortiz',
#         'perfil': 'administrador',
#         'email': 'jean@gamil.com',
#         'password': 'admin123',
#         'status': True    
#     }
# ]

# def menuIterativoLogeado():
#     msg2=""""
#         1.Crear Producto
#         2. Listar Productos
#         3. Evaluar Cliente
#         4. Salir
#     """
#     logeado = True
#     while logeado:
#         print(msg2)
#         opcion = int(input("Ingrese una opcion: "))
#         if opcion == 1:
#             pass
#         elif opcion == 2:
#             pass
#         elif opcion == 3:
#             pass
#         elif opcion == 4:
#             logeado = False
#         else:
#             print("Opcion no valida")

# def buscar_usuario(email):
#     for i in usuario:
#         if email==i['email']:
#             return i
#     return False




# def login():
#     #se necesita un usuario y contraseña
#     #comparar en la bd
#     email = input("Ingrese su email: ")
#     usuario = buscar_usuario(email)
#     if usuario.get('status'):
#         password = input("Ingrese su contraseña: ")
#         if password == usuario['password']:
#             print(f"Login exitoso {usuario['username']}")
#         else:
#             print("Contraseña incorrecta")
#     else:
#         print("Usuario inactivo")
        


# while True:
#     print(msg)
#     opcion = int(input("Ingrese una opcion: "))
#     if opcion == 1:
#         usuario_logeado = login()
#         menuIterativoLogeado()
#     elif opcion == 2:
#         print("Saliendo...")
#         break
#     else:
#         print("Opcion no valida")
        
"Paso Valor Referencia"
# lista = [1,2,3,4,5]
# a = 10

# def FxDemo(a, lista):
#     a = a * 2
#     print(a)
#     lista[-1] = 2*lista[-1]
#     print(a,lista)
# FxDemo(a, lista)
# print(a, lista)

"Find - Realiza busqueda en texto "
# my_String = "Where's waldo?"
# print(my_String.find("waldo"))  # Devuelve el indice donde empieza la palabra
# print(my_String.find("wenda"))
# if my_String.find("wenda"):
#     print("wenda")
# else:
#     print("wenda no esta") # Devuelve -1 si no encuentra la palabra

"Primera letra en mayuscula"
# string1 = "hola"
# print(string1.capitalize())

"Cambiar palabra en texto"
# text="Hola fulano como estas todo bien"
# new_list = text.split(" ")
# new_list[1]="mengano" #el 1 significa el fulano, empieza con 0 1 2 etc
# print(" ".join(new_list))

"Try - Except"
# try:
#     opcion = int(input("Ingrese un numero: "))
#     print(f"El numero ingresado es: {opcion}")
# except:
#     print(f"Fallo, no es un entero")
# else:
#     print("Solo si las lineas 2 y 3 se ejecutan ya funciona")
# finally:
#     print("Se ejecuta siempre")
"Forma generica"
# try:
#     lista = [1,2,3]
#     lista[5]
#     # print(0/0)
# except Exception as e:
#     print(e)

"POO - Encapsulamiento"
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def __str__(self):
        return f"Hola mi nombre es {self.nombre} y tengo {self.edad} años"
persona1 = Persona("Jean", 25)
print(persona1)

class Empleado(Persona):
    def comparar_edades(self, edad2):
        return self.edad == edad2
empleado1 = Empleado("Carlos", 50) #compara con ese numero
print(empleado1.comparar_edades(30))
print(empleado1.comparar_edades(25))

# __init__()   # constructor
# __str__()    # print(obj)
# __repr__()   # representación técnica
# __len__()    # len(obj)
# __eq__()     # ==
# __lt__()     # <
# __del__()    # destructor


    



