from persistencia.dao import DAO
from entidade.fornecedor import Fornecedor


class FornecedorDAO(DAO):

    def __init__(self):
        super().__init__('fornecedores.pkl')

    def add(self, fornecedor: Fornecedor):
        if isinstance(fornecedor, Fornecedor):
            super().add(fornecedor.cnpj, fornecedor)

    def remove(self, fornecedor: Fornecedor):
        if isinstance(fornecedor, Fornecedor):
            super().remove(fornecedor.cnpj)
        
