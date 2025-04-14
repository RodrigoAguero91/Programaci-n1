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

#import random
#num=int(input("ingrese un numero entre el 0 y 9:"))
#num_aleatorio=random.randint(0,9)
#intentos=0

#while num != num_aleatorio:
 #   num=int(input("ingrese un numero entre el 0 y 0:"))
  #  intentos += 1
#print(f"Has necesitado {intentos} intentos.")

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
#entre 0 y 100, en orden decreciente.
#num=int(input("imprimir los numeros pares de 100 a 0 :"))
#for num in range(100,0,-2):
 #    print(num)

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
#número entero positivo indicado por el usuario. 

#num=int(input("Escribir un numero entero:"))

#if num < 0:
 #  print("el numero debe ser positivo")
#else:
 #  suma=0
  # for i in range(num+1):
   #      suma= suma+i
#print(suma)

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
#menor, pero debe estar preparado para procesar 100 números con un solo cambio). 
#pares=0
#impares=0
#pos=0
#neg=0


#for i in range(1,101):
 #   num=int(input("ingrese 100 numeros enteros:"))
  #  if num% 2==0 :
    #    pares= pares+1
   # else:
     #   impares=impares+1
   # if num>0:
    #    pos=pos+1
    #elif  num<0:
     #   neg=neg+1

#print(f"hay {pares} pares.")
#print(f"hay {impares} impares.")
#print(f"hay {pos} positivos.")
#print(f"hay {neg} negativos.")

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
#poder procesar 100 números cambiando solo un valor). 

#num=0
#cantidad=100
#suma=0

#for i in range(cantidad):
 # num= int(input("Escriba un numero:"))
  #suma=suma+num

#media=suma/cantidad
#print(f"La media es {media}")

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

num=0
digito=0
inverso=0
num=int(input("Escribir un numero:"))

while num!=0:
    digito=num%10
    inverso=inverso*10+digito
    num=num//10
print(f"El numero invertido es:{inverso}")

