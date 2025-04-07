#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

#for numeros in range(101):
 #   print(numeros)

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.

#numero=int(input("Ingrese un numero entero:"))
#i=0

#while numero > 0 :
 #   numero= numero // 10
  #  i += 1
#print(f"El numero ingresado tiene {i} digitos.") 

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

#num_1=int(input("Ingresar primer numero:"))
#num_2=int(input("Ingresar segundo numero:"))

#if num_1 > num_2:
 #   mayor= num_1
  #  menor= num_2
#else:
 #   mayor= num_2
  #  menor= num_1
#suma=0

#while mayor >= menor:
 #   suma= suma + mayor
  #  mayor= mayor -1 
#print(f"la suma entre los valores es {suma}")

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.

#num=int(input("Ingrese numeros (hasta ingresar 0 para terminar):"))

#suma= 0

#while num != 0:    
 #   suma= suma + num
  #  num=int(input("Ingrese numeros (hasta ingresar 0 para terminar):"))
#print(f"la suma de los numeros es {suma}")

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número

import random
num=int(input("ingrese un numero entre el 0 y 10:"))
num_aleatorio=random.randint(0,9)
intentos=0

while num != num_aleatorio:
    num=int(input("ingrese un numero entre el 0 y 10:"))
    intentos += 1
print(f"Has necesitado {intentos} intentos.")