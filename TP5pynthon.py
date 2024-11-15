#---------------Trajbajo Practico Nº 5----------------
# 1. Escriba una función redondear() que permita redondear un número
# decimal de acuerdo al criterio: Si la parte decimal es mayo 0.5 (por
# ejemplo 3.5), devolver el entero siguiente (en este caso, 4), si no devolver
# el entero inmediatamente anterior.

# def redo(numero):
#     decimal=numero%1
#     if decimal<0.5:
#         numero=int(numero)
#     else:
#         numero=int(numero+1)
#     return numero

# numero=0
# numero=float(input("ingrese un rno "))

# print(redo(numero))

# 2. Coloque el módulo del ejercicio anterior dentro de un paquete. En un
# módulo que esté fuera de ese paquete, cree una función de suma de
# decimales que redondee el resultado haciendo uso de la función
# redondear() del paquete recién creado.

# from redondear import redo 
# def suma(num1,num2):
#     resultado=num1 + num2
#     return redo(resultado)

# print(suma(5,10.8))

# 3. Usando el módulo datetime, escribe un programa que muestre la fecha
# y hora actuales del sistema.

# from datetime import datetime
# fecha=datetime.now()
# #fecha1=fecha.strftime("%d/%m/%y")
# print(fecha)

# 4. Escriba un programa que devuelva un número par al azar entre 2 y 10
# (pista: para comprobar si se pueden generar todos los números, pruebe
# ejecutar el programa dentro de un ciclo infinito).

# import time 
# inicio = time.time()
# import random

# while True:
#     numero=random.randint(2,10)
#     if numero%2 == 0:
#         print(numero)
#         break
# fin=time.time()
# print(fin-inicio)

# 5. Bola mágica: La bola mágica (Magic 8 ball) es un popular juguete usado
# para la adivinación o para buscar consejo. Su mecanismo es muy simple:
# ante una pregunta del usuario, la bola responde con una de 8 posibles
# respuestas:

# import time 
# inicio = time.time()
# import random
# def bola_magica ():
#     respuestas=["Es seguro que sí","Las chances son buenas","Puedes contar con ello","Pregúntame de nuevo más tarde",
# "Concéntrate y pregunta de nuevo","No veo con claridad, intenta de nuevo","Mi respuesta es no","Mis fuentes me dicen que no"]
#     return random.choice(respuestas)

# pregunta=input("Cual es tu Pregunta para la Bola Magica ")

# print("la bola Magica dice que: ",bola_magica())
# fin=time.time()
# print(fin-inicio)

# 6. Encuentre el tiempo de ejecución de los programas de los ejercicios
# anteriores (pista: use el módulo time)

# se realizo en los dos ejercicios anteriores. Se muestra en segundos 

# 7. Sorteo: Escriba un programa que simule un sorteo donde toman uno o 
# más papeles al azar de un pozo para elegir los ganadores.

# import random
# def sorteo():
#     participantes=["Pablo Saravia","Juan Carlos","Pedro Picapiedra","Ulises Bueno","Joaquin sabina","Ignacio perez","Juan Molina","Checo Perez"]
#     return random.choice(participantes)

# while True:
#     seleccion=input("Selcione G para pedir un ganador o X para salir del programa")
#     if seleccion.upper()=="G":
#         print("El Ganador es  ",sorteo())
#     elif seleccion.upper()=="X":
#         break
#     else:
#         print("Elija una opción valida")



# 8. Escriba una función que pida al usuario ingresar su fecha de nacimiento 
# y sea capaz de devolver la cantidad de días desde su nacimiento hasta 
# hoy. 

# def calcula_dia(fechaNac):
#     from datetime import datetime

#     fechaReal=datetime.strptime(fechaNac, "%Y-%m-%d")
#     fechahoy=datetime.now()

#     fecha=fechahoy-fechaReal
#     dias=fecha.days
#     return dias

# fechaNac=input("Ingrese su fecha de Nacimiento con Formato AAAA-MM-DD ")

# print("Los dias Vividos a hoy son: ",calcula_dia(fechaNac))

# 9. Implemente el programa del ejercicio 6 usando un diccionario.