class Estacionamento:
    def __init__(self, carro, placa):
        self.carro = carro
        self.placa = placa
        self.proximo = None


class EstacionamentoA:
    def __init__(self):
        self.ultimo = None
        self._quantidade = 0

    def __repr__(self):
        texto = ''
        aux = self.ultimo
        while (aux):
            texto = texto + f'{str(aux.carro)} - {str(aux.placa)} \n'
            aux = aux.proximo
        return texto

    def __str__(self):
        return self.__repr__()

    def __len__(self):
        return self._quantidade

    def estacionar(self, carro, placa):
        vaga = Estacionamento(carro, placa)
        vaga.proximo = self.ultimo
        self.ultimo = vaga
        self._quantidade += 1
        print(f"Veículo {carro} - Placa: {placa} estacionou no Estacionamento A.")

    def retirar(self):
        if self._quantidade > 0:
            vaga = self.ultimo
            self.ultimo = self.ultimo.proximo
            self._quantidade -= 1
            print(f"Carro retirado: {vaga.carro} - Placa: {vaga.placa}")
        else:
            print("Estacionamento A vazio. Nenhum veículo para retirar.")

    def carros_estacionados(self):
        print("Estacionamento A:")
        if self._quantidade > 0:
            print(f'{self}')
        else:
            print ('Estacionamento (A) vazio!')


class EstacionamentoB:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        self._quantidade = 0

    def __repr__(self):
        texto = ''
        aux = self.ultimo
        while (aux):
            texto = texto + f'{str(aux.carro)} - {str(aux.placa)} \n'
            aux = aux.proximo
        return texto

    def __str__(self):
        return self.__repr__()

    def __len__(self):
        return self._quantidade

    def estacionar(self, carro, placa):
        vaga = Estacionamento(carro, placa)
        if self.ultimo is None:
            self.ultimo = vaga
            print(f"Veículo {carro} - Placa: {placa} estacionou no Estacionamento B.")
        else:
            self.ultimo.proximo = vaga
            self.ultimo = vaga

        if self.primeiro is None:
            self.primeiro = vaga

        self._quantidade += 1

    def retirar(self):
        if self._quantidade > 0:
            vaga = self.primeiro
            self.primeiro = self.primeiro.proximo

            if self.primeiro is None:
                self.ultimo = None

            self._quantidade -= 1
            print(f"Carro retirado: {vaga.carro} - Placa: {vaga.placa}")
        else:
            print("Estacionamento B vazio. Nenhum veículo para retirar.")

    def carros_estacionados(self):
        print("Estacionamento B:")
        if self._quantidade > 0:
            aux = self.primeiro  # Começa do primeiro carro
            while aux:
                print(f'Carro: {aux.carro} - Placa: {aux.placa}')
                aux = aux.proximo
        else:
            print('Estacionamento (B) vazio!')


class SistemaEstacionamento:
    def __init__(self):
        self.estacionamento_a = EstacionamentoA()
        self.estacionamento_b = EstacionamentoB()

    def menu(self):
        while True:
            print("\nEscolha uma ação:")
            print("1. Estacionar veículo no Estacionamento A")
            print("2. Retirar veículo do Estacionamento A")
            print("3. Listar carros estacionados no Estacionamento A")
            print("4. Estacionar veículo no Estacionamento B")
            print("5. Retirar veículo do Estacionamento B")
            print("6. Listar carros estacionados no Estacionamento B")
            print("7. Sair")

            escolha = input("Digite o número da ação desejada: ")

            if escolha == "1":
                carro = input("Digite o nome do veículo: ")
                placa = input("Digite a placa do veículo: ")
                self.estacionamento_a.estacionar(carro, placa)
            elif escolha == "2":
                self.estacionamento_a.retirar()
            elif escolha == "3":
                self.estacionamento_a.carros_estacionados()
            elif escolha == "4":
                carro = input("Digite o nome do veículo: ")
                placa = input("Digite a placa do veículo: ")
                self.estacionamento_b.estacionar(carro, placa)
            elif escolha == "5":
                self.estacionamento_b.retirar()
            elif escolha == "6":
                self.estacionamento_b.carros_estacionados()
            elif escolha == "7":
                break
            else:
                print("Escolha uma opção válida.")


if __name__ == "__main__":
    sistema = SistemaEstacionamento()
    sistema.menu()
