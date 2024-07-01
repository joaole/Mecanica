from datetime import datetime, date
from entidade.veiculo import Veiculo
from entidade.cliente import Cliente
from entidade.oleo import Oleo
import pickle

class TrocaDeOleo:

    __proximo_codigo = 0
    __codigo_filename = 'proximo_codigo.pkl'  # Nome do arquivo pickle para o próximo código

    def __init__(self, veiculo, cliente, data_entrada):
        if isinstance(veiculo, Veiculo):
            self.__veiculo = veiculo
        if isinstance(cliente, Cliente):
            self.__cliente = cliente
        self.__oleo = None
        self.__valor_final = None
        self.__codigo = TrocaDeOleo.gerar_codigo()  # Chamando o método de classe para gerar código
        self.__data_entrada = data_entrada
        self.__data_saida = None

    @classmethod
    def gerar_codigo(cls):
        cls.__proximo_codigo += 1
        return cls.__proximo_codigo

    @classmethod
    def set_proximo_codigo(cls, proximo_codigo):
        cls.__proximo_codigo = proximo_codigo

    def __converter_para_date(self, data):
        if isinstance(data, date):
            return data
        elif isinstance(data, datetime):
            return data.date()
        else:
            raise ValueError("A data fornecida não é do tipo date ou datetime.")

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
        self.__data_entrada = self.__converter_para_date(data_entrada)

    @property
    def data_saida(self):
        return self.__data_saida

    @data_saida.setter
    def data_saida(self, data_saida):
        self.__data_saida = self.__converter_para_date(data_saida)

    def calcula_valor_final(self, veiculo, oleo):
        self.__valor_final = float(veiculo.modelo.quantidade_oleo) * float(oleo.valor)
        return self.__valor_final

    @classmethod
    def salvar_proximo_codigo(cls):
        with open(cls.__codigo_filename, 'wb') as f:
            pickle.dump(cls.__proximo_codigo, f)

    @classmethod
    def carregar_proximo_codigo(cls):
        try:
            with open(cls.__codigo_filename, 'rb') as f:
                cls.__proximo_codigo = pickle.load(f)
        except FileNotFoundError:
            cls.__proximo_codigo = 0
