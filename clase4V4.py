"Expreciones Regulares"
import re
# texto = "hola mundo"
# encontrado = re.search("hola",texto)
# if encontrado:
#     print("Encontrado")
# else:
#     print("No encontrado")

texto = "los ganadores son: hola1, hola2, hola3"
#para encontrar valores de hola en el texto
patron = r"hola\d"
print(re.findall(patron,texto))
#para encontrar valores de hola exacto en el texto
patron = r"hola1\D"
print(re.findall(patron,texto))
