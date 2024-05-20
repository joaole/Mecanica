from entidade.oleo import Oleo
from entidade.fornecedor import Fornecedor
from limite.tela_oleo import TelaOleo


class ControladorOleo:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_oleo = TelaOleo()
        self.__oleos = []

    def gerar_codigo(self):
        codigo = str(len(self.__oleos) + 1)
        return codigo

    def pega_oleo_por_codigo(self, codigo):
        for oleo in self.__oleos:
            if oleo.codigo == codigo:
                return oleo
        else:
            return None

    def pega_oleo_por_expessura(self, expessura):
        for oleo in self.__oleos:
            if oleo.expessura == expessura:
                return Oleo
        else:
            return None

    def inclui_oleo(self):
        dados = self.__tela_oleo.pega_dados_oleo()
        for oleo in self.__oleos:
            if oleo.marca == dados["marca"] and oleo.expessura == dados["expessura"] and int(oleo.valor) < int(dados["valor"]):
                self.__tela_oleo.mostra_mensagem("ATENÇÃO: Oleo mais caro que um já cadastrado do mesmo modelo e expessura")
                break
            elif oleo.marca == dados["marca"] and oleo.expessura == dados["expessura"] and int(oleo.valor) > int(dados["valor"]):
                codigo = oleo.codigo
                novo_oleo = Oleo(dados["fornecedor"], dados["marca"], dados["expessura"], dados["valor"], codigo)
                self.__oleos.append(novo_oleo)
                self.__oleos.remove(oleo)
                self.__tela_oleo.mostra_mensagem("Oleo cadastrado com sucesso")
                break
        else:
            codigo = self.gerar_codigo()
            novo_oleo = Oleo(dados["fornecedor"], dados["marca"], dados["expessura"], dados["valor"], codigo)
            self.__oleos.append(novo_oleo)
            self.__tela_oleo.mostra_mensagem("Oleo cadastrado com sucesso")

    def exclui_oleo(self):
        codigo = self.__tela_oleo.seleciona_oleo()
        oleo = self.pega_oleo_por_codigo(codigo)
        if oleo is not None:
            self.__oleos.remove(oleo)
            self.__tela_oleo.mostra_mensagem("Oleo removido com sucesso")
        else:
            self.__tela_oleo.mostra_mensagem("ATENCAO: Oleo nao encontrado")

    def altera_oleo(self):
        self.lista_oleo()
        codigo = self.__tela_oleo.seleciona_oleo()
        oleo = self.pega_oleo_por_codigo(codigo)
        dados = self.__tela_oleo.pega_dados_oleo()
        if oleo is not None:
            oleo.fornecedor = dados["fornecedor"]
            oleo.marca = dados["marca"]
            oleo.valor = dados["valor"]
            oleo.expessura = dados["expessura"]
            self.__tela_oleo.mostra_mensagem("Oleo alterado com sucesso")
        else:
            self.__tela_oleo.mostra_mensagem("ATENCAO: Oleo não encontrado")

    def lista_oleo(self):
        for oleo in self.__oleos:
            self.__tela_oleo.mostra_oleo({"fornecedor": oleo.fornecedor, "expessura": oleo.expessura, "marca": oleo.marca, "valor": oleo.valor, "codigo": oleo.codigo})

    def lista_oleo_expessura(self):
        lista_oleos_expessura = []
        expessura = self.__tela_oleo.seleciona_expessura()
        for oleo in self.__oleos:
            if oleo.expessura == expessura:
                lista_oleos_expessura.append(oleo)
                self.__tela_oleo.mostra_oleo({"fornecedor": oleo.fornecedor, "expessura": oleo.expessura, "marca": oleo.marca, "valor": oleo.valor, "codigo": oleo.codigo})
        if len(lista_oleos_expessura) == 0:
            self.__tela_oleo.mostra_mensagem("ATENCAO: Nenhum oleo cadastrado com essa expessura")

    def abre_tela(self):
        lista_opcoes = {1: self.inclui_oleo, 2: self.altera_oleo, 3: self.lista_oleo_expessura,
                        4: self.exclui_oleo, 5: self.lista_oleo, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_oleo.tela_opcoes()]()

    def retornar(self):
        self.__controlador_sistema.abre_tela()
