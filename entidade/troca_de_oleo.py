from datetime import datetime
from entidade.veiculo import Veiculo
from entidade.cliente import Cliente
from entidade.oleo import Oleo


class TrocaDeOleo:
    __proximo_codigo = 0
    def __init__(self, veiculo, cliente, data_entrada):
        if isinstance(veiculo, Veiculo):
            self.__veiculo = veiculo
        if isinstance(cliente, Cliente):
            self.__cliente = cliente
        self.__oleo = None
        self.__valor_final = None
        self.__codigo = self.gerar_codigo()
        self.__data_entrada = data_entrada
        self.__data_saida = None

    @classmethod
    def set_proximo_codigo(cls, proximo_codigo):
        if proximo_codigo > TrocaDeOleo.__proximo_codigo:
            TrocaDeOleo.__proximo_codigo = proximo_codigo

    @classmethod
    def get_proximo_codigo(cls):
        return TrocaDeOleo.__proximo_codigo

    def gerar_codigo(self):
        TrocaDeOleo.__proximo_codigo += 1
        self.__codigo = TrocaDeOleo.__proximo_codigo

    @property
    def veiculo(self):
        return self.__veiculo

    @veiculo.setter
    def veiculo(self, veiculo):
        if isinstance(veiculo, Veiculo):
            self.__veiculo = veiculo

    @property
    def oleo(self):
        return self.__oleo

    @oleo.setter
    def oleo(self, oleo):
        if isinstance(oleo, Oleo):
            self.__oleo = oleo

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        if isinstance(cliente, Cliente):
            self.__cliente = cliente

    @property
    def valor_final(self):
        return self.__valor_final

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def data_entrada(self):
        return self.__data_entrada

    @data_entrada.setter
    def data_entrada(self, data_entrada):
        self.__data_entrada = data_entrada

    @valor_final.setter
    def valor_final(self, valor_final):
        self.__valor_final = valor_final

    def calcula_valor_final(self, veiculo, oleo):
        self.__valor_final = float(veiculo.modelo.quantidade_oleo) * float(oleo.valor)
        return self.__valor_final

    @property
    def data_saida(self):
        return self.__data_saida

    @data_saida.setter
    def data_saida(self, data_saida):
        self.__data_saida = data_saida
