class TelaCliente:

    def tela_opcoes(self):
        print("-------- CLIENTE ----------")
        print("Escolha a opcao")
        print("1 - Incluir Cliente")
        print("2 - Alterar Cliente")
        print("3 - Listar Cliente")
        print("4 - Excluir Cliente")
        print("5 - Incluir Veiculo")
        print("6 - Alterar Veículo")
        print("7 - Excluir Veiculo")
        print("8 - Listar Veículos")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def seleciona_cliente(self):
        cpf = input("CPF do cliente que deseja selecionar: ")
        return cpf

    def pega_dados_moto(self):
        print("-------- DADOS CLIENTE ----------")
        modelo_moto = input("Modelo ")
        placa_moto = input("Placa: ")
        km_moto = input("Kilometragem: ")

        return {"modelo": modelo_moto, "placa": placa_moto, "kilometragem": km_moto}

    def pega_dados_cliente(self):
        print("-------- DADOS CLIENTE ----------")
        nome_cliente = input("Nome: ")
        cpf_cliente = input("CPF: ")
        telefone_cliente = input("Telefone: ")
        email_cliente = input("Email: ")
        return {"nome": nome_cliente, "cpf": cpf_cliente, "telefone": telefone_cliente, "email": email_cliente}
    def mostra_cliente(self, dados_cliente):
        print("NOME DO CLIENTE: ", dados_cliente["nome"])
        print("CPF DO CLIENTE: ", dados_cliente["cpf"])
        print("TELEFONE DO CLIENTE", dados_cliente["telefone"])
        print("EMAIL DO CLIENTE", dados_cliente["email"])
        print("\n")

    def seleciona_cliente(self):
        cpf = input("Cpf do cliente que deseja selecionar: ")
        return cpf

    def seleciona_moto(self):
        placa_moto = input("Placa da moto que deseja selecionar: ")
        return placa_moto

    def mostra_mensagem(self, msg):
        print(msg)
