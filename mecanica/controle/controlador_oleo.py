from entidade.oleo import Oleo
from entidade.fornecedor import Fornecedor


class ControladorOleo:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__oleos = []

    def inclui_oleo(self, fornecedor: Fornecedor, marca: str, expessura: int, valor: str, codigo: int):
        novo_oleo = Oleo(fornecedor, marca, expessura, valor, codigo)
        for oleo in self.__oleos:
            '''se o codigo for igual, nem adiciona'''
            if oleo.codigo == novo_oleo.codigo:
                return None
            elif oleo.marca == novo_oleo.marca and oleo.expessura == expessura and oleo.valor > novo_oleo.valor:
                self.__oleos.append(novo_oleo)
                self.__oleos.remove(oleo)
                return novo_oleo
        else:
            self.__oleos.append(novo_oleo)
            return novo_oleo

    def exclui_oleo(self, codigo):
        for oleo in self.__oleos:
            if oleo.codigo == codigo:
                self.__oleos.remove(oleo)
        else:
            return None

    def altera_valor_oleo(self, codigo, valor):
        for oleo in self.__oleos:
            if oleo.codigo == codigo:
                oleo.valor = valor
        else:
            return None

    def procura_oleo_expessura(self, expessura):
        oleos_da_expessura = []
        for oleo in self.__oleos:
            if oleo.expessura == expessura:
                oleos_da_expessura.append(oleo)
        return oleos_da_expessura

    def listar_oleo_fornecedor(self, fornecedor):
        oleos_do_fornecedor = []
        for oleo in self.__oleos:
            if oleo.fornecedor == fornecedor:
                oleos_do_fornecedor.append(oleo)
        return oleos_do_fornecedor
    def retornar(self):
        self.__controlador_sistema.abre_tela()
