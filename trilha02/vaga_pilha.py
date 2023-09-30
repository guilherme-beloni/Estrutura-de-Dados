#from estacionamento_pilha import Estacionamento
class Estacionamento:
    def __init__(self, carro, placa):
        self.carro = carro
        self.placa = placa
        self.proximo = None
class Vaga:
    def __init__(self):
        self.ultimo = None
        self._quantidadade = 0

    def __repr__(self):
        texto = ''
        aux = self.ultimo
        while (aux):
            texto = texto + f'{str(aux.carro)} - {str(aux.placa)} \n' 
            aux = aux.proximo
        return texto    

    def __str__(self) -> str:
        return self.__repr__()


    def __len__(self):
        return self._quantidadade

    def estacionar(self, carro, placa):
        vaga = Estacionamento(carro, placa)
        vaga.proximo = self.ultimo
        self.ultimo = vaga
        self._quantidadade += 1

    def retirar(self):
        if self._quantidadade > 0:
            vaga = self.ultimo  
            self.ultimo = self.ultimo.proximo
            self._quantidadade -= 1
            return vaga.carro, vaga.placa   
        else:
            return 'Erro!'
        
    def carros_estacionados(self):
        print("Estacionamento A:")
        if self._quantidadade > 0:
            print(f'{self}')
        else:
            print ('Nenhum carro' )   
        
estacioanmentoA = Vaga()
while True:
    print("\nEscolha uma ação:")
    print("1. Estacionar veículo")
    print("2. Retirar veículo")
    print("3. Listar carros estacionados")
    print("4. Sair")

    escolha = input("Digite o número da ação desejada: ")

    if escolha == "1":
        carro = input("Digite o nome do veículo: ")
        placa = input("Digite a placa do veículo: ")
        estacioanmentoA.estacionar(carro, placa)
    elif escolha == "2":
        carro, placa = estacioanmentoA.retirar()
        print(f"Carro retirado: {carro} - Placa: {placa}")
    elif escolha == "3":
        estacioanmentoA.carros_estacionados()
    elif escolha == "4":
        break
    else:
        print("Escolha uma opção válida.")

