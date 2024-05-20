

class TelaOleo:
    def tela_opcoes(self):
        print("-------- OLEOS ----------")
        print("Escolha a opcao")
        print("1 - Incluir Oleo")
        print("2 - Alterar Oleo")
        print("3 - Listar Oleos de Uma Expessura")
        print("4 - Excluir Oleo")
        print("5 - Listar Oleos")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def seleciona_oleo(self):
        codigo = input("Codigo do oleo que deseja selecionar: ")
        return codigo

    def seleciona_expessura(self):
        expessura = input("Expessura do oleo que deseja selecionar: ")
        return expessura

    def pega_dados_oleo(self):
        print("-------- DADOS OLEO ----------")
        fornecedor = input("Fornecedor: ")
        marca = input("Marca: ")
        expessura = input("Expessura: ")
        valor = input("Valor: ")

        return {"fornecedor": fornecedor, "marca": marca, "expessura": expessura, "valor": valor}

    def mostra_oleo(self, dados_oleo):
        if isinstance(dados_oleo, dict):
            print("FORNECEDOR: ", dados_oleo["fornecedor"])
            print("MARCA DO OLEO: ", dados_oleo["marca"])
            print("EXPESSURA DO OLEO: ", dados_oleo["expessura"])
            print("VALOR DO OLEO: ", dados_oleo["valor"])
            print("CODIGO DO OLEO ", dados_oleo["codigo"])
            print("\n")
        else:
            print("Erro: dados_oleo não é um dicionario")
    def mostra_mensagem(self, msg):
        print(msg)
