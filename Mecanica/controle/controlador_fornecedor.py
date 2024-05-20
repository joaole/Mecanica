from entidade.fornecedor import Fornecedor
from limite.tela_fornecedor import TelaFornecedor


class ControladorFornecedor:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_fornecedor = TelaFornecedor()
        self.__fonecedores = []

    @property
    def fornecedores(self):
        return self.__fonecedores

    def listar_fornecedores(self):
        for fornecedor in self.__fonecedores:
            self.__tela_fornecedor.mostra_fornecedor({"nome": fornecedor.nome, "email": fornecedor.email, "telefone": fornecedor.telefone, "cnpj": fornecedor.cnpj})

    def altera_fornecedor(self):
        self.listar_fornecedores()
        cnpj = self.__tela_fornecedor.seleciona_fornecedor()
        fornecedor = self.pega_fornecedor_por_cnpj(cnpj)
        if fornecedor is not None:
            dados = self.__tela_fornecedor.pega_dados_fornecedor()
            fornecedor.nome = dados["nome"]
            fornecedor.telefone = dados["telefone"]
            fornecedor.email = dados["email"]
            fornecedor.cnpj = dados["cnpj"]
            self.__tela_fornecedor.mostra_mensagem("Fornecedor alterado com sucesso")
        else:
            self.__tela_fornecedor.mostra_mensagem("ATENCAO: Fornecedor nao cadastrado")

    def pega_fornecedor_por_cnpj(self, cnpj):
        for fornecedor in self.__fonecedores:
            if fornecedor.cnpj == cnpj:
                return fornecedor
        else:
            return None

    def inclui_fornecedor(self):
        dados = self.__tela_fornecedor.pega_dados_fornecedor()
        novo_fornecedor = Fornecedor(dados["nome"], dados["telefone"], dados["email"], dados["cnpj"])
        if self.pega_fornecedor_por_cnpj(novo_fornecedor) is None:
            self.__fonecedores.append(novo_fornecedor)
            self.__tela_fornecedor.mostra_mensagem("Fornecedor cadastrato com sucesso")
        else:
            self.__tela_fornecedor.mostra_mensagem("ATENCAO: CNPJ duplicado")

    def exclui_fornecedor(self):
        self.listar_fornecedores()
        cnpj_fornecedor = self.__tela_fornecedor.seleciona_fornecedor()
        fornecedor = self.pega_fornecedor_por_cnpj(cnpj_fornecedor)
        if fornecedor is not None:
            self.__fonecedores.remove(fornecedor)
            self.__tela_fornecedor.mostra_mensagem("Fornecedor removido com sucesso")
        else:
            self.__tela_fornecedor.mostra_mensagem("ATENCAO: Fornecedor nao cadastrado")

    def abre_tela(self):
        lista_opcoes = {1: self.inclui_fornecedor, 2: self.altera_fornecedor, 3: self.listar_fornecedores,
                        4: self.exclui_fornecedor, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_fornecedor.tela_opcoes()]()

    def retornar(self):
        self.__controlador_sistema.abre_tela()
