# Funciones en Python (definición, parámetros, valores de retorno).


# definimos funcion saludo sin parametro
def saludo():
    print("Hola este mensaje es un saludo")


# definimos funcion de saludo con parametro
def saludo2(nombre):
    print(f"Hola {nombre} este mensaje es un saludo")


# llamamos las funciones
saludo()
print("--------------------------------------")
saludo2("Alex")


# si no se conoce la cantidad de argumentos/parametros podemos usar *nombre_variable para recibir una tupla de argumentos
def prueba_arg(*datos):
    print("--------------------------------------")
    print(f"Este es el valor del indice 2: {datos[2]}")


# llamamos la funcion
prueba_arg(1, 2, 3, 4, 5)


# valores de retorno
def multiplicar(x):
    return 2 * x


print("--------------------------------------")
print("El valor retornado es: ", multiplicar(10))


# recursividad
print("--------------------------------------")


def factorial(numero):
    if numero == 1:
        return 1
    elif numero > 1:
        return numero * factorial(numero - 1)


print(f"El factorial del numero es: {factorial(5)}")
