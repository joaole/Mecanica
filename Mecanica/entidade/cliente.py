from entidade.pessoa import Pessoa
from entidade.veiculo import Veiculo


class Cliente(Pessoa):
    def __init__(self,nome, telefone, email, cpf):
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

    def validar_cpf(self, cpf: str) -> bool:
        cpf = ''.join(filter(str.isdigit, cpf))

        if len(cpf) != 11 or cpf == cpf[0] * 11:
            return False

        for i in range(9, 11):
            soma = sum(int(cpf[j]) * (i + 1 - j) for j in range(i))
            digito = (soma * 10) % 11
            if digito == 10:
                digito = 0
            if cpf[i] != str(digito):
                return False
        return True
