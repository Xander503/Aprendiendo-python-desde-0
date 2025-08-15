# Estructura if,elif y else

nombre = input("ingresa tu nombre: ").upper() # upeer() conviente la variable en mayusculas
edad = input("ingrese su edad: ")             # edad es un dato tipo string

if nombre != "":
    print(f" BIENVENIDO {nombre}")

    if edad.isdigit() and int(edad) > 0:      # si edad(dato string) es un digito y (convertimos edad en un entero) si edad es mayor que 0 
        if int(edad) >= 18:                   # (convertimos edad en un entero) si edad es mayor o igual a 18 
            print(f"eres mayor de edad")

        elif int(edad) < 18:                  # (convertimos edad en un entero) si edad es menor a 18 
            print("llama a tus padres ya que eres menor de edad")
    
    else:
        print("por favor ingrese datos que sean validos")