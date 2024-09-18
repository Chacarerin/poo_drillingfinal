#Parte2
from vehiculos import *

particular = Particular("Ford", "Fiesta", 4, "180", "500", 5)
carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motocicleta("BMW", "F800s",2,"Deportiva","2T","Doble Viga", 21)

print(particular)
print(carga)
print(bicicleta)
print(motocicleta)

print(f"Motocicleta es instancia con relación a Vehículo: {isinstance(motocicleta, Vehiculo)}")
print(f"Motocicleta es instancia con relación a Automovil: {isinstance(motocicleta, Automovil)}")
print(f"Motocicleta es instancia con relación a Vehículo particular: {isinstance(motocicleta, Particular)}")
print(f"Motocicleta es instancia con relación a Vehículo de Carga: {isinstance(motocicleta, Carga)}")
print(f"Motocicleta es instancia con relación a Bicicleta: {isinstance(motocicleta, Bicicleta)}")
print(f"Motocicleta es instancia con relación a Motocicleta: {isinstance(motocicleta, Motocicleta)}")