from persistencia.dao import DAO
from entidade.troca_de_oleo import TrocaDeOleo


class TrocaDeOleoEntradaDAO(DAO):

    def __init__(self):
        super().__init__('trocas_entrada.pkl')

    def add(self, troca_de_oleo: TrocaDeOleo):
        if isinstance(troca_de_oleo, TrocaDeOleo):
            super().add(troca_de_oleo.codigo, troca_de_oleo)

    def remove(self, troca_de_oleo: TrocaDeOleo):
        if isinstance(troca_de_oleo, TrocaDeOleo):
            super().remove(troca_de_oleo.codigo)
