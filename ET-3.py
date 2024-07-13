# Función asignar sueldos aleatorios

import random

trabajadores = ["Juan Pérez","María García",
            "Carlos López","Ana Martínez","Pedro Rodríguez",
            "Laura Hernández","Miguel Sánchez",
            "Isabel Gómez","Francisco Díaz","Elena Fernández"]

# Generar sueldo aleatorio
dic_sueldos = {}

def sueldos_aleatorios():
    global dic_sueldos
for _ in (range(len(trabajadores))):
    nombre_aleatorio = random.choice(trabajadores)
    sueldo_aleatorio = random.randint(300000, 2500000)
    dic_sueldos[nombre_aleatorio] = sueldo_aleatorio

# Clasificar sueldos:
def clasificar_sueldos():
    #Validación
    if not dic_sueldos:
        print(f"No hay datos de sueldos disponibles. Genere sueldos aleatorios primero.")
        return
    
sueldos_clasificados = sorted(dic_sueldos.items(), key=lambda item:item[1])

#Impresión
print("\n Clasificación de sueldos:")
print(f"Nombre empleado    Sueldo")
for nombre, sueldo in sueldos_clasificados:
    print(f"{nombre:10} | {sueldo:,} |")

#Validación
def ver_estadisticas():
    if not dic_sueldos:
        print(f"No hay datos de sueldos disponibles. Genere sueldos aleatorios primero.")
        return

#Promedio sueldos
sueldo_promedio = sum()



#Menú delprograma
while True:
    print("\n ---Menú del programa---")
    print("1. Asignar sueldos aleatorios")
    print("2. Clasificar sueldos")
    print("3. Reporte de sueldos")
    print("5. Salir del programa")
    opcion = input("Seleccione una alternativa:")
   
    if opcion == 1:
        sueldos_aleatorios()
    elif opcion == 2:
        clasificar_sueldos()
    elif opcion == 3:
        ver_estadisticas()
    elif opcion == 4:
        reporte_sueldos()
    elif opcion == 5:
        print("Salir del programa")
        break
else:  
print("Ingrese opción válida")