from limite.tela_modelo import TelaModelo
from entidade.modelo import Modelo


class ControladorModelo:
    def __init__(self, controlador_sistema):
        self.__modelos = []
        self.__tela_modelo = TelaModelo()
        self.__controlador_sistema = controlador_sistema

    def gerar_codigo(self):
        codigo = str(len(self.__modelos) + 1)
        return codigo

    def pega_modelo_por_codigo(self, codigo: int):
        for modelo in self.__modelos:
            if modelo.codigo == codigo:
                return modelo
        return None

    def incluir_modelo(self):
        dados_modelo = self.__tela_modelo.pega_dados_modelo()

        for m in self.__modelos:
            if m.nome == dados_modelo["nome"] and m.expessura == dados_modelo["expessura"] and m.quantidade_oleo == dados_modelo["Quantidade de oleo"]:
                self.__tela_modelo.mostra_mensagem("ATENCAO: Modelo já existente")
                break
        else:
            codigo = self.gerar_codigo()
            novo_modelo = Modelo(dados_modelo["nome"], dados_modelo["expessura"], dados_modelo["Quantidade de oleo"], codigo)
            self.__modelos.append(novo_modelo)
            self.__tela_modelo.mostra_mensagem("Modelo cadastrado com sucesso")

    def alterar_modelo(self):
        self.lista_modelos()
        modelo_codigo = self.__tela_modelo.seleciona_modelo()
        modelo = self.pega_modelo_por_codigo(modelo_codigo)

        if modelo is not None:
            novos_dados_modelo = self.__tela_modelo.pega_dados_modelo()
            modelo.nome = novos_dados_modelo["nome"]
            modelo.quantidade_oleo = novos_dados_modelo["Quantidade de oleo"]
            modelo.expessura = novos_dados_modelo["expessura"]
            self.lista_modelos()
        else:
            self.__tela_modelo.mostra_mensagem("ATENCAO: Amigo não existente")


    def lista_modelos(self):
        if len(self.__modelos) == 0:
            return self.__tela_modelo.mostra_mensagem("ATENCAO: Nenhum modelo cadastrado.")
        for modelo in self.__modelos:
            self.__tela_modelo.mostra_modelo({"nome": modelo.nome, "quantidade_oleo": modelo.quantidade_oleo, "expessura": modelo.expessura, "codigo": modelo.codigo})

    def excluir_modelo(self):
        self.lista_modelos()
        codigo_modelo = self.__tela_modelo.seleciona_modelo()
        modelo = self.pega_modelo_por_codigo(codigo_modelo)

        if modelo is not None:
          self.__modelos.remove(modelo)
          self.lista_modelos()
          self.__tela_modelo.mostra_mensagem("Modelo removido com sucesso.")
        else:
          self.__tela_modelo.mostra_mensagem("ATENCAO: Modelo não existente")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def adicionar_oleo(self, oleo):
        for modelo in self.__modelos:
            if modelo.expessura == oleo.expessura:
                modelo.incluir_oleo(oleo)

    def remover_oleo(self, oleo):
        for md in self.__modelos:
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
        codigo = self.__tela_modelo.seleciona_modelo()
        modelo = self.pega_modelo_por_codigo(codigo)
        for oleo in modelo.oleos:
            self.__tela_modelo.mostra_oleo_modelo({"fornecedor": oleo.fornecedor.cnpj, "marca": oleo.marca, "valor": oleo.valor, "codigo": oleo.codigo})



    def abre_tela(self):
        lista_opcoes = {1: self.incluir_modelo, 2: self.alterar_modelo, 3: self.lista_modelos, 4: self.excluir_modelo, 5: self.listar_oleos, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_modelo.tela_opcoes()]()
