from entidade.pessoa import Pessoa


class Fornecedor(Pessoa):
    def __init__(self, nome, telefone, email, cnpj):
        super().__init__(nome, telefone, email)
        self.__cnpj = cnpj

    @property
    def cnpj(self):
        return self.__cnpj

    @cnpj.setter
    def cnpj(self, cnpj):
        self.__cnpj = cnpj
fornecedor = Fornecedor('Cleverson', '5555', 'uhuhuh', 556)
print(fornecedor.nome)
