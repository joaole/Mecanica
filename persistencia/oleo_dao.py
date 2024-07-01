import pickle
from persistencia.dao import DAO
from entidade.oleo import Oleo


class OleoDAO(DAO):

    def __init__(self):
        super().__init__('oleos.pkl')

    def add(self, oleo: Oleo):
        if isinstance(oleo, Oleo):
            super().add(oleo.codigo, oleo)

    def remove(self, oleo: Oleo):
        if isinstance(oleo, Oleo):
            super().remove(oleo.codigo)

    def atualiza(self):
        super().atualiza()
