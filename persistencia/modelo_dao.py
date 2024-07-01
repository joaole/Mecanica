from persistencia.dao import DAO
from entidade.modelo import Modelo


class ModeloDAO(DAO):

    def __init__(self):
        super().__init__('modelos.pkl')

    def add(self, modelo: Modelo):
        if isinstance(modelo, Modelo):
            super().add(modelo.codigo, modelo)

    def remove(self, modelo: Modelo):
        if isinstance(modelo, Modelo):
            super().remove(modelo.codigo)

    def atualiza(self):
        super().atualiza()
        
