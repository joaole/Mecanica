from entidade.troca_de_oleo import TrocaDeOleo
from limite.tela_troca_de_oleo import TelaTrocaDeOleo


class ControladorTrocaDeOleo:
    def __init__(self,controlador_sistema, modelo=None):
        self.__controlador_sistema = controlador_sistema
        self.__tela_troca_de_oleo = TelaTrocaDeOleo()
        self.__trocas = []

    def gerar_codigo(self):
        codigo = len(self.__trocas) + 1
        return codigo

    def pega_troca_por_codigo(self, codigo):
        for troca in self.__trocas:
            if troca.codigo == codigo:
                return troca
        else:
            return None
    def efetuar_troca(self, dados_troca):
        cliente = self.__controlador_sistema.controlador_cliente.pega_cliente_por_cpf(dados_troca["cpf_cliente"])
        if cliente is not None:
            veiculo = self.__controlador_sistema.controlador_cliente.pega_moto_por_placa(cliente, dados_troca["placa_moto"])
            if veiculo is not None:
                codigo = self.gerar_codigo()
                nova_troca = TrocaDeOleo(veiculo, cliente, dados_troca["data_entrada"], None, codigo)
                for troca in self.__trocas:
                    if troca.cliente != nova_troca.cliente and troca.veiculo != nova_troca.veiculo and troca.data_entrada != nova_troca.data_entrada:
                        self.__trocas.append(nova_troca)
                    else:
                        self.__tela_troca_de_oleo.mostra_mensagem("ATENCAO: Ja possui uma troca com o mesmo cliente, veiculo e data de entrada")



    def cancelar_troca(self, codigo):
        for troca in self.__trocas:
            if troca.codigo == codigo:
                self.__trocas.remove(troca)

    def calcular_quantidade_oleo(self):


        else:
            return 0
