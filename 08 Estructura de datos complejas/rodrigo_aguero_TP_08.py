#1) Dado el diccionario precios_frutas 
#precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 
#1450} 
#Añadir las siguientes frutas con sus respectivos precios: 
#● Naranja = 1200 
#● Manzana = 1500 
#● Pera = 2300 

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)


#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
#desarrollado en el punto anterior, actualizar los precios de las siguientes frutas: 
#● Banana = 1330 
#● Manzana = 1700 
#● Melón = 2800

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450, 
                  'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300}

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

#3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
#desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas 
#sin los precios.

precios_frutas = {'Banana': 1330, 'Ananá': 2500, 'Melón': 2800, 'Uva': 1450, 
                  'Naranja': 1200, 'Manzana': 1700, 'Pera': 2300}

lista_frutas = list(precios_frutas.keys())
print(lista_frutas)

#4) Escribí un programa que permita almacenar y consultar números telefónicos. 
#• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor. 
#• Luego, pedí un nombre y mostrale el número asociado, si existe.

agenda = {
    "Juan":"12345", "Ana":"5485866","Pedro":"12345", "Sol":"5485866","Lucia":"56783"
}

for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
    numero = input(f"Ingrese el número de {nombre}: ")
    agenda[nombre] = numero 

consulta = input("Ingrese el nombre del contacto que desea buscar: ")

if consulta in agenda:
    print(f"El número de {consulta} es: {agenda[consulta]}")
else:
    print("Ese contacto no existe en la agenda.")

#5) Solicita al usuario una frase e imprime: 
#• Las palabras únicas (usando un set). 
#• Un diccionario con la cantidad de veces que aparece cada palabra. 


frase = input("Ingrese una frase: ")
palabras = frase.split()
palabras_unicas = set(palabras)

frecuencia_palabras = {}
for palabra in palabras:
    frecuencia_palabras[palabra] = frecuencia_palabras.get(palabra, 0) + 1

print("\nPalabras únicas:", palabras_unicas)
print("\nFrecuencia de palabras:", frecuencia_palabras)

#6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. 
#Luego, mostrá el promedio de cada alumno.

alumnos = {
    "Sofia":(10,9,8),
    "Luis":(6,7,7),
    "Rodrigo":(7,8,9)
}
for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    notas = tuple(map(float, input(f"Ingrese 3 notas de {nombre}, separadas por espacio: ").split()))
    alumnos[nombre] = notas  

print("\nPromedios de los alumnos:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")

#7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 
#y Parcial 2: 
#• Mostrá los que aprobaron ambos parciales. 
#• Mostrá los que aprobaron solo uno de los dos. 
#• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).


aprobados_parcial1 = {101, 102, 103, 104, 105, 106}
aprobados_parcial2 = {104, 105, 106, 107, 108, 109}

aprobados_ambos = aprobados_parcial1 & aprobados_parcial2
aprobados_solo_uno = aprobados_parcial1 ^ aprobados_parcial2
aprobados_total = aprobados_parcial1 | aprobados_parcial2

print("Estudiantes que aprobaron ambos parciales:", aprobados_ambos)
print("Estudiantes que aprobaron solo uno de los dos:", aprobados_solo_uno)
print("Lista total de estudiantes que aprobaron al menos un parcial:", aprobados_total)

#8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. 
#Permití al usuario: 
#• Consultar el stock de un producto ingresado. 
#• Agregar unidades al stock si el producto ya existe. 
#• Agregar un nuevo producto si no existe.

stock_productos = {}
def consultar_stock(producto):
    if producto in stock_productos:
        print(f"Stock de {producto}: {stock_productos[producto]} unidades")
    else:
        print(f"{producto} no está registrado en el inventario.")

def modificar_stock(producto, cantidad):
    if producto in stock_productos:
        stock_productos[producto] += cantidad
        print(f"Se agregaron {cantidad} unidades a {producto}. Nuevo stock: {stock_productos[producto]}")
    else:
        stock_productos[producto] = cantidad
        print(f"{producto} ha sido agregado con un stock inicial de {cantidad} unidades.")

while True:
    print("\nMenú de opciones:")
    print("1 - Consultar stock")
    print("2 - Modificar stock")
    print("3 - Salir")

    opcion = input("Elija una opción: ")

    if opcion == "1":
        producto = input("Ingrese el nombre del producto a consultar: ")
        consultar_stock(producto)
    elif opcion == "2":
        producto = input("Ingrese el nombre del producto: ")
        cantidad = int(input(f"Ingrese la cantidad de unidades a agregar para {producto}: "))
        modificar_stock(producto, cantidad)
    elif opcion == "3":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida, por favor intente nuevamente.")

#9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.

agenda = {
    ("Lunes", "10:00"):"Reunión de equipo",
    ("Martes", "15:30"):"Llamada con cliente",
    ("Viernes", "18:00"): "Clase de yoga",
}

def agregar_evento(dia, hora, evento):
    clave = (dia, hora)  
    agenda[clave] = evento
    print(f"Evento '{evento}' agregado el {dia} a las {hora}.")

def consultar_evento(dia, hora):
    clave = (dia, hora)
    if clave in agenda:
        print(f"Evento programado: {agenda[clave]}")
    else:
        print("No hay evento programado en esa fecha y hora.")

consultar_evento("Martes", "15:30")
consultar_evento("Miércoles", "11:00") 