from entidade.troca_de_oleo import TrocaDeOleo
from limite.tela_troca_de_oleo import TelaTrocaDeOleo
from persistencia.troca_de_oleo_entrada_dao import TrocaDeOleoEntradaDAO
from persistencia.troca_de_oleo_saida_dao import TrocaDeOleoSaidaDAO


class ControladorTrocaDeOleo:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_troca_de_oleo = TelaTrocaDeOleo()
        self.__troca_de_oleo_entrada_dao = TrocaDeOleoEntradaDAO()
        self.__troca_de_oleo_saida_dao = TrocaDeOleoSaidaDAO()

    def pega_troca_por_codigo(self, lista, codigo):
        for troca in lista.get_all:
            if troca.codigo == codigo:
                return troca
        else:
            return None

    def cadastrar_troca(self):
        self.__controlador_sistema.controlador_cliente.listar_clientes()
        cpf_cliente = self.__tela_troca_de_oleo.pega_dados_cliente()
        cliente = self.__controlador_sistema.controlador_cliente.pega_cliente_por_cpf(cpf_cliente)
        if cliente is not None:
            self.__controlador_sistema.controlador_cliente.listar_veiculos_cliente(cliente)
            placa_moto = self.__tela_troca_de_oleo.seleciona_moto()
            veiculo = self.__controlador_sistema.controlador_cliente.pega_moto_por_placa(cliente, placa_moto)
            if veiculo is not None:
                data_entrada = self.__tela_troca_de_oleo.pega_data_entrada()
                for troca in self.__troca_de_oleo_entrada_dao.get_all():
                    if (troca.cliente == cliente
                            and troca.veiculo == veiculo
                            and troca.data_entrada == data_entrada):
                        (self.__tela_troca_de_oleo.mostra_mensagem
                         ("ATENCAO: Ja possui uma troca com o mesmo cliente, veiculo e data de entrada"))
                else:
                    nova_troca = TrocaDeOleo(veiculo, cliente, data_entrada)
                    self.__troca_de_oleo_entrada_dao.add(nova_troca)
                    self.__tela_troca_de_oleo.mostra_mensagem("Troca cadastrada com sucesso")
            else:
                self.__tela_troca_de_oleo.mostra_mensagem("ATENCAO: Veiculo nao cadastrado")
        else:
            self.__tela_troca_de_oleo.mostra_mensagem("ATENCAO: Cliente nao cadastrado")

    def finalizar_troca(self):
        self.listar_trocas()
        codigo = self.__tela_troca_de_oleo.seleciona_troca()
        troca = self.pega_troca_por_codigo(self.__troca_de_oleo_entrada_dao, codigo)
        if troca is not None:
            self.__controlador_sistema.controlador_modelo.listar_oleos_do_modelo(troca.veiculo.modelo)
            dados_saida = self.__tela_troca_de_oleo.pega_dados_saida_veiculo()
            oleo = self.__controlador_sistema.controlador_oleo.pega_oleo_por_codigo(dados_saida["codigo_oleo"])
            troca.data_saida = dados_saida["data_saida"]
            troca.oleo = oleo
            troca.valor_final = self.calcular_valor_troca(troca)
            self.finaliza_troca(troca.codigo)
            print(troca.data_saida)
            print(troca.oleo.marca)
            print(troca.valor_final)
            self.__tela_troca_de_oleo.mostra_mensagem("Troca finalizada com sucesso")
        else:
            self.__tela_troca_de_oleo.mostra_mensagem("ATENCAO: Troca nao encontrada")

    def listar_oleos_modelo_da_troca(self):
        pass

    def finaliza_troca(self, codigo):
        for troca in self.__troca_de_oleo_entrada_dao.get_all():
            if troca.codigo == codigo:
                self.__troca_de_oleo_saida_dao.add(troca)
                self.__troca_de_oleo_entrada_dao.remove(troca)
        else:
            return None

    def cancelar_troca(self, codigo):
        for troca in self.__troca_de_oleo_entrada_dao.get_all():
            if troca.codigo == codigo:
                self.__troca_de_oleo_entrada_dao.remove(troca)

    def listar_trocas(self):
        for troca in self.__troca_de_oleo_entrada_dao.get_all():
            self.__tela_troca_de_oleo.mostra_troca({
                "nome": troca.cliente.nome,
                "placa": troca.veiculo.placa_moto,
                "modelo": troca.veiculo.modelo.nome,
                "data_entrada": troca.data_entrada,
                "espessura": troca.veiculo.modelo.expessura,
                "oleo": None,
                "valor_final": None,
                "data_saida": None,
                "codigo": troca.codigo
            })

    def listar_trocas_efetuadas(self):
        for troca in self.__troca_de_oleo_saida_dao.get_all():
            self.__tela_troca_de_oleo.mostra_troca({
                "nome": troca.cliente.nome,
                "placa": troca.veiculo.placa_moto,
                "modelo": troca.veiculo.modelo.nome,
                "data_entrada": troca.data_entrada,
                "espessura": troca.veiculo.modelo.expessura,
                "oleo": troca.oleo.marca,
                "valor_final": troca.valor_final,
                "data_saida": troca.data_saida,
                "codigo": troca.codigo
            })

    def calcular_valor_troca(self, troca):
        valor_final = troca.calcula_valor_final(troca.veiculo, troca.oleo)
        return valor_final

    def abre_tela(self):
        lista_opcoes = {
            1: self.cadastrar_troca,
            2: self.finalizar_troca,
            3: self.listar_trocas,
            4: self.listar_trocas_efetuadas,
            0: self.retornar
        }

        continua = True
        while continua:
            opcao = self.__tela_troca_de_oleo.tela_opcoes()
            if opcao in lista_opcoes:
                lista_opcoes[opcao]()
            else:
                self.__tela_troca_de_oleo.mostra_mensagem("Opção inválida")

    def retornar(self):
        self.__controlador_sistema.abre_tela()
