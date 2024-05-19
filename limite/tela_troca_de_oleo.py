from entidade.veiculo import Veiculo
from entidade.cliente import Cliente
from entidade.oleo import Oleo
from controle.controlador_troca_de_oleo import ControladorTrocaDeOleo


class TelaTrocaDeOleo:
    def __init__(self, controlador: ControladorTrocaDeOleo):
        self.__controlador = controlador

    def mostrar_menu(self):
        while True:
            print("\n Troca de Óleo")
            print("1. Fazer troca de óleo")
            print("2. Cancelar troca de óleo")
            print("3. Ver detalhes de uma troca de óleo")
            print("4. Ver quantidade total de óleo utilizado")
            print("0. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.fazer_troca_de_oleo()
            elif opcao == "2":
                self.cancelar_troca_de_oleo()
            elif opcao == "3":
                self.ver_detalhes_troca()
            elif opcao == "4":
                self.ver_quantidade_total_oleo()
            elif opcao == "0":
                break
            else:
                print("Opção inválida, tente novamente.")

    def fazer_troca_de_oleo(self):
      self.__controlador.fazer_troca_de_oleo()
      self.__controlador.incluir_troca()


    def cancelar_troca_de_oleo(self):
        print("\nCancelando troca de óleo")
        self.__controlador.cancelar_troca()

    def ver_detalhes_troca(self):
        print("\nDetalhes da troca de óleo")
        codigo = int(input("Código da troca: "))
        troca = self.__controlador.pega_dados_troca(codigo)
        if troca:
            print(f"Código: {troca.codigo}")
            print(f"Veículo: {troca.veiculo.placa_moto}")
            print(f"Cliente: {troca.cliente.nome}")
            print(f"Óleo: {troca.oleo.marca} - {troca.oleo.expessura}")
            print(f"Data de entrada: {troca.data_entrada}")
            print(f"Data de saída: {troca.data_saida}")
            print(f"Quantidade de óleo: {troca.quantidade_oleo} litros")
            print(f"Valor final: R$ {troca.valor_final}")
            print(f"Tempo na oficina: {self.__controlador.calcular_tempo_na_oficina(codigo)} dias")
        else:
            print("Troca de óleo não encontrada!")

    def ver_quantidade_total_oleo(self):
        quantidade_total = self.__controlador.calcular_quantidade_total_de_oleo()
        print(f"\nQuantidade total de óleo utilizado: {quantidade_total} litros")

    def obter_veiculo(self):
        placa_moto = input("Placa do veículo: ")
        km_moto = float(input("Quilometragem do veículo: "))
        modelo = input("Modelo do veículo: ")  # Aqui deve ser um objeto Modelo, simplificando para string
        return Veiculo(placa_moto, km_moto, modelo)

    def obter_cliente(self):
        nome = input("Nome do cliente: ")
        telefone = input("Telefone do cliente: ")
        email = input("Email do cliente: ")
        cpf = int(input("CPF do cliente: "))
        return Cliente(nome, telefone, email, cpf)

    def obter_oleo(self):
        marca = input("Marca do óleo: ")
        expessura = input("Expessura do óleo: ")
        valor = float(input("Valor do óleo por litro: "))
        codigo = int(input("Código do óleo: "))
        fornecedor = input("Fornecedor do óleo: ")  # Aqui deve ser um objeto Fornecedor, simplificando para string
        return Oleo(fornecedor, marca, expessura, valor, codigo)
