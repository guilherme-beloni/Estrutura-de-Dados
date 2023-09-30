from voo import Voo

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
        novo_voo = Voo(codigo_voo, origem, destino)  #passando os inputs para o OBJ Voo

        while True:
            cidade = input("Digite o nome da cidade de conexão (ou digite 0 para sair): ")
            if cidade == '':  #se não for dada a entrada de dados das paradas, para o laço
                break
            novo_voo.adicionar_parada(cidade) # se não adiciona a cidade atraves do metodo adicionar_parada

        voos.append(novo_voo)
        print("Voo cadastrado com sucesso!") #adicionando o voo cadastrado na lista voos


    elif escolha == "2":
        codigo_voo = input("Digite o código do voo que deseja visualizar: ")
        encontrado = False
        for voo in voos:
            if voo.codigo == codigo_voo:
                voo.exibe_voo()
                encontrado = True
                break
        if not encontrado:
            print("Voo não encontrado!")    

    elif escolha == "3":
        print('Até logo!')
        break
        

    else:        
        print("Por favor, escolha uma opção válida.")