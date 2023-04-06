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

• En este programa se creó una variable llamada "numero_juegos" para almacenar el número entero del 1 al 9 ingresado por el usuario. Esta variable es importante para determinar si cada número del 1 al 9 es múltiplo del número ingresado por el usuario.
• También se creó una variable "i" en el bucle "for" para recorrer los números del 1 al 9. Esta variable es necesaria para llevar un control sobre los números que se están evaluando en cada iteración.
• Además de estas variables, no se crearon otras variables en este programa porque los valores se pueden imprimir directamente en la consola sin necesidad de almacenarlos en variables adicionales.

Respuestas: 2

• La variable "numero_juego" es fundamental en este programa ya que almacena el número entero del 1 al 9 ingresado por el usuario, y se utiliza para determinar si cada número del 1 al 9 es múltiplo de ese número.
• La variable "i" se utiliza en el bucle "for" para recorrer los números del 1 al 9 y llevar un control sobre los números que se están evaluando en cada iteración.
• En resumen, la variable "numero" es esencial para el funcionamiento del programa, mientras que la variable "i" es necesaria para recorrer los números del 1 al 9 en el bucle "for".

Respuesta 3

• Esta variable es importante porque se utiliza para determinar si cada número del 1 al 9 es múltiplo del número ingresado por el usuario. De esta manera, se puede determinar qué números se deben saltar al ingresar la secuencia de números.
• También se utiliza una variable "i" en el bucle "for" para recorrer los números del 1 al 9. Esta variable es necesaria para llevar un control sobre los números que se están evaluando en cada iteración y para imprimir la secuencia de números en pantalla.
• En resumen, las variables "numero" e "i" son esenciales para el funcionamiento del programa ya que se utilizan para tomar decisiones y controlar el flujo del programa.






'''

#####################################################################################################
# Se crea la variable "numero_juegos" para almacenar el número entero ingresado por el usuario.     #       # 
# Esta variable será la clave para determinar qué números se deben omitir en la secuencia.          #             #
#####################################################################################################

numero_juegos = int(input("Ingresa un número entero del 1 al 9: "))


#########################################################################
# Si el número ingresado está dentro del rango, se inicia la secuencia. #
# Se utiliza un bucle "for" para recorrer los números de la secuencia.  #            
#########################################################################
if numero_juegos < 1 or numero_juegos > 9:
    print("Error: el número ingresado debe estar entre 1 y 9.")
else:
#########################################################################
# Si el número ingresado está dentro del rango, se inicia la secuencia. #
# Se utiliza un bucle "for" para recorrer los números de la secuencia.  #            
#########################################################################
    for i in range(1, numero_juegos+1):

#########################################################################################
# La variable "i" toma los valores de la secuencia.                                     #
# Se utiliza la expresión "numero+1" en el rango para que se incluya el último número.  #            
#########################################################################################

        if i % numero_juegos != 0:
############################################################################
# Si el número actual de la secuencia NO es múltiplo del número ingresado  #
# se solicita al usuario que ingrese el número correspondiente.            #            
############################################################################

            respuesta_juego = int(input("Ingresa el número " + str(i) + " de la secuencia: "))

#######################################################################################
# Se crea la variable "respuesta" para almacenar el número ingresado por el usuario.  #
# Esta variable se utiliza para comparar con el número actual de la secuencia.        #            
#######################################################################################

            if respuesta_juego != i:
                print("Error: el número ingresado debió ser " + str(i) + ".")
#######################################################################################################
#  # Si el usuario ingresa un número incorrecto, se muestra un mensaje de error y se rompe el bucle.  #          
#######################################################################################################

                break
    else:
        print("¡Felicidades, completaste la secuencia!")
#######################################################################################################
# Si el usuario ingresa todos los números correctamente, se muestra un mensaje de felicitación.  #          
#######################################################################################################

