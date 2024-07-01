from persistencia.dao import DAO
from entidade.cliente import Cliente


class CLienteDAO(DAO):

    def __init__(self):
        super().__init__('clientes.pkl')

    def add(self, cliente: Cliente):
        if isinstance(cliente, Cliente):
            super().add(cliente.cpf, cliente)

    def remove(self, cliente: Cliente):
        if isinstance(cliente, Cliente):
            super().remove(cliente.cpf)

    def atualizar_veiculos(self):
        super().atualiza()
        
