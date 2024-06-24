from persistencia.dao import DAO
from entidade.troca_de_oleo import TrocaDeOleo


class TrocaDeOleoEntradaDAO(DAO):

    def __init__(self):
        super().__init__('trocas_entrada.pkl')

    def load(self):
        super().load()
        if self.get_all():
            print(self.get_all()[0].get_proximo_codigo())
            TrocaDeOleo.set_proximo_codigo(self.get_all()[0].get_proximo_codigo())

    def add(self, troca_de_oleo: TrocaDeOleo):
        if isinstance(troca_de_oleo, TrocaDeOleo):
            super().add(troca_de_oleo.codigo, troca_de_oleo)

    def remove(self, troca_de_oleo: TrocaDeOleo):
        if isinstance(troca_de_oleo, TrocaDeOleo):
            super().remove(troca_de_oleo.codigo)
