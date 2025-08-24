class Vehiculo:
    def __init__(self, Fecha_Fabricacion, VIN_Chasis, VIN_Motor):
        self.Fecha = Fecha_Fabricacion
        self.VIN_Chasis = VIN_Chasis
        self.VIN_Motor = VIN_Motor

    def get_Fecha_Fabricacion(self):
        return self.Fecha   
    
    def get_VIN_Chasis(self):
        return self.VIN_Chasis
    
    def get_VIN_Motor(self):
        return self.VIN_Motor
    
    
