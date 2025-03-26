#Alumno: Rodrigo Aguero
#Comision:23

# 1)Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”. 
print("Hola mundo!");

#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando 
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir 
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para 
# realizar la impresión por pantalla.

nombre = input("Escriba su nombre:");
print(f"Hola {nombre}")

# 3) 3Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e 
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa 
# Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar 
# la impresión por pantalla. 

nombre = input("Escriba su nombre:");
apellido = input("Escriba su apellido:");
edad = input("Escriba su edad:");
residencia = input("Escriba su residencia:");
print(f"Hola soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y 
#su perímetro. 

import math
print("calcular el radio de un circulo:");
radio = float(input("Ingrese el radio de un circulo: "))
area = math.pi * (radio**2)
Perimetro = 2 * radio * math.pi 

print(f"el area del circulo es : {area}");
print(f"el perimetro del ciculo es: {Perimetro}");


#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a 
#cuántas horas equivale. 

segundos = input("Ingrese cantidad de segundos:");
segundos = int(segundos);
horas = segundos//3600
sobrantes1= segundos%3600
minutos=sobrantes1//60
sobrantes2= sobrantes1%60
print(f"{segundos} equivale a {horas}h:{minutos}m:{sobrantes2}s")

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de 
#multiplicar de dicho número. 

numero = int(input("Escribir un numero:"));
for i in range(0,11):
    resultado= i * numero
    print(numero, "X", i, "=", resultado)

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por 
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos 

print("Ingrese un numero:");
num1= int(input());
print("Ingreses otro numero:");
num2= int(input());

suma= num1 + num2;
resta= num1 - num2;
mult= num1 * num2;
div= num1 / num2;

print(f"La suma de los dos numeros es: {suma}")
print(f"La resta de los dos numeros es: {resta}")
print(f"La multiplicacion de los dos numeros es: {mult}")
print(f"La division de los dos numeros es: {div}")

 #8)Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice 
#de masa corporal. 

altura= float(input("ingresa tu altura:"));
peso= float(input("ingresa tu peso:"));
masa_corporal= peso / (altura * altura)
print(f"Tu masa corporal es de : {masa_corporal}")

#9)Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por 
#pantalla su equivalente en grados Fahrenheit.

grados_celsius= float(input("Ingrese grados de temperatura:"))
grados_fahrenheit= 9/5 * grados_celsius + 32
print(f"La temperatura {grados_celsius} celsius es igual a {grados_fahrenheit} en grados fahrenheit ")

#10) Crear un programa que pida al usuario  3 números e imprima por pantalla el promedio de 
#dichos números. 

num1=float(input("Ingrese un primer numero:"))
num2=float(input("Ingrese un segundo numero:"))
num3=float(input("Ingrese un tercer numero:"))

suma= num1 + num2 + num3
promedio= suma / 3

print(f"El promedio de la suma de los tres numeros es: {promedio}")
