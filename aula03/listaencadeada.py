from no import No


class LinkedList:
    def __init__(self):
        self.inicio = None
        self._tamanho = 0


    def __len__(self):
        return self._tamanho

    def __repr__(self):
        pass

    def append(self, info):
        if self.inicio:
            aux = self.inicio
            while(aux.proximo):
                aux = aux.proximo
            aux.proximo = No(info)    
        else:
            self.inicio = No(info)
            self._tamanho += 1

    def __getitem__(self, index):
        aux = self._getNo(index)
        if aux:
            return aux.info
        else:
            raise IndexError('Índice inexistente')

    def __setitem__(self, index, info):
        aux = self._getNo(index)
        if aux:
            aux.info = info
        else:
            raise IndexError('Índice inexistente')

    def _getNo(self, index):
        aux = self.inicio
        for i in range(index):
            if aux:
                aux = aux.proximo
            else:
                return None
        return aux        