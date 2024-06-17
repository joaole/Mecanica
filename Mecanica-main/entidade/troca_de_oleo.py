from entidade.modelo import Modelo
from entidade.veiculo import Veiculo
from entidade.cliente import Cliente
from entidade.oleo import Oleo


class TrocaDeOleo:
    def __init__(self, veiculo, cliente, data_entrada, codigo):
        if isinstance(veiculo, Veiculo):
            self.__veiculo = veiculo
        if isinstance(cliente, Cliente):
            self.__cliente = cliente
        self.__oleo = None
        self.__valor_final = None
        self.__codigo = codigo
        self.__data_entrada = data_entrada
        self.__data_saida = None

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
