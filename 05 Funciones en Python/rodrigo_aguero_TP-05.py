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