from entidade.troca_de_oleo import TrocaDeOleo
from entidade.veiculo import Veiculo
from entidade.cliente import Cliente
from entidade.oleo import Oleo

class ControladorTrocaDeOleo:
    def __init__(self):
        self.__trocas = []
        self.__quantidade_de_oleo_total = 0

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

    def incluir_troca(self, troca: TrocaDeOleo):
        self.__trocas.append(troca)
        self.__quantidade_de_oleo_total += troca.quantidade_oleo

    def cancelar_troca(self, codigo):
        troca_para_cancelar = self.pega_dados_troca(codigo)
        if troca_para_cancelar:
            self.__trocas.remove(troca_para_cancelar)
            self.__quantidade_de_oleo_total -= troca_para_cancelar.quantidade_oleo

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
