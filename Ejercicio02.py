class Vendedor:
    def __init__(self, nombreCompleto, rut, edad, domicilio, correoElectronico, sueldoBase, totalVentas, porcentajeComision):
        self.nombreCompleto = nombreCompleto
        self.rut = rut
        self.edad = edad
        self.domicilio = domicilio
        self.correoElectronico = correoElectronico
        self.sueldoBase = sueldoBase
        self.totalVentas = totalVentas
        self.porcentajeComision = porcentajeComision

    def getNombreCompleto(self):
        return self.nombreCompleto

    def getRut(self):
        return self.rut

    def getEdad(self):
        return self.edad

    def getDomicilio(self):
        return self.domicilio

    def getCorreoElectronico(self):
        return self.correoElectronico

    def getSueldoBase(self):
        return self.sueldoBase

    def getTotalVentas(self):
        return self.totalVentas

    def getPorcentajeComision(self):
        return self.porcentajeComision

    def calcularIngresoTotal(self):
        sueldo_base = self.getSueldoBase()
        total_ventas = self.getTotalVentas()
        porcentaje_comision = self.getPorcentajeComision()
        ingreso_total = sueldo_base + total_ventas * porcentaje_comision
        return ingreso_total

    def __str__(self):
        return (
            f" Datos del Vendedor       \n"
            f"Nombre Completo de Vendedor: {self.getNombreCompleto()}\n"
            f"RUT: {self.getRut()}\n"
            f"Edad: {self.getEdad()} Años\n"
            f"Domiciliado en: {self.getDomicilio()}\n"
            f"Correo Electrónico: {self.getCorreoElectronico()}\n"
            f"Sueldo Base: {self.getSueldoBase()}\n"
            f"Total Ventas: {self.getTotalVentas()}\n"
            f"Porcentaje de Comisión: {self.getPorcentajeComision()}\n"
            f"Ingreso Total: {self.calcularIngresoTotal()}\n"
        )

vendedor1 = Vendedor(
    nombreCompleto="Camila Herrera",
    rut="13.456.789-0",
    edad=27,
    domicilio="Av. Macul 2020, Santiago",
    correoElectronico="camila.herrera@ventas.cl",
    sueldoBase=500000,
    totalVentas=3000000,
    porcentajeComision=0.05
)

print(vendedor1)