from limite.tela_modelo import TelaModelo
from entidade.modelo import Modelo

class ControladorModelo:
    def __init__(self, controlador_sistema):
        self.__modelos = []
        self.__tela_modelo = TelaModelo()
        self.__controlador_sistema = controlador_sistema

    def pega_modelo_por_codigo(self, codigo: int):
        for modelo in self.__modelos:
            if(modelo.codigo == codigo):
                return modelo
        return None

    # Sugestão: não deixe cadastrar dois amigos com o mesmo CPF
    def incluir_modelo(self):
        dados_modelo = self.__tela_modelo.pega_dados_modelo()
        modelo = Modelo(dados_modelo["nome"], dados_modelo["quantidade_oleo"], dados_modelo["codigo"])

        for m in self.__modelos:
            if m.codigo == modelo.codigo:
                return 'Modelo ja existente'
        else:
            self.__modelos.append(modelo)
    def alterar_modelo(self):
        self.lista_modelos()
        cpf_amigo = self.__tela_amigo.seleciona_amigo()
        amigo = self.pega_amigo_por_cpf(cpf_amigo)

        if(amigo is not None):
            novos_dados_amigo = self.__tela_amigo.pega_dados_amigo()
            amigo.nome = novos_dados_amigo["nome"]
            amigo.telefone = novos_dados_amigo["telefone"]
            amigo.cpf = novos_dados_amigo["cpf"]
            self.lista_amigos()
        else:
            self.__tela_amigo.mostra_mensagem("ATENCAO: Amigo não existente")

  # Sugestão: se a lista estiver vazia, mostrar a mensagem de lista vazia
    def lista_modelos(self):
        for modelo in self.__modelos:
            self.__tela_modelo.mostra_modelo({"Nome": modelo.nome, "Quantidade de Oleo": modelo.quantidade_oleo, "Codigo": modelo.codigo})
    def excluir_modelo(self):
        self.lista_modelos()
        codigo_modelo = self.__tela_modelo.seleciona_modelo()
        modelo = self.pega_modelo_por_codigo(codigo_modelo)

        if(modelo is not None):
          self.__modelos.remove(modelo)
          self.lista_modelos()
        else:
          self.__tela_modelo.mostra_mensagem("ATENCAO: Modelo não existente")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_modelo, 2: self.alterar_modelo, 3: self.lista_modelos, 4: self.excluir_modelo, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_modelo.tela_opcoes()]()
