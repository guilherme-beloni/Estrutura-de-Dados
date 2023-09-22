# semelhante ao arquivo listaencadeada.py das aulas do professor
# aqui faremos as atribuiçõees dos voos em sí  

from parada import Parada


class Voo:
    def __init__(self, codigo, origem, destino):   #construtor voo
        self.codigo = codigo
        self.origem = origem
        self.destino = destino
        self.primeira_parada = None

   
        

    def adicionar_parada(self, cidade):   #função que adiciona uma parada (um nó)
        nova_parada = Parada(cidade) # Criando o Obj Parada
        if self.primeira_parada:                                                           # se parada não existir, sera definido a nova_parada como a primeira parada
            parada_atual = self.primeira_parada                                            # se tiver uma parada, a funcao percorre as paradas    
            while parada_atual.proxima_parada:    
                parada_atual += parada_atual.proxima_parada                               
            parada_atual.proxima_parada = nova_parada                                      # define a nova_parada como a próxima parada dessa última parada
        else:
            self.primeira_parada = nova_parada        

    def exibe_voo(self):
        print(f'\nCódigo do Voo: {self.codigo}')
        print(f"Origem: {self.origem}")
        print(f"Destino: {self.destino}")
        print("\nConexões:")
        parada_atual = self.primeira_parada
        while parada_atual:
            print(f"- Cidade: {parada_atual.cidade}")
            parada_atual = parada_atual.proxima_parada # Apontando para a Prox parada


    