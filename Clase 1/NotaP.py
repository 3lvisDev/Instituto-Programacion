############################################################################################
#                #                                                               #         #
#            #       #       # Student: Elvis Da Silva                         #    #      #
#         #              #   # Institute Providencia Profesional #          #         #    #
#      #                     # Date: 29/03/2023                   #      #            #   #
#   #                                                                 #                  # #
############################################################################################

###########################################################
#                NOTA LABORATORIO                         #
###########################################################
lab1 = float(input("Ingrese la nota del Laboratorio 1: "))
lab2 = float(input("Ingrese la nota del Laboratorio 2: "))
lab3 = float(input("Ingrese la nota del Laboratorio 3: "))


###########################################################
#        CALCULAR NOTA PROMEDIO DE LABORATOR              #
###########################################################
prom_lab = (lab1 + lab2 + lab3) / 3


###########################################################
#                    NOTA TAREAS                          #
###########################################################
tarea1 = float(input("Ingrese la nota de la Tarea 1: "))
tarea2 = float(input("Ingrese la nota de la Tarea 2: "))
tarea3 = float(input("Ingrese la nota de la Tarea 3: "))

###########################################################
#           CALCULAR NOTA PROMEDIO DE TAREAS              #
###########################################################
prom_tareas = (tarea1 + tarea2 + tarea3) / 3

###########################################################
#                   NOTA SOLEMNES                         #
###########################################################
solemne1 = float(input("Ingrese la nota del Solmene 1: "))
solemne2 = float(input("Ingrese la nota del Solmene 2: "))

###########################################################
#         CALCULAR NOTA PROMEDIO DE PRESENTACION          #
###########################################################
nota_presentacion = prom_lab * 0.15 + prom_tareas * 0.15 + solemne1 * 0.35 + solemne2 * 0.35
###########################################################
#           IMPRIMIR NOTA DE PRESENTACION                 #
###########################################################
print("La nota de presentación es:", nota_presentacion)


