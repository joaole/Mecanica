from persistencia.dao import DAO
from entidade.troca_de_oleo import TrocaDeOleo

class TrocaDeOleoEntradaDAO(DAO):

    def __init__(self):
        super().__init__('trocas_entrada.pkl')
        TrocaDeOleo.carregar_proximo_codigo()

    def load(self):
        super().load()
        for troca_de_oleo in self.get_all():
            TrocaDeOleo.set_proximo_codigo(troca_de_oleo.codigo + 1)

    def add(self, troca_de_oleo: TrocaDeOleo):
        if isinstance(troca_de_oleo, TrocaDeOleo):
            super().add(troca_de_oleo.codigo, troca_de_oleo)
            TrocaDeOleo.salvar_proximo_codigo()

    def remove(self, troca_de_oleo: TrocaDeOleo):
        if isinstance(troca_de_oleo, TrocaDeOleo):
            super().remove(troca_de_oleo.codigo)
            TrocaDeOleo.salvar_proximo_codigo()
