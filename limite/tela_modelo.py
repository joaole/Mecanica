

class TelaModelo:
  def tela_opcoes(self):
    print("-------- Modelos ----------")
    print("Escolha a opcao")
    print("1 - Incluir Modelo")
    print("2 - Alterar Modelo")
    print("3 - Listar Modelos")
    print("4 - Excluir Modelos")
    print("0 - Retornar")

    opcao = int(input("Escolha a opcao: "))
    return opcao

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def pega_dados_modelo(self):
    print("-------- DADOS MODELO ----------")
    nome = input("Nome: ")
    quantidade_oleo = input("Quantidade de Oleo: ")
    codigo = input("Codigo: ")

    return {"nome": nome, "Quantidade de oleo": quantidade_oleo, "Codigo": codigo}

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def mostra_modelo(self, dados_modelo):
    print("NOME DO MODELO: ", dados_modelo["nome"])
    print("QUANTIDADE DE OLEO: ", dados_modelo["quantidade_oleo"])
    print("CODIGO DO MODELO: ", dados_modelo["codigo"])
    print("\n")

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def seleciona_modelo(self):
    codigo = input("CODIGO do modelo que deseja selecionar: ")
    return codigo

  def mostra_mensagem(self, msg):
    print(msg)
