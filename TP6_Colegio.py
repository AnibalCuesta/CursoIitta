# Coleio 
alumnos = {
    "31130649": {
        "Nombre": "Anibal", 
        "Apellido" : "Cuesta", 
        "Fecha_Nac": "09-06-1985",  
        "Tutor" :"Maria Dana", 
        "Notas" : [5,6,10], 
        "Faltas" : 10, 
        "Amonestaciones": 5},
    "37152369":{
        "Nombre": "Marcelo", 
        "Apellido" : "Hernandez", 
        "Fecha_Nac": "09-06-1995",  
        "Tutor" :"Maria Juana", 
        "Notas" : [5,5,8], 
        "Faltas" : 9, 
        "Amonestaciones": 5},
    "25369345":{
        "Nombre": "Juan", 
        "Apellido" : "Riquelme", 
        "Fecha_Nac": "25-08-1999",  
        "Tutor" :"Maria Enriqueta", 
        "Notas" : [5,6,1], 
        "Faltas" : 5, 
        "Amonestaciones": 5},
    "36852369":{
        "Nombre": "Lautaro", 
        "Apellido" : "Blasco", 
        "Fecha_Nac": "09-08-2010",  
        "Tutor" :"Paula Valdiviezo", 
        "Notas" : [9,5,10], 
        "Faltas" : 1, 
        "Amonestaciones": 0}
}

def alta(DNI,alumnos):
    lista=[]
    lista=["Nombre","Apellido","Fecha_Nac","Tutor"]
    alumnos[DNI]={}
    for dato in lista:
        valor=input("Ingrese el "+dato+" del Alumno")
        alumnos[DNI][dato]=valor
    alumnos[DNI]["Notas"]=""
    alumnos[DNI]["Faltas"]=""
    alumnos[DNI]["Amonestaciones"]=""
    return alumnos

def baja(DNI,alumnos):
    del alumnos[DNI]
    return alumnos

def modifica(DNI,alumnos):
    opc=input("Si desea cambiar un Dato personal Seleccione M si desea agregar notas, faltas o amonestaciones A")
    if opc.upper()=="M":
        dato=input("Indique que Dato desea Modificar, puede ser el Nombre, Apellido, Fecha_Nac o Tutor")
        valor=input("Escriba el Nuevo "+dato+" del Alumno")
        alumnos[DNI][dato]=valor
    elif opc.upper()=="A":
        dato=input("para Agregar Notas seleccione N, para cambiar las amonestaciones A, para cambiar las Faltas F")
        if dato.upper()=="N":
            valor=str(input("ingrese la nota para agregar "))
            alumnos[DNI]["Notas"].append(valor)
        elif dato.upper()=="A":
            valor=str(input("ingrese la nota para agregar "))
            alumnos[DNI]["Amonestaciones"]=valor
        elif dato.upper()=="F":
            valor=str(input("ingrese la nota para agregar "))
            alumnos[DNI]["Faltas"]=valor
        else:
            print("La opción seleccionada no existe")
    else:
        print("La opcion no existe")

    return alumnos

for dni, datos in alumnos.items():
    print("DNI {}:{},{},Fecha Nac.{},Tutor: {}, Notas {}, Faltas {}, Amonestaciones {}".format(dni,datos["Nombre"],datos["Apellido"],datos["Fecha_Nac"],datos["Tutor"],datos["Notas"],datos["Faltas"],datos["Amonestaciones"]))

while True:
    band=0

    selec=input("Ingrese la tarea que desea Realizar: para Altas A, Bajas B, Modificacion de datos M, para Salir S")
    if selec.upper()=="A": # en este if es para el ALTA DE DATOS
        DNI=input("ingrese el DNI del Nuevo Alumno")
        for clave in alumnos.keys():
            if clave==DNI:
                print("El Alumno ya existe en la base")
                band=1
                break
        if band==0:  
            alumnos=alta(DNI,alumnos)
            print("el Alumno ",DNI,alumnos[DNI]["Nombre"],alumnos[DNI]["Apellido"],"fue dado de alta")
    elif selec.upper()=="B": # en este if es para la BAJA DE DATOS
        DNI=input("ingrese el DNI del Alumno que desea dar de Baja")
        for clave in alumnos.keys():
            if clave==DNI:
                band=1
                break
        if band==1:
            alumnos=baja(DNI,alumnos)
            print("La Baja del DNI",DNI," se realizo correctamente")
        else:
            print("El DNI ingresado no existe en la Base")

    elif selec.upper()=="M": # en este if es para la MODIFICACION DE DATOS
        DNI=input("ingrese el DNI del Alumno que desea Modificar")
        for clave in alumnos.keys():
            if clave==DNI:
                band=1
                break
        if band==1:
            alumnos=modifica(DNI,alumnos)
            nombre=alumnos[DNI]["Nombre"]
            apellido=alumnos[DNI]["Apellido"]
            print("el Alumno ",str(DNI),nombre,apellido,"fue Modificado")
        else:
            print("El Alumno que desea modificar no existe en la base")

    elif selec.upper()=="S":
        break
    else:
        print("La opcion Seleccionada no Existe")


for dni, datos in alumnos.items():
    print("DNI {}:{},{},Fecha Nac.{},Tutor: {}, Notas {}, Faltas {}, Amonestaciones {}".format(dni,datos["Nombre"],datos["Apellido"],datos["Fecha_Nac"],datos["Tutor"],datos["Notas"],datos["Faltas"],datos["Amonestaciones"]))
