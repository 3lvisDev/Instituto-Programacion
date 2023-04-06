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


Respuestas: 1

• En la primera línea se solicita al usuario su año de nacimiento y se almacena en la variable anio_nacimiento.
• En la segunda línea se solicita al usuario su año de muerte o 0 si sigue vivo, y se almacena en la variable anio_muerte.
• Luego se importa la librería datetime para obtener el año actual, que se almacena en la variable anio_actual.
• Si el usuario ingresó 0 como año de muerte, se reemplaza por el año actual mediante un condicional if.
• Se inicializa la variable cantidad_anios_bisiestos en 0, la cual será utilizada para almacenar la cantidad de años bisiestos vividos.
• Se utiliza un ciclo for para recorrer cada año desde el año de nacimiento hasta el año de muerte.
• Dentro del ciclo for, se utiliza un condicional if para verificar si el año actual es bisiesto y, de ser así, se incrementa la variable cantidad_anios_bisiestos.
• Finalmente, se muestra en pantalla la cantidad de años bisiestos vividos por la persona mediante la función print().
• Las variables en este programa son importantes porque permiten almacenar y manipular los datos que el usuario ingresa, así como los resultados obtenidos durante la ejecución del programa. Por ejemplo, las variables anio_nacimiento y anio_muerte almacenan los años ingresados por el usuario, y la variable cantidad_anios_bisiestos es utilizada para acumular la cantidad de años bisiestos vividos por la persona.

Respuesta 2: 

• Cada variable cumple una función específica dentro del programa y es necesaria para realizar los cálculos correspondientes y almacenar los resultados.

Respuesta 3

• Esta variable es importante porque se utiliza para determinar si cada número del 1 al 9 es múltiplo del número ingresado por el usuario. De esta manera, se puede determinar qué números se deben saltar al ingresar la secuencia de números.
• También se utiliza una variable "i" en el bucle "for" para recorrer los números del 1 al 9. Esta variable es necesaria para llevar un control sobre los números que se están evaluando en cada iteración y para imprimir la secuencia de números en pantalla.
• En resumen, las variables "numero" e "i" son esenciales para el funcionamiento del programa ya que se utilizan para tomar decisiones y controlar el flujo del programa.






'''

################################################################
# Importamos la librería datetime para obtener el año actual   #  
################################################################

import datetime 

##############################################
# Pedimos al usuario el año de nacimiento    #  
##############################################

fecha_nacimiento = int(input("Ingresa el año de nacimiento: "))


#########################################################################
# Pedimos al usuario el año de muerte (o 0 si aún está viva) #  #            
#########################################################################

fecha_muerte = int(input("Ingresa el año de muerte (o 0 si aún está viva): "))

#########################################################################
# Si la persona está viva, asignamos el año actual como su año de muerte. #          
#########################################################################

if fecha_muerte == 0:
    fecha_muerte = datetime.datetime.now().year

########################################################################
# Creamos una variable para almacenar la cantidad de años bisiestos    #            
########################################################################

cantidad_fecha_bisiestos = 0

###############################################################
# Iteramos desde el año de nacimiento hasta el año de muerte  #            
###############################################################

for fecha in range(fecha_nacimiento, fecha_muerte+1):

#######################################################################################
 # Si el año es bisiesto, sumamos 1 a la variable cantidad_fecha_bisiestos = 0        #
#######################################################################################

    if (fecha % 4 == 0 and fecha % 100 != 0) or fecha % 400 == 0:
        cantidad_fecha_bisiestos += 1
#######################################################################################################
#  # Si el usuario ingresa un número incorrecto, se muestra un mensaje de error y se rompe el bucle.  #          
#######################################################################################################

print("La cantidad de años bisiestos que ha vivido la persona es:", cantidad_fecha_bisiestos)
######################################################
# Mostramos la cantidad de años bisiestos calculados #        
######################################################

