# Alunos:
#        Aleff Lohan
#        Elis Vitória

class IngressoCinema:
    def __init__(self, data, sala, valor):
        self.data = data
        self.sala = sala
        self.valor = valor
        
    def getData(self):
        return self.data
    
    def setData(self):
        data = input("Digite a data: ")
        self.data = data

    def getSala(self):
        return self.sala
    
    def setSala(self):
        sala = int(input("Digite a sala: "))
        self.sala = sala
    
    def getValor(self):
        return self.valor
    
    def setValor(self):
        valor = float(input("Digite o valor: "))
        self.valor = valor

    def calcularDesconto(self, idade):
        if 16 > idade > 11:
            self.valor = self.valor * (40/100)
        elif 21 > idade > 15:
            self.valor = self.valor * (30/100)
        elif idade > 20:
            self.valor = self.valor * (20/100)
        else:
            print("Não há desconto.")
            return
        
        print(f"O valor do seu desconto é {IngressoCinema.getValor(self)}")

class TestarIngresso:
    def main():
        data = input("Digite a data: ")
        sala = int(input("Digite a sala: "))
        valor = float(input("Digite o valor: "))
        ingresso = IngressoCinema(data, sala, valor)

        idade = int(input("Digite a idade: "))
        IngressoCinema.calcularDesconto(ingresso, idade)

        IngressoCinema.setSala(ingresso)

        print("Nova sala:", ingresso.getSala())

if __name__ == "__main__":
    TestarIngresso.main()

sessao01 = IngressoCinema("14/02", 9, 32)
IngressoCinema.calcularDesconto(sessao01, 13)
IngressoCinema.setSala(sessao01)
IngressoCinema.getSala(sessao01)