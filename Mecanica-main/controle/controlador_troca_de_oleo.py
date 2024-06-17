from entidade.troca_de_oleo import TrocaDeOleo
from limite.tela_troca_de_oleo import TelaTrocaDeOleo


class ControladorTrocaDeOleo:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_troca_de_oleo = TelaTrocaDeOleo()
        self.__trocas = []
        self.__trocas_efetuadas = []

    def gerar_codigo(self):
        codigo = str(len(self.__trocas) + 1)
        return codigo

    def pega_troca_por_codigo(self, codigo):
        for troca in self.__trocas:
            if troca.codigo == codigo:
                return troca
        else:
            return None

    def cadastrar_troca(self):
        self.__controlador_sistema.controlador_cliente.listar_clientes()
        cpf_cliente = self.__tela_troca_de_oleo.pega_dados_cliente()
        cliente = self.__controlador_sistema.controlador_cliente.pega_cliente_por_cpf(cpf_cliente)
        self.__controlador_sistema.controlador_cliente.listar_veiculos_cliente(cliente)
        dados_troca = self.__tela_troca_de_oleo.pega_dados_troca()
        if cliente is not None:
            veiculo = self.__controlador_sistema.controlador_cliente.pega_moto_por_placa(cliente, dados_troca["placa_moto"])
            if veiculo is not None:
                codigo = self.gerar_codigo()
                nova_troca = TrocaDeOleo(veiculo, cliente, dados_troca["data_entrada"], codigo)
                for troca in self.__trocas:
                    if troca.cliente == nova_troca.cliente and troca.veiculo == nova_troca.veiculo and troca.data_entrada == nova_troca.data_entrada:
                        self.__tela_troca_de_oleo.mostra_mensagem("ATENCAO: Ja possui uma troca com o mesmo cliente, veiculo e data de entrada")
                else:
                    self.__trocas.append(nova_troca)
                    self.__tela_troca_de_oleo.mostra_mensagem("Troca cadastrada com sucesso")
            else:
                self.__tela_troca_de_oleo.mostra_mensagem("ATENCAO: Veiculo nao cadastrado")
        else:
            self.__tela_troca_de_oleo.mostra_mensagem("ATENCAO: Veiculo nao cadastrado")

    def finalizar_troca(self):
        self.listar_trocas()
        codigo = self.__tela_troca_de_oleo.seleciona_troca()
        troca = self.pega_troca_por_codigo(codigo)
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
        for troca in self.__trocas:
            if troca.codigo == codigo:
                self.__trocas_efetuadas.append(troca)
                self.__trocas.remove(troca)
        else:
            return None

    def cancelar_troca(self, codigo):
        for troca in self.__trocas:
            if troca.codigo == codigo:
                self.__trocas.remove(troca)

    def listar_trocas(self):
        for troca in self.__trocas:
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
        for troca in self.__trocas_efetuadas:
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
