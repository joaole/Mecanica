from entidade.oleo import Oleo
from limite.tela_oleo import TelaOleo
from persistencia.oleo_dao import OleoDAO


class ControladorOleo:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_oleo = TelaOleo()
        self.__oleo_dao = OleoDAO()

    def oleo_dao(self):
        return self.__oleo_dao.get_all()

    def gerar_codigo(self):
        codigo = str(self.__oleo_dao.get_size() + 1)
        return codigo

    def pega_oleo_por_codigo(self, codigo):
        for oleo in self.__oleo_dao.get_all():
            if oleo.codigo == codigo:
                return oleo
        else:
            return None

    def pega_oleo_por_expessura(self, expessura):
        for oleo in self.__oleo_dao.get_all():
            if oleo.expessura == expessura:
                self.__tela_oleo.mostrar_oleo(oleo)
        else:
            return None

    def inclui_oleo(self, codigo=None):
        cnpj = self.__controlador_sistema.controlador_fornecedor.listar_fornecedores()

        fornecedor = self.__controlador_sistema.controlador_fornecedor.pega_fornecedor_por_cnpj(cnpj)
        if fornecedor is not None:
            dados = self.__tela_oleo.pega_dados_oleo()

            for oleo in self.__oleo_dao.get_all():
                if oleo.marca == dados['marca'] and oleo.expessura == dados['expessura'] and int(oleo.valor) <= int(dados['valor']):
                    self.__tela_oleo.mostra_mensagem("ATENÇÃO: Óleo de mesmo valor ou mais caro já cadastrado para o mesma marca e espessura")
                    break
                elif oleo.marca == dados['marca'] and oleo.expessura == dados['expessura'] and int(oleo.valor) > int(
                        dados['valor']):
                    codigo = oleo.codigo
                    novo_oleo = Oleo(fornecedor, dados['marca'], dados['expessura'], dados['valor'], codigo)
                    self.__oleo_dao.add(novo_oleo)
                    self.__controlador_sistema.controlador_modelo.adicionar_oleo(novo_oleo)
                    self.__controlador_sistema.controlador_modelo.remover_oleo(oleo)
                    self.__tela_oleo.mostra_mensagem("Óleo cadastrado com sucesso")
                    break
            else:
                codigo = self.gerar_codigo()
                novo_oleo = Oleo(fornecedor, dados['marca'], dados['expessura'], dados['valor'], codigo)
                self.__oleo_dao.add(novo_oleo)
                self.__controlador_sistema.controlador_modelo.adicionar_oleo(novo_oleo)
                self.__tela_oleo.mostra_mensagem("Óleo cadastrado com sucesso")
        else:
            self.__tela_oleo.mostra_mensagem("ATENÇÃO: Fornecedor não cadastrado")

    def exclui_oleo(self, codigo=None):
        if codigo is None:
            codigo = self.__tela_oleo.seleciona_oleo()
        oleo = self.pega_oleo_por_codigo(codigo)
        if oleo is not None:
            self.__controlador_sistema.controlador_modelo.remover_oleo(oleo)
            self.__oleo_dao.remove(oleo)
            self.__tela_oleo.mostra_mensagem("Oleo removido com sucesso")
        else:
            self.__tela_oleo.mostra_mensagem("ATENCAO: Oleo nao encontrado")

    def altera_oleo(self, codigo=None):
        if codigo is None:
            self.lista_oleo()
            codigo = self.__tela_oleo.seleciona_oleo()
        oleo = self.pega_oleo_por_codigo(codigo)
        dados = self.__tela_oleo.pega_dados_oleo({'marca': oleo.marca, 'expessura': oleo.expessura, 'valor': oleo.valor })
        if oleo is not None:

            oleo.marca = dados["marca"]
            oleo.valor = dados["valor"]
            oleo.expessura = dados["expessura"]
            self.__tela_oleo.mostra_mensagem("Oleo alterado com sucesso")
        else:
            self.__tela_oleo.mostra_mensagem("ATENCAO: Oleo não encontrado")

    def lista_oleo(self):
        if self.__oleo_dao.get_size() == 0:
            self.__tela_oleo.mostra_mensagem("ATENCAO: Nenhum oleo cadastrado")
        for oleo in self.__oleo_dao.get_all():
            self.__tela_oleo.mostrar_oleo({"fornecedor": oleo.fornecedor.cnpj, "expessura": oleo.expessura, "marca": oleo.marca, "valor": oleo.valor, "codigo": oleo.codigo})

    def lista_oleo_por_expessura(self):
        self.lista_oleo()
        lista_oleos_expessura = []
        expessura = self.__tela_oleo.seleciona_expessura()
        for oleo in self.__oleo_dao.get_all():
            if oleo.expessura == expessura:
                lista_oleos_expessura.append(oleo)
                self.__tela_oleo.mostra_oleo({"fornecedor": oleo.fornecedor.cnpj, "expessura": oleo.expessura, "marca": oleo.marca, "valor": oleo.valor, "codigo": oleo.codigo})
        if len(lista_oleos_expessura) == 0:
            self.__tela_oleo.mostra_mensagem("ATENCAO: Nenhum oleo cadastrado com essa expessura")

    def abre_tela(self):
        lista_opcoes = {1: self.inclui_oleo, 2: self.altera_oleo, 3: self.lista_oleo_por_expessura,
                        4: self.exclui_oleo, 5: self.lista_oleo, 0: self.retornar}

        lista_oleo = []
        for oleo in self.__oleo_dao.get_all():
            lista_oleo.append([oleo.fornecedor.nome, oleo.marca, oleo.expessura, oleo.valor, oleo.codigo])
        dados_tela = self.__tela_oleo.tela_opcoes(lista_oleo)
        opcao = dados_tela['opcao']
        if opcao in lista_opcoes:
            if opcao == 0:
                lista_opcoes[opcao]()
            else:
                lista_opcoes[opcao](dados_tela.get('codigo'))
        else:
            self.__tela_oleo.mostra_mensagem('Opção Inválida')

    def retornar(self):
        self.__controlador_sistema.abre_tela()
