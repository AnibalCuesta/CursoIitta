# Coleio 
alumnos = {
    "31130649": {
        "Nombre": "Anibal", 
        "Apellido" : "Cuesta", 
        "Fecha_Nac": "09-06-1985",  
        "Tutor" :"Maria Dana", 
        "Notas" : [5,6,10], 
        "Faltas" : 10, 
        "amonestaciones": 5},
    "37152369":{
        "Nombre": "Marcelo", 
        "Apellido" : "Hernandez", 
        "Fecha_Nac": "09-06-1995",  
        "Tutor" :"Maria Dana", 
        "Notas" : [5,6,10], 
        "Faltas" : 10, 
        "amonestaciones": 5},
    "25369345":{
        "Nombre": "Juan", 
        "Apellido" : "Riquelme", 
        "Fecha_Nac": "25-08-1999",  
        "Tutor" :"Maria Enriqueta", 
        "Notas" : [5,6,10], 
        "Faltas" : 10, 
        "amonestaciones": 5},
    "36852369":{
        "Nombre": "Lautaro", 
        "Apellido" : "Blasco", 
        "Fecha_Nac": "09-08-2010",  
        "Tutor" :"Maria Dana", 
        "Notas" : [5,6,10], 
        "Faltas" : 10, 
        "amonestaciones": 5}
}

for dni, datos in alumnos.items():
    print("DNI {}:{}".format(dni,datos["Nombre"]))

