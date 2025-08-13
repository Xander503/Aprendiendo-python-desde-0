# declaramos e inicializamos 2 numeros y hacemos uso de los tipos de operadores
numero1 = 10
numero2 = 3

# Operadores aritméticos de Python
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2
modulo = numero1 % numero2
potencia = numero1**numero2
division_de_piso = numero1 // numero2

print(f"la suma es: {suma}")
print(f"la resta es: {resta}")
print(f"la multiplicacion es {multiplicacion}")
print(f"la division es: {division}")
print(f"el modulo es: {modulo}")
print(f"ĺa potencia es: {potencia}")
print(f"la division de piso es: {division_de_piso}")
print("-----------------------------------------------------------------")


# Operadores de asignación de Python (mas comunes)
variable = 5
print("variable actual : ",variable)
variable += 3
print("variable : ",variable)
variable -= 3
print("8 - 3: ",variable)
variable *= 3
print("5 * 3: ",variable)
variable /= 3
print("15 / 3: ",variable)
print("-----------------------------------------------------------------")


# Operadores de comparación de Python

print(f"el numero {numero1} es igual que el numero { numero2}: {numero1==numero2}")
print(f"el numero {numero1} es diferente que el numero { numero2}: {numero1!=numero2}")
print(f"el numero {numero1} es menor que el numero { numero2}: {numero1<numero2}")
print(f"el numero {numero1} es mayor que el numero { numero2}: {numero1>numero2}")
print(f"el numero {numero1} es menor o igual que el numero { numero2}: {numero1<=numero2}")
print(f"el numero {numero1} es mayor o igual que el numero { numero2}: {numero1>=numero2}")
print("-----------------------------------------------------------------")


# Operadores lógicos de Python

print(f"los numeros 10 y 3 son mayores que 5: {(numero1 and numero2) > 5}")
print(f"los numeros 10 (not)y 3 son mayores que 5: {not(numero1 and numero2 > 5)}")
print(f"los numeros 10 o 3 son mayores que 5: {(numero1 or numero2) > 5}")
print("-----------------------------------------------------------------")

# Operadores de identidad de Python(compara direccion de memoria)

a = numero1
print(numero1 is numero2)     # False ya que no tienen la misma direccion de memoria
print(numero1 is a)           # True ya que tienen la misma direccion de memoria
print(numero1 is not a)       # Es la negacion del "is"
print("-----------------------------------------------------------------")


# Operadores de membresía de Python(se utiliza para saber si un valor esta dentro de un conjunto,listas,tuplas,etc.)

lista = [1,2,3,4,5]

print(3 in lista)             # True ya que el 3 si esta en la lista
print(10 in lista)            # False ya que el 10 no esta en la lista
print (3 not in lista)        # Negacion del "in"


