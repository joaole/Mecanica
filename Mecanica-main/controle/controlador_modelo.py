from limite.tela_modelo import TelaModelo
from entidade.modelo import Modelo
from persistencia.modelo_dao import ModeloDAO

class ControladorModelo:
    def __init__(self, controlador_sistema):
        self.__modelo_dao = ModeloDAO()
        self.__tela_modelo = TelaModelo()
        self.__controlador_sistema = controlador_sistema

    def gerar_codigo(self):
        codigo = str(self.__modelo_dao.get_size() + 1)
        return codigo

    def pega_modelo_por_codigo(self, codigo: int):
        for modelo in self.__modelo_dao.get_all():
            if modelo.codigo == codigo:
                return modelo
        return None

    def incluir_modelo(self):
        dados_modelo = self.__tela_modelo.pega_dados_modelo()

        for m in self.__modelo_dao.get_all():
            if m.nome == dados_modelo["nome"] and m.expessura == dados_modelo["expessura"] and m.quantidade_oleo == \
                    dados_modelo["Quantidade de oleo"]:
                self.__tela_modelo.mostra_mensagem("ATENCAO: Modelo já existente")
                break
        else:
            codigo = self.gerar_codigo()
            novo_modelo = Modelo(dados_modelo["nome"], dados_modelo["expessura"], dados_modelo["Quantidade de oleo"],
                                 codigo)
            self.__modelo_dao.add(novo_modelo)
            self.__tela_modelo.mostra_mensagem("Modelo cadastrado com sucesso")

    def alterar_modelo(self, modelo_codigo=None):
        self.lista_modelos()
        modelo_codigo = self.__tela_modelo.seleciona_modelo()
        modelo = self.pega_modelo_por_codigo(modelo_codigo)
        novos_dados_modelo = self.__tela_modelo.pega_dados_modelo({'nome': modelo.nome,
                                                                   'quantidade_oleo': modelo.quantidade_oleo,
                                                                   'expessura': modelo.expessura})

        if modelo is not None:
            modelo.nome = novos_dados_modelo["nome"]
            modelo.quantidade_oleo = novos_dados_modelo["Quantidade de oleo"]
            modelo.expessura = novos_dados_modelo["expessura"]
            self.lista_modelos()
        else:
            self.__tela_modelo.mostra_mensagem("ATENCAO: Amigo não existente")

    def lista_modelos(self):
        if self.__modelo_dao.get_size() == 0:
            return None
        else:
            for modelo in self.__modelo_dao.get_all():
                self.__tela_modelo.mostrar_modelo({"nome": modelo.nome, "quantidade_oleo": modelo.quantidade_oleo, "expessura": modelo.expessura, "codigo": modelo.codigo})
                return True

    def excluir_modelo(self):
        self.lista_modelos()
        codigo_modelo = self.__tela_modelo.seleciona_modelo()
        modelo = self.pega_modelo_por_codigo(codigo_modelo)

        if modelo is not None:
          self.__modelo_dao.remove(modelo)
          self.lista_modelos()
          self.__tela_modelo.mostra_mensagem("Modelo removido com sucesso.")
        else:
          self.__tela_modelo.mostra_mensagem("ATENCAO: Modelo não existente")

    def adicionar_oleo(self, oleo):
        for modelo in self.__modelo_dao.get_all():
            if modelo.expessura == oleo.expessura:
                modelo.incluir_oleo(oleo)

    def remover_oleo(self, oleo):
        for md in self.__modelo_dao.get_all():
            if md.expessura == oleo.expessura:
                for ol in md.oleos:
                    if ol.codigo == oleo.codigo:
                        if md.exclui_oleo(oleo) is not None:
                            return "Oleo Removido"
                else:
                    return "Oleo nao encontrado"
        else:
            return "Modelo nao encontrado"
    def listar_oleos(self):
        self.lista_modelos()
        codigo = self.__tela_modelo.seleciona_modelo()
        modelo = self.pega_modelo_por_codigo(codigo)
        if modelo is not None:
            self.listar_oleos_do_modelo(modelo)

    def listar_oleos_do_modelo(self, modelo):
        for oleo in modelo.oleos:
            self.__tela_modelo.mostra_oleo_modelo({"fornecedor": oleo.fornecedor.cnpj, "marca": oleo.marca, "valor": oleo.valor, "codigo": oleo.codigo})

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_modelo,
            2: self.alterar_modelo,
            3: self.lista_modelos,
            4: self.excluir_modelo,
            5: self.listar_oleos,
            0: self.retornar
        }

        lista_modelo = []
        for modelo in self.__modelo_dao.get_all():
            lista_modelo.append([modelo.nome, modelo.quantidade_oleo, modelo.expessura, modelo.codigo])
        dados_tela = self.__tela_modelo.tela_opcoes(lista_modelo)
        opcao = dados_tela['opcao']
        if opcao in lista_opcoes:
            lista_opcoes[opcao]()
        else:
            self.__tela_modelo.mostra_mensagem('Opção Inválida')

    def retornar(self):
        self.__controlador_sistema.abre_tela()
