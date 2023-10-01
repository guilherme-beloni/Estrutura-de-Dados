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

    def __str__(self):
        return self.__repr__()


    def __len__(self):
        return self._quantidadade
    
    def estacionar(self, carro, placa):
        estacionamento = Estacionamento(carro, placa)
        self.ultimo = estacionamento

        




# estacionamento = Vaga()

# estacionamento.estacionar('teste', 'teste')
