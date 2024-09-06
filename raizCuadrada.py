class RaizCuadrada:
    def __init__(self):
        self.number = float(input("Ingrese numero para calcular raiz cuadrada: "))

    def calcular(self):
        raiz = 1.0
        for k in range(1, 10):
            raiz = (raiz + self.number / raiz) / 2
        print(f"La raiz cuadrada de {self.number} es {raiz}")
