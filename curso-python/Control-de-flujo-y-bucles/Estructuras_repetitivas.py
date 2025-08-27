# Bucle while, else y continue

contador = 1
while contador < 11:
    print(f"contador while: {contador}")
    contador += 1

else:
    print("aca termina el ciclo")
    print("---------------------------------------------")

contador2 = 1
while contador < 11:
    contador +=1
    if contador == 7:
        print(f"el numero 7 no se va a imprimir")
        continue
    print(contador2)

# #Bucle for,else y continue 
for contador3 in range (1,11):      #rango desde 1 a 10
    print(f"contador for: {contador3}")

else:
    print("aca termina el ciclo")
    print("---------------------------------------------")

for numero in range (10):
    if numero == 3:
        print("el numero 3 no se va a imprimir")
        continue
    print(numero)


