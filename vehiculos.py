import csv

class Vehiculo:
    def __init__(self, marca, modelo, n_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.n_ruedas = n_ruedas

#parte final:
    def guardar_datos_csv(self):
        try:
            archivo = open("vehiculos.csv", "a", newline="") #modo "a":append para no sobrescribir
            datos = [(self.__class__, self.__dict__)]
            archivo_csv = csv.writer(archivo)
            archivo_csv.writerows(datos)
            archivo.close()
        except IOError:
            print(f"Error al guardar los datos en el archivo vehiculos.csv")

    def leer_datos_csv(self):
        vehiculos = []
        try:
            archivo = open("vehiculos.csv", "r")
            archivo_csv = csv.reader(archivo)
            for vehiculo in archivo_csv:
                vehiculos.append(vehiculo)
            #archivo.close()
        except FileNotFoundError:
            print("Error, no se encuentra el archivo vehiculos.csv")
        except IOError:
            print(f"Error al leer el archivo vehiculos.csv")
        else:
            for item in vehiculos:
                tipo = str(self.__class__)
            
                if tipo in item:
                    print(f"Lista de Vehiculos {str(type(self).__name__)}")
                    print(item[1])

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, n_ruedas, velocidad, cilindrada):
        super().__init__(marca, modelo, n_ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.n_ruedas} ruedas, {self.velocidad} Km/h, {self.cilindrada} cc."

class Particular(Automovil):
    def __init__(self, marca, modelo, n_ruedas, velocidad, cilindrada, n_puesto):
        super().__init__(marca, modelo, n_ruedas, velocidad, cilindrada)
        self.n_puesto = n_puesto

class Carga(Automovil):
    def __init__(self, marca, modelo, n_ruedas, velocidad, cilindrada, peso):
        super().__init__(marca, modelo, n_ruedas, velocidad, cilindrada)
        self.peso = peso

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, n_ruedas, tipo):
        super().__init__(marca, modelo, n_ruedas)
        self.tipo = tipo

    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.n_ruedas} ruedas, {self.tipo}"

class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, n_ruedas, tipo, motor, cuadro, n_radios):
        super().__init__(marca, modelo, n_ruedas, tipo)
        self.motor = motor
        self.cuadro = cuadro
        self.n_radios = n_radios

    def __str__(self):
        return Bicicleta.__str__(self) + f"Motor: {self.motor}, Cuadro: {self.cuadro}, nro de radios: {self.n_radios}"