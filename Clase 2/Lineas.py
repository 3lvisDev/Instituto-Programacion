############################################################################################
#                #                                                               #         #
#            #       #       # Student: Elvis Da Silva                         #    #      #
#         #              #   # Institute Providencia Profesional #          #         #    #
#      #                     # Date: 06/04/2023                   #      #            #    #
#   #                                                                 #                  # #
############################################################################################

''' 

Explicar el flujo del código mediante comentarios y cómo las variables toman importancia
• ¿Por qué creaste cada variable?
• ¿Cuál fue su función para el ítem?
• ¿Por qué creaste cada variable?

Respuestas: 1

• Estas variables fueron creadas para almacenar y manipular la información necesaria para dibujar la matriz. num_filas y num_columnas se utilizan para determinar la cantidad de filas y columnas que tendrá la matriz. fila se utiliza para crear cada fila de la matriz, mientras que matriz se utiliza para almacenar la matriz completa. Al utilizar una lista de listas, podemos acceder a cada elemento de la matriz mediante su índice de fila y columna, lo que facilita la manipulación de la información en la matriz.

Respuestas: 2

• cada variable se creó con un propósito específico y todas son necesarias para lograr la construcción de la matriz solicitada por el usuario.

Respuesta 3

• Se crearon estas variables para poder almacenar los valores ingresados por el usuario y utilizarlos en la creación de la matriz mediante los bucles for. La variable fila se utiliza para almacenar los caracteres que conforman cada fila de la matriz y luego imprimirlos, y la variable columna se utiliza para agregar cada carácter a la fila correspondiente. De esta forma, se pueden crear las filas y columnas de la matriz según las dimensiones ingresadas por el usuario.






'''

####################################################################### 
# # Se solicita al usuario ingresar el número de filas y columnas     #    
#######################################################################

num_filas_principal = int(input("Ingrese la cantidad de filas: "))

#####################################
# Solicitar la cantidad de columnas #
#####################################
num_columnas_principal = int(input("Ingresa la cantidad de columnas: "))


#####################
# Dibujar la matriz #           
#####################
for i in range(num_filas_principal):
    for j in range(num_columnas_principal):
        print("*", end=" ")

##########################################################################################################
# Utilizamos la función "print" con el argumento "end" para imprimir los asteriscos en una misma línea.  #
# De esta forma, se formará una fila completa antes de pasar a la siguiente.                             #
##########################################################################################################
        
print()
##########################################################################################################
# Al final de cada fila, utilizamos la función "print" sin argumentos para imprimir un salto de línea    #
# De esta forma, se creará una nueva línea para la siguiente fila.                                       #
##########################################################################################################
    