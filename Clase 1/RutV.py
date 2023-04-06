############################################################################################
#                #                                                               #         #
#            #       #       # Student: Elvis Da Silva                         #    #      #
#         #              #   # Institute Providencia Profesional #          #         #    #
#      #                     # Date: 29/03/2023                   #      #            #    #
#   #                                                                 #                  # #
############################################################################################


###########################################################
#                  INGRESO DE RUT                         #
###########################################################
rut = input("Ingrese su RUT sin dígito verificador: ")

###########################################################
#             CONVERTIR EL RUT Y REVERTIR                 #
###########################################################
rut_digitos = list(reversed([int(d) for d in rut]))

###########################################################
#         NUMERO SECUENCIALES DE MUTIPLICADOR             #
###########################################################
secuencia = [2, 3, 4, 5, 6, 7]

#################################################################################
#                                                                               #
#        NUMERO DE MUTIPLICADOR DE RUT POR MULTIPLICACION CORRESPONDIENTE       #
#                                                                               #
#################################################################################
secuencia_repetida = (len(rut_digitos) // len(secuencia)) * secuencia + secuencia[:len(rut_digitos) % len(secuencia)]
prod = [a * b for a, b in zip(rut_digitos, secuencia_repetida)]

###########################################################
#         SUMA DE RESULTADO  DE  LA MUTIPLICADOR          #
###########################################################
suma = sum(prod)
###########################################################
#        CALCULA EL RESTO  DE LA SUMA Y LO DIVIDE         #
###########################################################
resto = suma % 11
if resto == 0:
    verificador = 0
elif resto == 1:
    verificador = "K"
else:
    verificador = 11 - resto

###########################################################
#           MUESTRA DE NUMERO DE RUT COMPLETO             #
###########################################################
rut_con_verifador = rut + "-" + str(verificador)
print("Su RUT completo es:", rut_con_verifador)