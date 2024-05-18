from entidade.fornecedor import Fornecedor


class ControladorFornecedor:
    def __init__(self):
        self.__fonecedores = []

    @property
    def fornecedores(self):
        return self.__fonecedores

    def inclui_fornecedor(self, nome, telefone, email, cnpj):
        novo_fornecedor = Fornecedor(nome, telefone, email, cnpj)
        for fornecedor in self.__fonecedores:
            if fornecedor.cnpj == novo_fornecedor.cnpj:
                return None
        else:
            self.__fonecedores.append(novo_fornecedor)

