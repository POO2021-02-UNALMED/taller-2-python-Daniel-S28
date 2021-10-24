class Asiento:
    def __init__(self,color,precio,registro):
        self.color=color
        self.precio=precio
        self.registro=registro
    
    def cambiarColor(self,color):
        if (color=="rojo" or color=="verde" or color=="amarillo" or color=="negro" or color=="blanco"):
            self.color=color

class Auto:
    cantidadCreados=0
    def __init__(self,precio,asientos,marca,motor,registro):
        self.precio=precio
        self.asientos=asientos
        self.marca=marca
        self.motor=motor
        self.registro=registro
        
    def cantidadAsientos(self):
        n=0
        for i in asientos:
            if (i!=None):
                n+=1
        return n
    
    def verificarIntegridad(self):
        if (self.registro!=self.motor.registro):
            return "Las piezas no son originales"
        else:
            for i in self.asientos:
                if (i.registro!=self.registro and i!=None):
                    return "Las piezas no son originales"
            return "Auto original"

class Motor:
    def __init__(self,numeroCilindros,tipo,registro):
        self.numeroCilindros=numeroCilindros
        self.tipo=tipo
        self.registro=registro
    
    def cambiarRegistro(self,registro):
        self.registro=registro
    
    def asignarTipo(self,tipo):
        if (tipo=="electrico" or tipo=="gasolina"):
            self.tipo=tipo
