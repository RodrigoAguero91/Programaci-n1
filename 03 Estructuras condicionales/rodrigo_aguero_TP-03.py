#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

#usuario= int(input("ingrese su edad:"))

#if usuario > 18 :
 #   print("Es mayor de edad ")
#else:
 #   print("Tiene que tener mas de 18 años")

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”.

#nota=int(input("Ingrese su nota:"))

#if nota >= 6 :
 #   print("Aprobado")
#else:
 #   print("Desaprobado")

#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
#operador de módulo (%) en Python para evaluar si un número es par o impar.

#num_par=int(input("Ingrese un numero par:"))

#if num_par % 2 == 0 :
 #   print("Ha ingresado un número par")
#else :
   # print("Por favor, ingrese un número par")

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.

#edad=int(input("Ingrese su edad:"))

#if edad < 12 :
    #print("Usted pertenece a la categoria Niño/a")
#elif edad >= 12 and edad < 18:
   # print("Usted pertenece a la categoria Adolescente")
#elif edad >= 18 and edad < 30 :
  #  print("Usted pertenece a la categoria Adulto/a joven")
#elif edad >= 30 :
 #   print("Usted pertenece a la categoria Adulto/a")
#else:
 #   print("Dato mal ingresado")

#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
#como una lista o un string.

#contraseña=input("Ingrese su contraseña(entre 8 y 14 caracteres):")

#if len(contraseña) >= 8 and len(contraseña) <= 14 :
 #   print("Ha ingresado una contraseña correcta") 
#else:
#    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#6) escribir un programa que tome la lista
#numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
#Definir la lista numeros_aleatorios de la siguiente forma:
#import random
#numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

 #  import random
 #  import statistics
 #  numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

 #  moda= statistics.mode(numeros_aleatorios)
 #  mediana= statistics.median(numeros_aleatorios)
 #  media= statistics.mean(numeros_aleatorios)

  # if media > mediana:
    #   sesgo= "positivo"
  # elif media < mediana:
   #    sesgo= "negativo"
  # else:
    #   sesgo= "sin sesgo"

   #print("Lista de números aleatorios:", numeros_aleatorios)
   #print("Moda:", moda)
   #print("Mediana:", mediana)
   #print("Media:", media)
   #print("Sesgo:", sesgo)

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

