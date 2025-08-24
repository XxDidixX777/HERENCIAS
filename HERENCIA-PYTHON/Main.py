from  Clases.Automovil import Automovil

auto = Automovil("2020-06-12", "2HMC8230923J0239",
                 "7779340394AJDS", "Chevrolet", "Camaro", 5000000)


def mostrar_Datos(self):
    print(f"Fecha de Fabricación: {self.get_Fecha_Fabricacion()}")
    print(f"VIN Chasis: {self.get_VIN_Chasis()}")
    print(f"VIN Motor: {self.get_VIN_Motor()}")
    print(f"Marca: {self.marca}")
    print(f"Modelo: {self.modelo}")
    print(f"Precio: {self.precio}")


auto.mostrar_Datos()