import os
import msvcrt
from funciones import *


while True:
    os.system("cls")
    print(""" Menu de la Aplicación
    1, Asignar sueldos aleatorios
    2, Clasificar sueldos
    3, Ver estadisticas
    4, Reporte de sueldos
    5, Salir del programa""")
    while True:
        try:
            opc=int(input("Ingrese una opción: "))
            if opc in (1,2,3,4,5):
                break
            else:
                print("ERROR OPCIÓN INCORRECTA!")
        except:
            print("ERROR NO INGRESE CARACTERES!")
    if opc==1:
        opc_1()
    elif opc==2:
        opc_2()
    elif opc==3:
        opc_3()
    elif opc==4:
        opc_4()
    else:
        print("Finalizando programa...")
        print("Desarrollado por Arturo Nuñez")
        print("RUT: 21.488.044-K")
        break
