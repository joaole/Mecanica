from entidade.fornecedor import Fornecedor


class Oleo:
    def __init__(self, fornecedor, marca, expessura, valor, codigo):
        if isinstance(fornecedor, Fornecedor):
            self.__fornecedor = fornecedor
        self.__marca = marca
        self.__expessura = expessura
        self.__valor = valor
        self.__codigo = codigo

    @property
    def fornecedor(self):
        return self.__fornecedor

    @fornecedor.setter
    def fornecedor(self, fornecedor):
        self.__fornecedor = fornecedor

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    @property
    def expessura(self):
        return self.__expessura

    @expessura.setter
    def expessura(self, expessura):
        self.__expessura = expessura

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        self.__valor = valor

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo
