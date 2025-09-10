# Los módulos integrados en Python son bibliotecas estándar que vienen incluidas
# con la instalación de Python.
# Algunos ejemplos de módulos integrados en Python son:


# datetime: Proporciona clases para trabajar con fechas y horas.
import datetime

# se consigue con un formato de: año-mes-dia hora:minutos:segundos.microsegundos
fecha_actual = datetime.datetime.now()
print("-------------------")
print(fecha_actual)

# se consigue la fecha actual con un formato de: año-mes-dia
fecha_actual2 = datetime.datetime.now().strftime("%Y-%m-%d")
print("-------------------")
print(fecha_actual2)

# se consigue la hora actual con un formato de hora:minutos:segundos
hora_actual = datetime.datetime.now().strftime("%H:%M:%S")
print("-------------------")
print(hora_actual)


# math: Proporciona funciones matemáticas avanzadas.
import math

# devuelve el valor maximo entre los argumentos
maximo = max(2, 4, 8, 3)
print("-------------------")
print(maximo)

# devuelve el valor minimo entre los argumentos
print("-------------------")
minimo = min(13, 5, 7, 3)
print(minimo)

# devuelve el valor de la potencia 4**3
print("-------------------")
potencia = pow(4, 3)
print(potencia)

# debuelve el valor de una raiz cuadrada
print("-------------------")
raiz = math.sqrt(64)
print(raiz)

# devuelve el valor de la constante pi
print("-------------------")
pi = math.pi
print(pi)


# json: Proporciona funciones para trabajar con datos en formato JSON (JavaScript Object Notation).
import json

# convertir de Json a diccionario python

json_dato = '{"nombre":"eduardo","edad":"34","genero":"masculino"}'
print("----------------------------------------------------------")
python = json.loads(json_dato)
print(python)

# convertir diccionario  python en json
print("----------------------------------------------------------")
json_conversion = json.dumps(python)
print(json_conversion)


# os: Proporciona una interfaz para trabajar con el sistema operativo.
import os

# permite limpiar la terminar clear en Linux/macOS y cls en Windows
print("----------------------------------------")
enter = input("presione enter para limpiar la terminar: ")
os.system("clear")


# re: Proporciona funciones para trabajar con expresiones regulares.
import re

# revisa si un texto unicia con un patron
texto = "hola mundo"
resultado = re.match("hola", texto)
print("------------------------------------------------------------")
print(f"texto:{texto} \nresultado:{resultado}")

# busca el patron en cualquier parte del texto
texto2 = "hoy es un buen dia para salir a caminar"
resultado2 = re.search("buen", texto2)
print("------------------------------------------------------------")
print(f"texto:{texto2} \nresultado:{resultado2}")

# devuelve todas las coincidencias en una lista
texto3 = "hola, adios, buenos dias, buenas tardes, buenas noches"
resultado3 = re.findall("buenas", texto3)
print("------------------------------------------------------------")
print(f"texto:{texto3} \nresultado:{resultado3}")

# reemplaza las coicidencias del patron por otro texto
texto4 = "hola, hola, Hola, HOLA, holA"
# flags=re.IGNORECASE ignora las mayusculas/minisculas para hacer el reemplazo
resultado4 = re.sub("hola", "adios", texto4, flags=re.IGNORECASE)
print("------------------------------------------------------------")
print(f"texto:{texto4} \nresultado:{resultado4}")

# divide el texto usando el patron como separador
texto5 = "uno dos tres cuatro cinco"
# [ ] indica que se usa el espacio como separador
resultado5 = re.split("[ ]", texto5)
print("------------------------------------------------------------")
print(f"texto:{texto5} \nresultado:{resultado5}")


# random: Proporciona funciones para generar números aleatorios.
import random

# genera un numero aleatorio en un rango del 1 al 100
numero_aleatorio = random.randint(1, 100)
print("------------------------------------------------------------")
print(f"numero aleatorio: {numero_aleatorio}")
