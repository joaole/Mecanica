from entidade.fornecedor import Fornecedor
from limite.tela_fornecedor import TelaFornecedor
from persistencia.fornecedor_dao import FornecedorDAO
import re


class ControladorFornecedor:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_fornecedor = TelaFornecedor()
        self.__fornecedor_dao = FornecedorDAO()

    @property
    def fornecedores(self):
        return self.__fornecedor_dao.get_all()

    def listar_fornecedores(self):
        if self.__fornecedor_dao.get_size() == 0:
            self.__tela_fornecedor.mostra_mensagem("ATENCAO: Nenhum fornecedor cadastrado.")
        else:
            lista_fornecedores = []
            for fornecedor in self.__fornecedor_dao.get_all():
                lista_fornecedores.append([fornecedor.nome, fornecedor.cnpj])

            return self.__tela_fornecedor.mostrar_fornecedor(lista_fornecedores)

    def altera_fornecedor(self, cnpj):
        fornecedor = self.pega_fornecedor_por_cnpj(cnpj)
        if fornecedor is not None:
            dados = self.__tela_fornecedor.pega_dados_fornecedor({'nome': fornecedor.nome, 'telefone': fornecedor.telefone,
                                                                  'email': fornecedor.email, 'cnpj': fornecedor.cnpj})
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
        for fornecedor in self.__fornecedor_dao.get_all():
            if fornecedor.cnpj == cnpj:
                return fornecedor
        return None

    def inclui_fornecedor(self, cnpj=None):
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
            self.__fornecedor_dao.add(novo_fornecedor)
            self.__tela_fornecedor.mostra_mensagem("Fornecedor cadastrado com sucesso")
        else:
            self.__tela_fornecedor.mostra_mensagem("ATENÇÃO: CNPJ duplicado")

    def exclui_fornecedor(self, cnpj):
        fornecedor = self.pega_fornecedor_por_cnpj(cnpj)
        if fornecedor is not None:
            self.__fornecedor_dao.remove(fornecedor)
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
        }

        continua = True
        while continua:
            lista_fornecedores = []
            for fornecedor in self.__fornecedor_dao.get_all():
                lista_fornecedores.append([fornecedor.nome, fornecedor.cnpj, fornecedor.telefone, fornecedor.email])
            dados_tela = self.__tela_fornecedor.tela_opcoes(lista_fornecedores)
            opcao = dados_tela['opcao']
            if opcao in lista_opcoes:
                lista_opcoes[opcao](dados_tela['cnpj'])
            elif opcao == 0:
                self.retornar()
            else:
                self.__tela_fornecedor.mostra_mensagem("Opção inválida")

    def retornar(self):
        self.__controlador_sistema.abre_tela()


