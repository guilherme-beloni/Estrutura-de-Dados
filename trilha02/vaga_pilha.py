from estacionamento_pilha import Estacionamento

class Vaga:
    def __init__(self):
        self.ultimo = None
        self._quantidadade = 0

    def __repr__(self):
        texto = ''
        aux = self.ultimo
        while (aux):
            texto = texto + str(aux.carro) + '\n'
            aux = aux.proximo
        return texto    

    def __str__(self) -> str:
        return self.__repr__()


    def __len__(self):
        return self._quantidadade

    def estacionar(self, carro):
        vaga = Estacionamento(carro)
        vaga.proximo = self.ultimo
        self.ultimo = vaga
        self._quantidadade += 1

    def retirar(self):
        if self._quantidadade > 0:
            vaga = self.ultimo  
            self.ultimo = self.ultimo.proximo
            self._quantidadade -= 1
            return vaga.carro   
        else:
            return 'Erro!'
        
    def carros_estacionados(self):
        print("Estacionamento A:")
        if self._quantidadade > 0:
            print(f'{self}')
        else:
            print ('Nenhum carro' )   
        
est = Vaga()

est.estacionar('CRV - zxc-432')
est.estacionar('Gol - abc-123')
est.estacionar('Opala - jhj-123')
est.estacionar('CBR - jhg-123')
est.estacionar('Chevette - gfd-123')

est.carros_estacionados()
est.retirar()
est.carros_estacionados()