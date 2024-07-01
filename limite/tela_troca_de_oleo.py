

class TelaTrocaDeOleo:

    def tela_opcoes(self):
        print("-------- TROCA DE OLEO ----------")
        print("Escolha a opcao")
        print("1 - Cadastrar Troca")
        print("2 - Finalizar Troca")
        print("3 - Listar Trocas")
        print("4 - Listrar Trocas Efetuadas")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def mostra_troca(self, dados_troca):
        print("NOME DO CLIENTE: ", dados_troca["nome"])
        print("PLACA DA MOTO: ", dados_troca["placa"])
        print("MODELO DA MOTO: ", dados_troca["modelo"])
        print("DATA DE ENTRADA DO VEICULO: ", dados_troca["data_entrada"])
        print("ESPESSURA DO OLEO", dados_troca["espessura"])
        if dados_troca["oleo"] is not None:
            print("MODELO DO OLEO ESCOLHIDO: ", dados_troca["oleo"])
        if dados_troca["valor_final"] is not None:
            print("VALOR DA TROCA EFETUADA: R$", dados_troca["valor_final"])
        if dados_troca["data_saida"] is not None:
            print("DATA DE SAIDA DO VEICULO: ", dados_troca["data_saida"])
        print("CODIGO DA TROCA: ", dados_troca["codigo"])
        print("\n")


    def seleciona_troca(self):
        codigo = input("Codigo da troca que deseja selecionar: ")
        return codigo

    def pega_dados_saida_veiculo(self):
        data_saida = input("DATA DE SAIDA DO VEICULO: ")
        return data_saida

    def pega_dados_cliente(self):
        print("-------- DADOS CLIENTE ----------")
        placa_moto = input("Placa da moto: ")
        return placa_moto

    def pega_dados_cliente(self):
        print("-------- DADOS CLIENTE ----------")
        cpf_cliente = input("CPF do cliente: ")
        return cpf_cliente

    def pega_data_entrada(self):
        print("-------- DADOS TROCA ----------")
        data_entrada = input("Data de entrada: ")
        return data_entrada

    def mostra_cliente(self, dados_cliente):
        print("NOME DO CLIENTE: ", dados_cliente["nome"])
        print("CPF DO CLIENTE: ", dados_cliente["cpf"])
        print("TELEFONE DO CLIENTE", dados_cliente["telefone"])
        print("EMAIL DO CLIENTE", dados_cliente["email"])
        print("\n")

    def mostra_veiculo(self, dados_veiculo):
        print("MODELO DO VEICULO: ", dados_veiculo["modelo"])
        print("KILOMETRAGEM: ", dados_veiculo["kilometragem"])
        print("PLACA: ", dados_veiculo["placa"])
        print("\n")

    def seleciona_moto(self):
        placa_moto = input("Placa da moto que deseja selecionar: ")
        return placa_moto

    def mostra_mensagem(self, msg):
        print(msg)
