from entidade.pessoa import Pessoa
from entidade.veiculo import Veiculo


class Cliente(Pessoa):
    def __init__(self, nome, telefone, email, cpf):
        super().__init__(nome, telefone, email)
        self.__cpf = cpf
        self.__veiculos = []

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def veiculos(self):
        return self.__veiculos

    def inclui_veiculo(self, veiculo: Veiculo):
        self.__veiculos.append(veiculo)

    def exclui_veiculo(self, veiculo: Veiculo):
        self.__veiculos.remove(veiculo)

    def pega_veiculo(self, placa_moto):
        for veiculo in self.__veiculos:
            if veiculo.placa_moto == placa_moto:
                return veiculo
