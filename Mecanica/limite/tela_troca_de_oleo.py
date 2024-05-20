

class TelaTrocaDeOleo:

    def tela_opcoes(self):
        print("-------- TROCA DE OLEO ----------")
        print("Escolha a opcao")
        print("1 - Realizar Troca")
        print("2 - Alterar Troca")
        print("3 - Listar Cliente")
        print("4 - Cancelar Troca")
        print("5 - Finalizar Troca")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def seleciona_cliente(self):
        cpf = input("CPF do cliente que deseja selecionar: ")
        return cpf

    def pega_codigo_modelo(self):
        codigo_modelo = input("CODIGO DE MODELO DO VEICULO: ")
        return codigo_modelo

    def pega_dados_troca(self):
        print("-------- DADOS TROCA DE OLEO ----------")
        cpf_cliente = input("CPF do Cliente ")
        placa_moto = input("Placa do veículo: ")

        return {"cpf_cliente": cpf_cliente, "placa": placa_moto}

    def pega_dados_cliente(self):
        print("-------- DADOS CLIENTE ----------")
        nome_cliente = input("Nome: ")
        telefone_cliente = input("Telefone: ")
        email_cliente = input("Email: ")
        cpf_cliente = input("CPF: ")
        return {"nome": nome_cliente, "telefone": telefone_cliente, "email": email_cliente, "cpf": cpf_cliente}
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
