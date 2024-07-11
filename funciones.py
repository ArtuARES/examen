import random
import os
import msvcrt
import time
import csv
trabajadores = ["Juan Pérez", "Maria Garcia", "Carlos López", "Ana Martinez", "Pedro Rodriguez", "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]
sueldos_base=[]
suel_bajo=[]
suel_medio=[]
suel_alto=[]
suel_800=[800000]
suel_8002=[800000, 2000000]
suel_2=[2000000, 2500000]
def opc_1():
    for x in range(10):
        aleatorio=random.randint(300000, 2500000)
        sueldos_base.append(aleatorio)
    if sueldos_base<suel_800:
        suel_bajo.append(sueldos_base)
        print(suel_bajo)
        
    elif sueldos_base>=suel_8002 and sueldos_base==suel_8002:
        suel_medio.append(sueldos_base)
        print(suel_medio)
        
    elif sueldos_base>suel_2:
        suel_alto.append(sueldos_base)
        print(suel_alto)
        
    print("Sueldos asignados correctamente!")
    print("Presione una tecla para continuar!")
    msvcrt.getch()   
def opc_2():
    print(f"Sueldos menores a $800.000 Total:",)
    print(f"""Nombre empleado      Sueldo""",
             trabajadores,      "$",suel_bajo)

    print(f"""Sueldos entre $800.000 y $2.000.000
          Total:""",)
    print(f"""Nombre empleado      Sueldo""",
             trabajadores,       "$",suel_medio)
    

    print(f"""Sueldos superiores a $2.000.000 
        Total:""", )
    print(f"""Nombre empleado      Sueldo""",
             trabajadores,      "$",suel_alto)
    
    Total=suel_alto+suel_bajo+suel_medio
    print(f"TOTAL SUELDOS: $",Total)
    print("Presione una tecla para continuar!")
    msvcrt.getch()
def opc_3():
    print("Sueldo mas alto:",)
    print("Sueldo mas bajo: ",)
    print("Promedio de sueldos: ",)
    print("Media geometrica: ", )
    print("Presione una tecla para  continuar!")
    msvcrt.getch()
def opc_4():        
    total=sueldos_base
    des_salud=sueldos_base/0.07
    des_afp= sueldos_base/0.12
    sue_liquido=total-des_salud-des_afp
    print("""Nombre empleado    Sueldo Base     Descuento Salud     Descuento AFP     Sueldo Líquido
    """,     trabajadores,    "$",total,    "$",des_salud,    "$",des_afp,   "$",sue_liquido)  