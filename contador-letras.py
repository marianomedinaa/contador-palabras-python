# Paso 1: Mostrar mensaje: "Por favor, ingrese una palabra: "

palabra_ingresada = input("Por favor, ingrese una palabra: ")

# Paso 2: Definir la variable cantidad_letras y asignarle la Longitud de la palabra ingresada

cant_letras = len(palabra_ingresada)

# Paso 3: Mostrar mensaje: "La palabra ingresada tiene", cantidad_letras, "letras."

print(f"La palabra {palabra_ingresada} tiene {cant_letras} letras.")