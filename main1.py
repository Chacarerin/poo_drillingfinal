#Parte 1

from vehiculos import *



n_evaluados = int(input("Cuantos Vehiculos desea evaluar: "))
print(f"La cantidad de vehículso a evaluar es de {n_evaluados}")
print("Iniciando evaluación")

i=0
lista_datos=[]

for i in range (n_evaluados):

    print(f"Ingrese los datos del automóvil {i+1}")
    marca = input("Inserte la marca del automóvil: ")
    modelo = input("Inserte el modelo: ")
    n_ruedas = int(input("Inserte el número de ruedas: "))
    velocidad = float(input("Inserte la velocidad en km/h: "))
    cilindrada = int(input("Inserte el cilindraje en cc: "))

    n_auto = Automovil(marca, modelo, n_ruedas, velocidad, cilindrada)

    lista_datos.append(n_auto)

print("Imprimiendo por pantalla los Vehiculos: ")

for i in range(n_evaluados):
    print(f"Datos del automovil {i+1}: {lista_datos[i]}")
    
