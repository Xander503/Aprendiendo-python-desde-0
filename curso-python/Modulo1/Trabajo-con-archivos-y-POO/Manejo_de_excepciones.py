# El bloque try le permite probar un bloque de código en busca de errores.
try:
    # Código que puede causar una excepción
    numero = int(input("Ingrese un número: "))
    resultado = 10 / numero
# El bloque except le permite manejar el error.
except ValueError:
    print("Error: Debe ingresar un número válido.")
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
# El bloque else te permite ejecutar código cuando no hay ningún error.
else:
    print(f"El resultado es: {resultado}")
# El bloque finally le permite ejecutar código, independientemente del resultado de los bloques de prueba y excepción.
finally:
    print("Ejecución del bloque finally. Esto siempre se ejecuta.")



#generar una excepción personalizada con "raise"
print("-----------------------------------------------")
numero2 = int(input("ingrese un numero mayor que 5: "))
if numero2 < 5:
    raise Exception("El número ingresado es menor que 5, se genera una excepción personalizada.")
else:
    print(f"el numero es: {numero2}")