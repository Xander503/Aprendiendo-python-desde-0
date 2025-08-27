# Listas(Colecciones ordenadas y mutables)
lista_de_carros = []

# creamos las variables para guardar en la lista de carros
carro1 = "Toyota"
carro2 = "Ford"
carro3 = "Nissan"

# las agregamos en la lista de carros usando .append()
lista_de_carros.append(carro1)
lista_de_carros.append(carro2)
lista_de_carros.append(carro3)

# imprimimos la lista de carros
# con len() obtenemos el largo de la lista es decir la cantidad de los valores a imprimir por indices
print("------------------ \nLista:")
for x in range(len(lista_de_carros)):
    print(lista_de_carros[x])

# o tambien por valores
print("------------------ \nLista:")
for x in lista_de_carros:
    print(x)

# modificamos carro2 de Ford a ferrari por medio de indices
lista_de_carros[1] = "Ferrari"

# removemos o eliminamos carro1
print(
    "------------------ \nLista: usando la funcion .remove() y modificacion de elemento"
)
lista_de_carros.remove(carro1)
for x in range(len(lista_de_carros)):
    print(lista_de_carros[x])


# tuplas(Colecciones ordenadas e inmutables)
print("------------------ \nTupla:")
tupla_de_frutas = ("banana", "manzana", "pera", "uva")

# imprimimos los valores de la tupla
for x in range(len(tupla_de_frutas)):
    print(tupla_de_frutas[x])


# conjuntos(Colecciones desordenadas, mutables y de elementos únicos)
conjunto = set()

# para agregar un elemento al conjunto usamos .add()
conjunto.add(1)

# para agregar multiples elementos es decir un iterable como una lista,tupla,conjunto,etc usamos .update()
conjunto.update([2, 3, 9, 6])

# imprimimos el conjunto
print("------------------ \nConjunto predeterminado (desordenado):")
for elemento in conjunto:
    print(elemento)

# removemos el 3 de el cunjunto con ayuda de .remove()
conjunto.remove(3)

# imprimimos el conjunto de forma ordenada
print("------------------ \nConjunto ordenado:")
for elemento in sorted(conjunto):
    print(elemento)


# diccionarios(Colecciones desordenadas que almacenan datos en pares de clave-valor)
diccionario = {}

# agregamos un elemento clave-valor
diccionario["clave1"] = "valor1"

# agregamos multiples elementos con ayuda de un nuevo diccionario y .update()
nuevos_datos = {"clave2": "valor2", "clave3": "valor3"}
diccionario.update(nuevos_datos)

# actualizamos o modificamos el valor de una clave
diccionario["clave1"] = "nuevo_valor1"

# imprimimos el diccionario con clave-valor con ayuda de .item()
print("------------------ \nDiccionario:")
for clave, valor in diccionario.items():
    print(f"{clave}-{valor}")
