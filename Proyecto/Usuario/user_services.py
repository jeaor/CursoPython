from sqlite3 import Connection
#llama a la libreria y trae el objeto coneccion
def getUser(email:str,con:Connection):
    cursor = con.cursor
    query = "select * from user where email = ?"
    resultado = cursor.execute(query,(email))
    data = resultado.fetchall
    
if __name__ == "__main__":
    print ("main2")