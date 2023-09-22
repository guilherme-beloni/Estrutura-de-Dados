from parada import Parada


class Voo:
    def __init__(self, codigo, origem, destino):
        self.codigo = codigo
        self.origem = origem
        self.destino = destino
        self.primeira_parada = None

    def __str__(self):
        pass 

    def adicionar_parada(self, cidade):
        nova_parada = Parada(cidade)
        if not self.primeira_parada:
            self.primeira_parada = nova_parada
        else:
            atual = self.primeira_parada
            while atual.proxima_parada:
                atual = atual.proxima_parada
            atual.proxima_parada = nova_parada

    def mostrar_info(self):
        print(f"\nCódigo do Voo: {self.codigo}")
        print(f"Origem: {self.origem}")
        print(f"Destino: {self.destino}")
        print("\nConexões:")
        parada_atual = self.primeira_parada
        while parada_atual:
            print(f"- Cidade: {parada_atual.cidade}")
            parada_atual = parada_atual.proxima_parada

# Lista para armazenar os voos
voos = []

while True:
    print("\n(1) Cadastrar um novo voo")
    print("(2) Informações de um voo")
    print("(3) Sair")
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        codigo_voo = input("Digite o código do voo: ")
        origem = input("Digite a origem: ")
        destino = input("Digite o destino: ")
        novo_voo = Voo(codigo_voo, origem, destino)

        while True:
            cidade = input("Digite o nome da cidade de conexão (ou deixe em branco para sair): ")
            if not cidade:
                break
            novo_voo.adicionar_parada(cidade)

        voos.append(novo_voo)
        print("Voo cadastrado com sucesso!")

    elif escolha == "2":
        codigo_voo = input("Digite o código do voo que deseja visualizar: ")
        encontrado = False
        for voo in voos:
            if voo.codigo == codigo_voo:
                voo.mostrar_info()
                encontrado = True
                break
        if not encontrado:
            print("Voo não encontrado!")

    elif escolha == "3":
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
