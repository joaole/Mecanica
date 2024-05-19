

class Modelo:
    def __init__(self, nome, quantidade_oleo, codigo):
        self.__nome = nome
        self.__quantidade_oleo = quantidade_oleo
        self.__oleos = []
        self.__codigo = codigo

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def quantidade_oleo(self):
        return self.__quantidade_oleo

    @quantidade_oleo.setter
    def quantidade_oleo(self, quantidade_oleo):
        self.__quantidade_oleo = quantidade_oleo

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def oleos(self):
        return self.__oleos
