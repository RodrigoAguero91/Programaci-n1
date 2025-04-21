 #1. Crear una función llamada imprimir_hola_mundo que imprima por
 #pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
 #programa principal.

def imprimir_hola_mundo():
        print("Hola Mundo!")
        
imprimir_hola_mundo()

#2. Crear una función llamada saludar_usuario(nombre) que reciba
#como parámetro un nombre y devuelva un saludo personalizado.
#Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de
#volver: “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.

def saludar_usuario(nombre):
        return (f"Hola {nombre}!")
nombre=input("Ingrese su nombre:")

print(saludar_usuario(nombre))

# 3. Crear una función llamada informacion_personal(nombre, apellido,
#edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal(nombre, apellido,edad, residencia):
        return(f"Soy {nombre} {apellido},tengo {edad} años y vivo en {residencia} .")

nombre=input("Ingrese su nombre:")
apellido=input("Ingrese su apellido:")
edad=input("Ingrese su edad:")
residencia=input("Ingrese su residencia:")

print(informacion_personal(nombre, apellido,edad, residencia))

#4. Crear dos funciones: calcular_area_circulo(radio) que reciba el ra
#dio como parámetro y devuelva el área del círculo. calcular_peri
#metro_circulo(radio) que reciba el radio como parámetro y devuel
#va el perímetro del círculo. Solicitar el radio al usuario y llamar am
#bas funciones para mostrar los resultados.

import math
pi=math.pi

def calcular_area_circulo(radio):
      A= pi * (radio*radio)
      return A
def calcular_perimetro_circulo(radio):
        P= 2*pi*radio
        return P
radio =float(input("Ingrese un numero:"))
print(f"El radio del circulo es: {radio}")
print(f"El area del ciculo es: {calcular_area_circulo(radio)}")
print(f"El perimetro del circulo es: {calcular_perimetro_circulo(radio)}")

#5. Crear una función llamada segundos_a_horas(segundos) que reciba
#una cantidad de segundos como parámetro y devuelva la cantidad
#de horas correspondientes. Solicitar al usuario los segundos y mos-
#trar el resultado usando esta función.

import math

def segundos_a_horas(segundos):
    hora = math.trunc(segundos / 3600)
    min = math.trunc((segundos - (hora * 3600)) / 60)
    segundos = math.trunc(segundos - ((hora * 3600) + (min * 60)))
    return hora, min, segundos

segundos = int(input("Ingrese segundos para calcular cuántas horas son: "))
hora, min, seg = segundos_a_horas(segundos)

print(f"Las horas es {hora}:{min}:{seg} hrs.")

#6. Crear una función llamada tabla_multiplicar(numero) que reciba un
#número como parámetro y imprima la tabla de multiplicar de ese
#número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero):
    for i in range(1, 11):  
        res = numero * i
        print(f"{numero} x {i} = {res}") 

numero = int(input("Ingrese un número para obtener su tabla de multiplicar: "))
tabla_multiplicar(numero)

#7. Crear una función llamada operaciones_basicas(a, b) que reciba
#dos números como parámetros y devuelva una tupla con el resulta-
#do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re-
#sultados de forma clara.

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b != 0:
        division = a / b
    else:
        division = "división por cero no permitida"
    return (suma, resta, multiplicacion, division)

a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))


resultados = operaciones_basicas(a, b)

print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")

#8. Crear una función llamada calcular_imc(peso, altura) que reciba el
#peso en kilogramos y la altura en metros, y devuelva el índice de
#masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun-
#ción para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
    imc=peso / (altura**2)
    return round(imc,2)

peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

resultado_imc = calcular_imc(peso, altura)

print(f"Su Índice de Masa Corporal (IMC) es: {resultado_imc}")

#9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
#una temperatura en grados Celsius y devuelva su equivalente en
#Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
#resultado usando la función.

def  celsius_a_fahrenheit(celsius):
        fahrenheit = (celsius * 9/5) + 32
        return round(fahrenheit, 2)

celsius = float(input("Ingrese la temperatura en grados Celsius: "))
resultado_fahrenheit = celsius_a_fahrenheit(celsius)
print(f"La temperatura en Fahrenheit es: {resultado_fahrenheit}")


#10.Crear una función llamada calcular_promedio(a, b, c) que reciba
#tres números como parámetros y devuelva el promedio de ellos.
#Solicitar los números al usuario y mostrar el resultado usando esta
#función.

def  calcular_promedio(a, b, c):
        promedio=(a+b+c)/3
        return round(promedio,2)

a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))

resultado_promedio = calcular_promedio(a, b, c)

print(f"El promedio de los números ingresados es: {resultado_promedio}")