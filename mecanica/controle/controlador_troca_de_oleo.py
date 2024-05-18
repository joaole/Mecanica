from entidade.troca_de_oleo import TrocaDeOleo
from entidade.veiculo import Veiculo
from entidade.cliente import Cliente
from entidade.modelo import Modelo

class ControladorTrocaDeOleo:
    def __init__(self, modelo=None):
        self.__trocas = []
        self.__modelo = modelo

    def efetuar_troca(self, veiculo, cliente, data_saida, data_entrada, codigo):
        if isinstance(veiculo, Veiculo) and isinstance(cliente, Cliente):
            troca_de_oleo = TrocaDeOleo(veiculo, cliente, data_saida, data_entrada, codigo)
            self.__trocas.append(troca_de_oleo)

    def cancelar_troca(self, codigo):
        for troca in self.__trocas:
            if troca.codigo == codigo:
                self.__trocas.remove(troca)

    def calcular_quantidade_oleo(self):
        if self.__modelo:
            self.__quantidade_de_oleo += self.__modelo.quantidade_oleo

        else:
            return 0
