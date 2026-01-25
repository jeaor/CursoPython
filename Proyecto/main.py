from Usuario.user_services import getUser
def getMenu():
    msg ="""
        BIENVENIDO A SISTEMA
        1. Login
        2. Salir
    """
    print(msg)
    opcion = int(input("Ingrese una opcion: "))
    return opcion

def evaluate(opcion:int):
    if opcion == 1:
        email = "this is email"
        password = "this is password"
        data = getUser(email)
        if data['password'] == password:
            print("Bienvenido")
        else:
            print("Contraseña incorrecta")
            getMenu()
    elif opcion == 2:
        print("Saliendo...")
        return False
    
if __name__ == "__main__":
    running = True
    while running:
        opcion = getMenu()
        eval = evaluate(opcion)
        running = eval