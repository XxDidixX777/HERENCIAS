from Clases.Vehiculo import Vehiculo

class Automovil(Vehiculo):
    def __init__(self, Fecha_Fabricacion, VIN_Chasis, VIN_Motor, marca, modelo, precio):
        super().__init__(Fecha_Fabricacion, VIN_Chasis, VIN_Motor)
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

    def mostrar_Datos(self):
        print(f"Fecha de Fabricación: {self.get_Fecha_Fabricacion()}")
        print(f"VIN Chasis: {self.get_VIN_Chasis()}")
        print(f"VIN Motor: {self.get_VIN_Motor()}")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Precio: {self.precio}")
        