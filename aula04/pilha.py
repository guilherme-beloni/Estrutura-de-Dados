from aula03.no import No

class Pilha:
    def __init__(self):
        self.topo = None
        self._tamanho = 0


    def __len__(self):
        return self._tamanho



    def __repr__(self):
        pass    


    def __str__(self):
        return self.__repr__()
    

    def push(self, info):
        no = No(info)
        no.proximo = self.topo
        self.topo = no
        self._tamanho += 1


    def pop(self):
        if self._tamanho > 0:
            no = self.topo

    def pick(self):
        pass
