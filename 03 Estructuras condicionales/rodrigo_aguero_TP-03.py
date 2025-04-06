#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

usuario= int(input("ingrese su edad:"))

if usuario > 18 :
    print("Es mayor de edad ")
else:
    print("Tiene que tener mas de 18 años")

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”.

nota=int(input("Ingrese su nota:"))

if nota >= 6 :
    print("Aprobado")
else:
    print("Desaprobado")

#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
#operador de módulo (%) en Python para evaluar si un número es par o impar.

num_par=int(input("Ingrese un numero par:"))

if num_par % 2 == 0 :
    print("Ha ingresado un número par")
else :
    print("Por favor, ingrese un número par")

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.

edad=int(input("Ingrese su edad:"))

if edad < 12 :
    print("Usted pertenece a la categoria Niño/a")
elif edad >= 12 and edad < 18:
    print("Usted pertenece a la categoria Adolescente")
elif edad >= 18 and edad < 30 :
    print("Usted pertenece a la categoria Adulto/a joven")
elif edad >= 30 :
    print("Usted pertenece a la categoria Adulto/a")
else:
    print("Dato mal ingresado")

#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
#como una lista o un string.

contraseña=input("Ingrese su contraseña(entre 8 y 14 caracteres):")

if len(contraseña) >= 8 and len(contraseña) <= 14 :
    print("Ha ingresado una contraseña correcta") 
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#6) escribir un programa que tome la lista
#numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
#Definir la lista numeros_aleatorios de la siguiente forma:
#import random
#numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

import random
import statistics
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

moda= statistics.mode(numeros_aleatorios)
mediana= statistics.median(numeros_aleatorios)
media= statistics.mean(numeros_aleatorios)

if media > mediana:
       sesgo= "positivo"
elif media < mediana:
       sesgo= "negativo"
else:
       sesgo= "sin sesgo"

print("Lista de números aleatorios:", numeros_aleatorios)
print("Moda:", moda)
print("Mediana:", mediana)
print("Media:", media)
print("Sesgo:", sesgo)

#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
#pantalla.

vocal=str(input("Escriba una palabra o frase:"))
ultima_letra= vocal[-1]

if ultima_letra.lower() in ["a","e","i","o","u"]:
    print(f"{vocal }!")
else:
    print(f"{vocal }")

#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
#dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
#usuario e imprimir el resultado por pantalla.

nombre=input("Ingrese su nombre:")
numero=int(input("elija un número del 1 al 3 (1. Si quiere su nombre en mayúsculas, 2. Si quiere su nombre en minúsculas,3. Si quiere su nombre con la primera letra mayúscula.) :"))

upper=nombre.upper()
lower=nombre.lower()
title=nombre.title()

if numero == 1:
    print(f"{upper}")
elif numero == 2:
    print(f"{lower}")
elif numero == 3 :
    print(f"{title}")
else:
    print("Numero incorrecto")

#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
#por pantalla:
#● Menor que 3: "Muy leve" (imperceptible).
#● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
#generalmente no causa daños).
#● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
#débiles).
#● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

magnitud=int(input("Ingrese la magnitud de un terremoto(escala de Richter):"))

if magnitud < 3:
    print("Muy leve (imperceptible).")
elif magnitud >= 3 and magnitud < 4:
    print("Leve (ligeramente perceptible).")
elif magnitud >=4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños).")
elif magnitud >=5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles).")
elif magnitud >=6 and magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos).")
elif magnitud >=7:
   print("Extremo (puede causar graves daños a gran escala).")

#10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
#si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio= input("en cuál hemisferio se encuentra (N/S):")
mes=int(input("qué mes del año es(utilice numero del mes):"))
dia=int(input("qué día es:"))

if hemisferio == "N":
    if (mes == 12 and dia >= 21) or mes in [1, 2] or (mes == 3 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or mes in [4, 5] or (mes == 6 and dia <= 20):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or mes in [7, 8] or (mes == 9 and dia <= 20):
        estacion = "Verano"
    elif (mes == 9 and dia >= 21) or mes in [10, 11] or (mes == 12 and dia <= 20):
        estacion = "Otoño"
elif hemisferio == "S":
    if (mes == 12 and dia >= 21) or mes in [1, 2] or (mes == 3 and dia <= 20):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or mes in [4, 5] or (mes == 6 and dia <= 20):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or mes in [7, 8] or (mes == 9 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 9 and dia >= 21) or mes in [10, 11] or (mes == 12 and dia <= 20):
        estacion = "Primavera"
else:
    estacion = "Hemisferio no válido"


print(f"Te encuentras en {estacion}.")