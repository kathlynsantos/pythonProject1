class NumerosComplexos:

    def __init__(self, numComp1, numComp2, numComp3):
        self.numComp1 = numComp1
        self.numComp2 = numComp2
        self.numComp3 = numComp3

    def soma(self):
        return print(self.numComp1 + self.numComp2 + self.numComp3)

    def subtracao(self):
        return print(self.numComp1 - self.numComp2 - self.numComp3)

    def multiplicao(self):
        return print(self.numComp1 * self.numComp2 * self.numComp3)

    def divisao(self):
        return print(self.numComp1 / self.numComp2 / self.numComp3)

    def mostrarParteReal(self):
        return print(self.numComp1.real, " ", self.numComp2.real, " ", self.numComp3.real)

    def mostrarParteImaginaria(self):
        return print(self.numComp1.imag, " ", self.numComp2.imag, " ", self.numComp3.imag)


numerosComplexos = NumerosComplexos(complex(10, 5), complex(6, 3), complex(2, 1))

numerosComplexos.soma()
numerosComplexos.subtracao()
numerosComplexos.multiplicao()
numerosComplexos.divisao()

numerosComplexos.mostrarParteReal()
numerosComplexos.mostrarParteImaginaria()



