from entidade.fornecedor import Fornecedor
from limite.tela_fornecedor import TelaFornecedor
import re


class ControladorFornecedor:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_fornecedor = TelaFornecedor()
        self.__fornecedores = []

    @property
    def fornecedores(self):
        return self.__fornecedores

    def listar_fornecedores(self):
        for fornecedor in self.__fornecedores:
            self.__tela_fornecedor.mostra_fornecedor({
                "nome": fornecedor.nome,
                "email": fornecedor.email,
                "telefone": fornecedor.telefone,
                "cnpj": fornecedor.cnpj
            })

    def altera_fornecedor(self):
        self.listar_fornecedores()
        cnpj = self.__tela_fornecedor.seleciona_fornecedor()
        fornecedor = self.pega_fornecedor_por_cnpj(cnpj)
        if fornecedor is not None:
            dados = self.__tela_fornecedor.pega_dados_fornecedor()
            if not self.verifica_cnpj(dados["cnpj"]):
                self.__tela_fornecedor.mostra_mensagem("ATENÇÃO: CNPJ inválido")
                return
            if not self.verifica_telefone(dados["telefone"]):
                self.__tela_fornecedor.mostra_mensagem("ATENÇÃO: Telefone inválido")
                return
            if not self.verifica_email(dados["email"]):
                self.__tela_fornecedor.mostra_mensagem("ATENÇÃO: Email inválido")
                return
            fornecedor.nome = dados["nome"]
            fornecedor.telefone = dados["telefone"]
            fornecedor.email = dados["email"]
            fornecedor.cnpj = dados["cnpj"]
            self.__tela_fornecedor.mostra_mensagem("Fornecedor alterado com sucesso")
        else:
            self.__tela_fornecedor.mostra_mensagem("ATENÇÃO: Fornecedor não cadastrado")

    def pega_fornecedor_por_cnpj(self, cnpj):
        for fornecedor in self.__fornecedores:
            if fornecedor.cnpj == cnpj:
                return fornecedor
        return None

    def inclui_fornecedor(self):
        dados = self.__tela_fornecedor.pega_dados_fornecedor()
        cnpj = dados["cnpj"]

        if not self.verifica_cnpj(cnpj):
            self.__tela_fornecedor.mostra_mensagem("ATENÇÃO: CNPJ inválido")
            return
        if not self.verifica_telefone(dados["telefone"]):
            self.__tela_fornecedor.mostra_mensagem("ATENÇÃO: Telefone inválido")
            return
        if not self.verifica_email(dados["email"]):
            self.__tela_fornecedor.mostra_mensagem("ATENÇÃO: Email inválido")
            return

        novo_fornecedor = Fornecedor(dados["nome"], dados["telefone"], dados["email"], cnpj)
        if self.pega_fornecedor_por_cnpj(novo_fornecedor.cnpj) is None:
            self.__fornecedores.append(novo_fornecedor)
            self.__tela_fornecedor.mostra_mensagem("Fornecedor cadastrado com sucesso")
        else:
            self.__tela_fornecedor.mostra_mensagem("ATENÇÃO: CNPJ duplicado")

    def exclui_fornecedor(self):
        self.listar_fornecedores()
        cnpj_fornecedor = self.__tela_fornecedor.seleciona_fornecedor()
        fornecedor = self.pega_fornecedor_por_cnpj(cnpj_fornecedor)
        if fornecedor is not None:
            self.__fornecedores.remove(fornecedor)
            self.__tela_fornecedor.mostra_mensagem("Fornecedor removido com sucesso")
        else:
            self.__tela_fornecedor.mostra_mensagem("ATENÇÃO: Fornecedor não cadastrado")

    def verifica_cnpj(self, cnpj):
        cnpj = ''.join(filter(str.isdigit, cnpj))

        if len(cnpj) != 14 or cnpj == cnpj[0] * 14:
            return False

        def calcular_digito(cnpj, pesos):
            soma = sum(int(cnpj[i]) * peso for i, peso in enumerate(pesos))
            resto = soma % 11
            return '0' if resto < 2 else str(11 - resto)

        pesos1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        pesos2 = [6] + pesos1

        return (cnpj[12] == calcular_digito(cnpj[:12], pesos1) and
                cnpj[13] == calcular_digito(cnpj[:13], pesos2))

    def verifica_telefone(self, telefone):
        telefone = ''.join(filter(str.isdigit, telefone))
        return len(telefone) in [10, 11]

    def verifica_email(self, email):
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email) is not None

    def abre_tela(self):
        lista_opcoes = {
            1: self.inclui_fornecedor,
            2: self.altera_fornecedor,
            3: self.listar_fornecedores,
            4: self.exclui_fornecedor,
            0: self.retornar
        }

        continua = True
        while continua:
            opcao = self.__tela_fornecedor.tela_opcoes()
            if opcao in lista_opcoes:
                lista_opcoes[opcao]()
            else:
                self.__tela_fornecedor.mostra_mensagem("Opção inválida")

    def retornar(self):
        self.__controlador_sistema.abre_tela()
