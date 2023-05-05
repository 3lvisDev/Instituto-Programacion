############################################################################################
#                #                                                               #         #
#            #       #       # Student: Elvis Da Silva                         #    #      #
#         #              #   # Institute Providencia Profesional #          #         #    #
#      #                     # Date: 04/04/2023                   #      #            #   #
#   #                                                                 #                  # #
############################################################################################

'''
Para el primer ejercicio, se debe crear una función que reciba una contraseña como
argumento y determine si es segura o no. Se deben implementar lógicas para verificar si
la contraseña contiene al menos una mayúscula, una minúscula y un número. La función
debe devolver True si es segura y False si no lo es

'''
def password_is_valid(password):
    # Variables para verificar si la contraseña contiene una mayúscula, una minúscula y un número
    has_upper = False
    has_lower = False
    has_digit = False

    # Iterar sobre cada carácter en la contraseña
    for char in password:
        # Verificar si el carácter es una letra mayúscula
        if char.isupper():
            has_upper = True
        # Verificar si el carácter es una letra minúscula
        elif char.islower():
            has_lower = True
        # Verificar si el carácter es un número
        elif char.isdigit():
            has_digit = True

    # Devolver True si la contraseña contiene al menos una mayúscula, una minúscula y un número, de lo contrario False
    return has_upper and has_lower and has_digit

# Ejecutar la función para verificar una contraseña de ejemplo
print(password_is_valid("#Ns!PMF7m")) # Debería imprimir True

'''
Para el segundo ejercicio, se debe crear una función recursiva que lea números ingresados
por el usuario hasta que se ingrese un espacio en blanco. La función debe sumar los
números y devolver el resultado. Si el primer input es un espacio, la función debe imprimir
0

'''
def sum_numbers():
    """
    Función recursiva que suma números ingresados por el usuario hasta que se ingrese un espacio en blanco.
    Si el primer input es un espacio, la función imprime 0.
    """
    # Obtener un número ingresado por el usuario
    num = input("Ingrese un número o un espacio en blanco para detener la entrada: ")

    # Verificar si el número es un espacio en blanco
    if num.strip() == "":
        # Si es un espacio en blanco, devolver 0
        return 0
    # Si no es un espacio en blanco, convertirlo a un número y sumarlo con la llamada recursiva
    else:
        return int(num) + sum_numbers()

# Ejecutar la función y guardar el resultado en una variable
result = sum_numbers()

# Imprimir el resultado
print("La suma de los números ingresados es:", result)

'''
Para el tercer ejercicio, se debe crear una clase llamada "Cuenta" que tenga las
propiedades número de cuenta, nombre del titular, saldo inicial y tipo de cuenta. La clase
debe tener tres métodos: depositar, retirar y obtener balance. El método depositar debe
recibir una cantidad y agregarla al saldo de la cuenta. El método retirar debe recibir una
cantidad y restarla del saldo de la cuenta. El método obtener balance debe devolver el
saldo actual de la cuenta. Para probar la clase, se debe crear una instancia de la misma,
hacer un depósito, un retiro y obtener el saldo actual. Finalmente, se debe imprimir la
información con todos los datos de usuarios y balances  y incluye lo importante que te indique

'''

class Cuenta:
    """
    Clase que representa una cuenta bancaria con las propiedades: número de cuenta, nombre del titular, saldo inicial y tipo de cuenta.
    """
    def __init__(self, numero_cuenta, nombre_titular, saldo_inicial, tipo_cuenta):
        """
        Inicializar la cuenta con los valores proporcionados.
        """
        self.numero_cuenta = numero_cuenta
        self.nombre_titular = nombre_titular
        self.saldo = saldo_inicial
        self.tipo_cuenta = tipo_cuenta

    def depositar(self, cantidad):
        """
        Depositar una cantidad en la cuenta.
        """
        self.saldo += cantidad

    def retirar(self, cantidad):
        """
        Retirar una cantidad de la cuenta.
        """
        self.saldo -= cantidad

    def obtener_balance(self):
        """
        Obtener el balance actual de la cuenta.
        """
        return self.saldo

# Crear una instancia de la clase Cuenta
cuenta = Cuenta("123456", "Elvis Da Silva", 1000, "Ahorro")

# Depositar una cantidad en la cuenta
cuenta.depositar(500)

# Retirar una cantidad de la cuenta
cuenta.retirar(250)

# Obtener el balance actual de la cuenta
balance = cuenta.obtener_balance()

# Imprimir la información de la cuenta
print("Información de la cuenta:")
print("Número de cuenta:", cuenta.numero_cuenta)
print("Nombre del titular:", cuenta.nombre_titular)
print("Saldo:", balance)
print("Tipo de cuenta:", cuenta.tipo_cuenta)
