

class TelaModelo:
    def tela_opcoes(self):
        print("-------- Modelos ----------")
        print("Escolha a opcao")
        print("1 - Incluir Modelo")
        print("2 - Alterar Modelo")
        print("3 - Listar Modelos")
        print("4 - Excluir Modelos")
        print("5 - Listar Oleos do Modelo")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def pega_dados_modelo(self):
        print("-------- DADOS MODELO ----------")
        nome = input("Nome: ")
        quantidade_oleo = input("Quantidade de Oleo: ")
        expessura = input("Expessura de oleo: ")

        return {"nome": nome, "Quantidade de oleo": quantidade_oleo, "expessura": expessura}

    def mostra_modelo(self, dados_modelo):
        print("NOME DO MODELO: ", dados_modelo["nome"])
        print("QUANTIDADE DE OLEO: ", dados_modelo["quantidade_oleo"])
        print("EXPESSURA DE OLEO DO MODELO: ", dados_modelo["expessura"])
        print("CODIGO DO MODELO: ", dados_modelo["codigo"])
        print("\n")

    def mostra_oleo_modelo(self, dados_oleo):
        print("CNPJ DO FORNECEDOR: ", dados_oleo["fornecedor"])
        print("MARCA OLEO: ", dados_oleo["marca"])
        print("CODIGO DO OLEO: ", dados_oleo["codigo"])
        print("VALOR DO OLEO: ", dados_oleo["valor"])
        print("\n")

    def seleciona_modelo(self):
        codigo = input("CODIGO do modelo que deseja selecionar: ")
        return codigo

    def mostra_mensagem(self, msg):
        print(msg)
