from controle.controlador_modelo import ControladorModelo
from controle.controlador_troca_de_oleo import ControladorTrocaDeOleo
from controle.controlador_oleo import ControladorOleo
from controle.controlador_cliente import ControladorCliente
from controle.controlador_fornecedor import ControladorFornecedor
from limite.tela_sistemas import TelaSistema


class ControladorSistema:
    def __init__(self):
        self.__controlador_oleo = ControladorOleo(self)
        self.__controlador_cliente = ControladorCliente(self)
        self.__controlador_fornecedor = ControladorFornecedor()
        self.__controlador_modelo = ControladorModelo(self)
        self.__controlador_troca_de_oleo = ControladorTrocaDeOleo()
        self.__tela_sistema = TelaSistema()

    @property
    def controlador_oleo(self):
        return self.__controlador_oleo

    @property
    def controlador_cliente(self):
        return self.__controlador_cliente

    @property
    def controlador_fornecedor(self):
        return self.__controlador_fornecedor

    @property
    def controlador_modelo(self):
        return self.__controlador_modelo

    @property
    def controlador_troca_de_oleo(self):
        return self.__controlador_troca_de_oleo

    def validar_cnpj(self, cnpj: str) -> bool:
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

    def cadastrar_oleo(self):
        self.__controlador_oleo.abre_tela()

    def cadastrar_cliente(self):
        self.__controlador_cliente.abre_tela()

    def cadastrar_fornecedor(self):
        self.__controlador_fornecedor.abre_tela()

    def cadastrar_modelo(self):
        self.__controlador_modelo.abre_tela()

    def cadastrar_troca_de_oleo(self):
        self.__controlador_troca_de_oleo.abre_tela()

    def inicializa_sistema(self):
        self.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.cadastrar_fornecedor, 2: self.cadastrar_oleo, 3: self.cadastrar_modelo,
                        4: self.cadastrar_cliente, 5: self.cadastrar_troca_de_oleo, 0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def encerra_sistema(self):
        exit(0)
