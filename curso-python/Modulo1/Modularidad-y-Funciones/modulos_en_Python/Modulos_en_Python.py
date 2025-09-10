# importamos "Modulo" donde tenemos nustras funciones y "os" para limmpiar la consola
import Modulo
import os

# llamamos la funcion saludo que esta definida dentro del modulo
Modulo.Saludo("jose hernandez")

# importar usando from, esto nos permite importar solo partes del modulo
from Modulo import Saludo

# llamamos a la funcion directamente sin referirnos a ella como Modulo.Saludo()
print("----------------------")
Saludo("maria fernanda")


# calculadora de areas
print("----------------------")
enter = input("presione ENTER para continuar a la caluladora de areas")

while True:
    os.system("clear")
    print("calculadora de areas:")
    print("1-cuadrado")
    print("2-rectangulo")
    print("3-triangulo")
    print("4-salir")
    opc = input("ingrese que figura desea calcular el area: ")
    
    if opc == "1":
        lado = input("ingrese el lado: ")
        if lado.isdigit():
            Modulo.AreaCuadrado(float(lado))
            enter = input("presione ENTER para continuar")
        else:
            print("por favor solo ingrese valores numericos")
            enter = input("presione ENTER para continuar")

    elif opc == "2":
        base = input("ingrese la base: ")
        altura = input("ingrese la altura:")
        if base.isdigit() and altura.isdigit():
            Modulo.AreaRectangulo(float(base), float(altura))
            enter = input("presione ENTER para continuar")
        else:
            print("por favor solo ingrese valores numericos")
            enter = input("presione ENTER para continuar")
    
    elif opc == "3":
        base = input("ingrese la base: ")
        altura = input("ingrese la altura:")
        if base.isdigit() and altura.isdigit():
            Modulo.AreaTriangulo(float(base), float(altura))
            enter = input("presione ENTER para continuar")
        else:
            print("por favor solo ingrese valores numericos")
            enter = input("presione ENTER para continuar")
    
    elif opc == "4":
        break
    else:
        print("ingrese valores validos")
        enter = input("presione ENTER para continuar")
