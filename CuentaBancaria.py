class CuentaBancaria:
    todas_cuentas = []
    def __init__(self, balance = 0, tasa_interes= 0.01 ):
        self.balance = balance
        self.tasa_interes = tasa_interes
        CuentaBancaria.todas_cuentas.append(self)
    
    def deposito(self, amount):
        self.nuevoBalance = self.balance + amount
        self.balance = self.nuevoBalance
        print("---Depósito---")
        print(self.balance)
        return self
    
    def retiro(self, amount):
        self.nuevoBalance = self.balance - amount
        self.balance = self.nuevoBalance
        print("---Retiro---")
        print(self.balance)
        return self
    
    def generar_interes(self):
        if self.balance > 0:
            print("---Interés Generado---")
            self.nuevoBalance = self.balance * self.tasa_interes
            print("Se ha generado: " + str(self.nuevoBalance) + " de intereses")
            self.balance = self.nuevoBalance + self.balance
            print("El nuevo balance es de: " + str(self.balance))
        else:
            print("No se cuenta con balance suficiente para generar interés")
        return self
    
    def mostrar_info_cuenta(self):
        print("---Info de la Cuenta---")
        print("La cuenta tiene " + str(self.balance))
        print("La tasa de interés es de: " + str(self.tasa_interes))
    
    # @classmethod
    # def informacion_global(cls):
    #     print(todas_cuentas())