

class TelaFornecedor:
    def tela_opcoes(self):
        print("-------- Fornecedor ----------")
        print("Escolha a opcao")
        print("1 - Incluir Fornecedor")
        print("2 - Alterar Fornecedor")
        print("3 - Listar Fornecedores")
        print("4 - Excluir Fornecedor")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def seleciona_fornecedor(self):
        cnpj = input("CNPJ do fornecedor que deseja selecionar: ")
        return cnpj

    def pega_dados_fornecedor(self):
        print("-------- DADOS FORNECEDOR ----------")
        nome = input("Nome ")
        telefone = input("Telefone: ")
        email = input("Email: ")
        cnpj = input("CNPJ: ")

        return {"nome": nome, "telefone": telefone, "email": email, "cnpj": cnpj}

    def mostra_fornecedor(self, dados_fornecedor):
        print("NOME DO FORNECEDOR: ", dados_fornecedor["nome"])
        print("CNPJ DO FORNECEDOR: ", dados_fornecedor["cnpj"])
        print("TELEFONE DO FORNECEDOR", dados_fornecedor["telefone"])
        print("EMAIL DO FORNECEDOR", dados_fornecedor["email"])
        print("\n")

    def mostra_mensagem(self, msg):
        print(msg)
