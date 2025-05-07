class Liquidacion:

    def __init__(self, nombreEmpleado, rut, edad, domicilio, correoElectronico, sueldoBruto, descuentos):
        self.nombreEmpleado = nombreEmpleado
        self.rut = rut
        self.edad = edad
        self.domicilio = domicilio
        self.correoElectronico = correoElectronico
        self.sueldoBruto = sueldoBruto
        self.descuentos = descuentos

    def getNombreEmpleado(self):
        return self.nombreEmpleado
    def getRut(self):
        return self.rut
    def getEdad(self):
        return self.edad
    def getDomicilio(self):
        return self.domicilio
    def getCorreoElectronico(self):
        return self.correoElectronico
    def getSueldoBruto(self):
        return self.sueldoBruto
    def getDescuentos(self):
        return self.descuentos
    def setNombreEmpleado(self, nombreEmpleado):
        self.nombreEmpleado = nombreEmpleado
    def setRut(self, rut):
        self.rut = rut
    def setEdad(self, edad):
        self.edad = edad
    def setDomicilio(self, domicilio):
        self.domicilio = domicilio
    def setCorreoElectronico(self, correoElectronico):
        self.correoElectronico = correoElectronico
    def setSueldoBruto(self, sueldoBruto):
        self.sueldoBruto = sueldoBruto
    def setDescuentos(self, descuentos):
        self.descuentos = descuentos


    def calcularSueldoLiquido(self):
        return self.sueldoBruto - self.descuentos

    def __str__(self):
        return (
            f"Liquidación de: {self.nombreEmpleado} (RUT: {self.rut})\n"
            f"Edad: {self.edad} años\n"
            f"Domicilio: {self.domicilio}\n"
            f"Correo: {self.correoElectronico}\n"
            f"Sueldo Bruto: {self.sueldoBruto}\n"
            f"Descuentos: {self.descuentos}\n"
            f"Sueldo Líquido: {self.calcularSueldoLiquido()}"
        )
liquidacion_ejemplo = Liquidacion(
    nombreEmpleado="Carla Rojas", 
    rut="12.345.678-9", 
    edad=30, 
    domicilio="Av. Providencia 1234, Santiago", 
    correoElectronico="carla.rojas@email.com", 
    sueldoBruto=1000000, 
    descuentos=170000
)

print(liquidacion_ejemplo)














