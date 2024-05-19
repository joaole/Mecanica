from entidade.troca_de_oleo import TrocaDeOleo
from entidade.veiculo import Veiculo
from entidade.cliente import Cliente
from entidade.oleo import Oleo
from limite.tela_troca_de_oleo import TelaTrocaDeOleo

class ControladorTrocaDeOleo:
    def __init__(self):
        self.__trocas = []
        self.__quantidade_de_oleo_total = 0
        self.__tela_troca_de_oleo = TelaTrocaDeOleo

    def pega_dados_troca(self, codigo):
        for troca in self.__trocas:
            if troca.codigo == codigo:
                return troca
        return None

    def fazer_troca_de_oleo(self, veiculo: Veiculo, cliente: Cliente, oleo: Oleo, data_entrada: str, data_saida: str, quantidade_oleo: float):
        codigo = len(self.__trocas) + 1
        nova_troca = TrocaDeOleo(veiculo, cliente, oleo, data_saida, data_entrada, codigo)
        nova_troca.quantidade_oleo = quantidade_oleo
        self.calcular_valor_final(nova_troca)
        self.__trocas.append(nova_troca)
        self.__quantidade_de_oleo_total += quantidade_oleo
        print('Troca Realizada!')

    def incluir_troca(self, troca: TrocaDeOleo):
        self.__trocas.append(troca)
        self.__quantidade_de_oleo_total += troca.quantidade_oleo

    def cancelar_troca(self, codigo):
        troca_para_cancelar = self.pega_dados_troca(codigo)
        if troca_para_cancelar:
            self.__trocas.remove(troca_para_cancelar)
            self.__quantidade_de_oleo_total -= troca_para_cancelar.quantidade_oleo

    def ver_detalhes_troca(self):
        print("\nDetalhes da troca de óleo")
        codigo = int(input("Código da troca: "))
        troca = self.pega_dados_troca(codigo)
        if troca:
            print(f"Código: {troca.codigo}")
            print(f"Veículo: {troca.veiculo.placa_moto}")
            print(f"Cliente: {troca.cliente.nome}")
            print(f"Óleo: {troca.oleo.marca} - {troca.oleo.expessura}")
            print(f"Data de entrada: {troca.data_entrada}")
            print(f"Data de saída: {troca.data_saida}")
            print(f"Quantidade de óleo: {troca.quantidade_oleo} litros")
            print(f"Valor final: R$ {troca.valor_final}")
            print(f"Tempo na oficina: {self.calcular_tempo_na_oficina(codigo)} dias")
        else:
            print("Troca de óleo não encontrada!")

    def ver_quantidade_total_oleo(self):
        quantidade_total = self.calcular_quantidade_total_de_oleo()
        print(f"\nQuantidade total de óleo utilizado: {quantidade_total} litros")

    def calcular_valor_final(self, troca: TrocaDeOleo):
        troca.valor_final = troca.oleo.valor * troca.quantidade_oleo

    def calcular_quantidade_total_de_oleo(self):
        return self.__quantidade_de_oleo_total

    def calcular_tempo_na_oficina(self, codigo):
        troca = self.pega_dados_troca(codigo)
        if troca:
            data_entrada = troca.data_entrada
            data_saida = troca.data_saida
            return (data_saida - data_entrada)
        return None

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



    def abre_tela(self):
        lista_opcoes = {1: self.fazer_troca_de_oleo, 2: self.cancelar_troca, 3: self.ver_detalhes_troca,
                        4: self.ver_quantidade_total_oleo}

        continua = True
        while continua:
            lista_opcoes[self.__tela_troca_de_oleo.tela_opcoes(self)]()
