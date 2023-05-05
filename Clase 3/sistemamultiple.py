############################################################################################
#                #                                                               #         #
#            #       #       # Student: Elvis Da Silva                         #    #      #
#         #              #   # Institute Providencia Profesional #          #         #    #
#      #                     # Date: 04/04/2023                   #      #            #   #
#   #                                                                 #                  # #
############################################################################################

'''
Escribir un programa que lea entre 10 y 20 números ingresados por el usuario, los almacene
en una lista y los muestre ordenados de mayor a menor. El programa debe seguir recibiendo
ingreso de números hasta que el usuario ingrese 0. Sin embargo, el número 0 no debe ser
mostrado en pantalla.

'''

# Ejercicio 1: Leer entre 10 y 20 números, almacenarlos y mostrarlos ordenados de mayor a menor
numeros = []

print("Ejercicio 1 - Números ordenados de mayor a menor\nIngrese números (0 para terminar).")

while len(numeros) < 20:
    entrada = input("Ingrese un número: ")
    numero = int(entrada)
    if numero == 0:
        break
    numeros.append(numero)

numeros_ordenados = sorted(numeros, reverse=True)
print("Números ingresados ordenados de mayor a menor:")
print(numeros_ordenados)
print("\n")


'''
Escribir un programa que almacene palabras ingresadas por el usuario. El programa debe
seguir recibiendo ingreso de palabras hasta que el usuario ingrese tres asteriscos "***". Luego
de esto, las palabras deben ser mostradas por pantalla una única vez. Es decir, si el usuario
ingresó palabras repetidas, solo se deben mostrar una vez.

'''

# Ejercicio 2: Almacenar palabras únicas ingresadas por el usuario
palabras = set()

print("Ejercicio 2 - Palabras únicas\nIngrese palabras. Ingrese '***' para terminar.")

while True:
    palabra = input("Ingrese una palabra: ")
    if palabra == "***":
        break
    palabras.add(palabra)

print("Palabras ingresadas sin repetición:")
for palabra in palabras:
    print(palabra)

print("\n")

'''
Construir un programa que determine si dos palabras ingresadas por el usuario son
anagramas.

'''
# Ejercicio 3: Anagramas
def son_anagramas(palabra1, palabra2):
    palabra1 = palabra1.upper().replace(" ", "")
    palabra2 = palabra2.upper().replace(" ", "")
    return sorted(palabra1) == sorted(palabra2)

palabra1 = input("Ejercicio 3 - Anagramas\nIngrese la primera palabra: ")
palabra2 = input("Ingrese la segunda palabra: ")
anagramas = son_anagramas(palabra1, palabra2)

if anagramas:
    print(f"'{palabra1}' y '{palabra2}' son anagramas.\n")
else:
    print(f"'{palabra1}' y '{palabra2}' no son anagramas.\n")


'''
Construir un programa en donde el usuario ingrese números por pantalla y el programa
devuelva la suma de todos los números ingresados por el usuario. Si el usuario ingresa un
carácter no numérico, el programa debe mostrar un mensaje de error y continuar
solicitando números y sumando. El programa finaliza cuando el usuario presione enter.

'''
# Ejercicio 4: Suma de números ingresados
suma = 0
print("Ejercicio 4 - Suma de números\nIngrese números para sumar. Presione 'Enter' para terminar.")

while True:
    entrada = input("Ingrese un número: ")
    if entrada == "":
        break
    try:
        numero = float(entrada)
        suma += numero
    except ValueError:
        print("Carácter no numérico ingresado. Por favor, ingrese un número.")

print(f"La suma de los números ingresados es: {suma}\n")


'''
Juguemos Scrabble! Construye un diccionario con los siguientes valores. Luego, el usuario
ingresa una palabra por pantalla y el programa devuelve el puntaje correspondiente

'''
# Ejercicio 5: Scrabble
valores_scrabble = {
    'A': 1, 'E': 1, 'I': 1, 'L': 1, 'N': 1, 'O': 1, 'R': 1, 'S': 1, 'T': 1, 'U': 1,
    'D': 2, 'G': 2,
    'B': 3, 'C': 3, 'M': 3, 'P': 3,
    'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
    'K': 5,
    'J': 8, 'X': 8,
    'Q': 10, 'Z': 10,
}

def calcular_puntaje(palabra, valores):
    puntaje = 0
    for letra in palabra.upper():
        if letra in valores:
            puntaje += valores[letra]
    return puntaje

palabra = input("Ejercicio 4 - Scrabble\nIngrese una palabra para calcular su puntaje en Scrabble: ")
puntaje = calcular_puntaje(palabra, valores_scrabble)
print(f"El puntaje de '{palabra}' en Scrabble es: {puntaje}\n")
