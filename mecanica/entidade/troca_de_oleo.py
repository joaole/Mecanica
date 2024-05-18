from entidade.veiculo import Veiculo
from entidade.cliente import Cliente
from entidade.oleo import Oleo

class TrocaDeOleo:
    def __init__(self, Veiculo, cliente, data_saida, data_entrada, codigo):
        self.__veiculo = Veiculo
        self.__cliente = cliente
        self.__data_saida = data_saida
        self.__valor_final = None
        self.__codigo = codigo
        self.__data_entrada = data_entrada

    @property
    def veiculo(self):
        return self.__veiculo

    @veiculo.setter
    def veiculo(self, veiculo):
        if isinstance(veiculo, Veiculo):
            self.__veiculo = veiculo

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        if isinstance(cliente, Cliente):
            self.__cliente = cliente

    @property
    def data_saida(self):
        return self.__data_saida

    @data_saida.setter
    def data_saida(self, data_saida):
        self.__data_saida = data_saida

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

    @data_saida.setter
    def dara_entrada(self, data_entrada):
        self.__data_entrada = data_entrada

    def valor_final(self):
        self.__valor_final = Veiculo.modelo.quantidade_oleo() * Oleo.valor
