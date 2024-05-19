from abc import ABC, abstractmethod


class Pessoa(ABC):
    def __init__(self, nome, telefone, email):
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(telefone, str):
            self.__telefone = telefone
        if isinstance(email, str):
            self.__email = email

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def telefone(self):
        return self.__nome

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email
