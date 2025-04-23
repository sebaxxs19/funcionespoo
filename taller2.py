# Creación de la clase
class Cuentabancaria:

    # Creación de los atributos
    def __init__(self, titular, saldo_inicial):
        # Atributo privado 1
        self.__titular = titular
        # Atributo privado 2
        self.__saldo = saldo_inicial

    # Creación de los métodos
    # Método público - ver saldo
    def ver_saldo(self):
        return f"Saldo de {self.__titular}: ${self.__saldo}"

    # Método público 1 (Depositar dinero)
    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            print(f"Deposito exitoso de ${monto}")
        else:
            print("El monto debe ser positivo.")

    # Método público 2 (Retirar dinero)
    def retirar(self, monto):
        if monto <= self.__saldo:
            self.__saldo -= monto
            print(f"Retiro exitoso de ${monto}")
        else:
            print("Fondos insuficientes o fondo inválido.")

# Creación de los objetos
cuenta1 = Cuentabancaria("Carlos", 1000)
cuenta2 = Cuentabancaria("Ana", 500)

# Salidas o resultados
# Salida 1 --> Ver saldo
print(cuenta1.ver_saldo())

# Salida 2 --> depositan dinero
cuenta1.depositar(200)

# Salida 3 --> Retiran dinero
cuenta1.retirar(100)

# Salida 4 --> Ver nuevo saldo
print(cuenta1.ver_saldo())
