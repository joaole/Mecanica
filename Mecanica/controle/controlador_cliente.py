from entidade.cliente import Cliente
from entidade.veiculo import Veiculo
from limite.tela_cliente import TelaCliente


class ControladorCliente:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_cliente = TelaCliente()
        self.__clientes = []

    def listar_clientes(self):
        for cliente in self.__clientes:
            self.__tela_cliente.mostra_cliente({"nome": cliente.nome, "telefone": cliente.telefone, "cpf": cliente.cpf, "email": cliente.email})

    def pega_cliente_por_cpf(self, cpf: int):
        for cliente in self.__clientes:
            if cliente.cpf == cpf:
                return cliente
        else:
            return None

    def pega_moto_por_placa(self, cliente, placa_moto):
        for veiculo in cliente.veiculos:
            if veiculo.placa_moto == placa_moto:
                return veiculo
        else:
            return None

    def inclui_cliente(self):
        dados = self.__tela_cliente.pega_dados_cliente()
        novo_cliente = Cliente(dados["nome"], dados["telefone"], dados["email"], dados["cpf"])

        if self.pega_cliente_por_cpf(novo_cliente.cpf) is None:
            self.__clientes.append(novo_cliente)
            self.__tela_cliente.mostra_mensagem(f"{novo_cliente.nome} cadastrado com sucesso.")
        else:
            self.__tela_cliente.mostra_mensagem("ATENCAO: CPF duplicado")

    def altera_cliente(self):
        self.listar_clientes()
        cpf_amigo = self.__tela_cliente.seleciona_cliente()
        cliente = self.pega_cliente_por_cpf(cpf_amigo)
        if cliente is not None:
            novos_dados_cliente = self.__tela_cliente.pega_dados_cliente()
            cliente.nome = novos_dados_cliente["nome"]
            cliente.cpf = novos_dados_cliente["cpf"]
            cliente.email = novos_dados_cliente["email"]
            cliente.telefone = novos_dados_cliente["telefone"]
            self.__tela_cliente.mostra_mensagem("Cliente removido")
        else:
            self.__tela_cliente.mostra_mensagem("ATENCAO: Cliente não existente")

    def exclui_cliente(self):
        self.listar_clientes()
        cpf_cliente = self.__tela_cliente.seleciona_cliente()
        cliente = self.pega_cliente_por_cpf(cpf_cliente)
        if cliente is not None:
            self.__clientes.remove(cliente)
        else:
            self.__tela_cliente.mostra_mensagem("ATENCAO: Cliente nao existente")

    def inclui_veiculo(self):
        self.listar_clientes()
        cpf = self.__tela_cliente.seleciona_cliente()
        cliente = self.pega_cliente_por_cpf(cpf)
        dados = self.__tela_cliente.pega_dados_moto()
        nova_moto = Veiculo(dados["placa"], dados["kilometragem"], dados["modelo"])
        if cliente is not None:
            if self.pega_moto_por_placa(cliente, nova_moto.placa_moto) is None:
                cliente.inclui_veiculo(nova_moto)
            else:
                self.__tela_cliente.mostra_mensagem("ATENCAO: Veiculo ja cadastrado.")
        else:
            self.__tela_cliente.mostra_mensagem("ATENCAO: Cliente não existe")

    def exclui_veiculo(self):
        self.listar_clientes()
        cpf = self.__tela_cliente.seleciona_cliente()
        cliente = self.pega_cliente_por_cpf(cpf)
        if cliente is not None:
            self.listar_veiculos()
            placa_moto = self.__tela_cliente.seleciona_moto()
            moto = self.pega_moto_por_placa(cliente, placa_moto)
            if moto is not None:
                cliente.veiculos.remove(moto)
            else:
                self.__tela_cliente.mostra_mensagem("ATENCAO: Moto nao cadastrada")
        else:
            self.__tela_cliente.mostra_mensagem("ATENCAO: Cliente nao cadastrado")

    def altera_veiculo(self):
        self.listar_clientes()
        cpf_cliente = self.__tela_cliente.seleciona_cliente()
        cliente = self.pega_cliente_por_cpf(cpf_cliente)
        if cliente is not None:
            self.listar_veiculos()
            placa = self.__tela_cliente.seleciona_moto()
            novos_dados_moto = self.__tela_cliente.pega_dados_moto()
            for veiculo in cliente.veiculos:
                if veiculo.placa_moto == placa:
                    veiculo.placa_moto = novos_dados_moto["placa"]
                    veiculo.km_moto = novos_dados_moto["kilometragem"]
                    veiculo.modelo = novos_dados_moto["modelo"]
            else:
                self.__tela_cliente.mostra_mensagem("ATENCAO: Nenhum veículo cadastrado com esta placa.")
        else:
            self.__tela_cliente.mostra_mensagem("ATENCAO: Nenhum cliente cadastrado com este CPF")

    def listar_veiculos(self):
        cpf = self.__tela_cliente.seleciona_cliente()
        cliente = self.pega_cliente_por_cpf(cpf)
        if cliente is not None:
            for veiculo in cliente.veiculos:
                self.__tela_cliente.mostra_veiculo({"modelo": veiculo.modelo, "kilometragem": veiculo.km_moto, "placa": veiculo.placa_moto})

    def abre_tela(self):
        lista_opcoes = {1: self.inclui_cliente, 2: self.altera_cliente, 3: self.listar_clientes,
                        4: self.exclui_cliente, 5: self.inclui_veiculo, 6: self.altera_veiculo,
                        7: self.exclui_veiculo, 8: self.listar_veiculos, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_cliente.tela_opcoes()]()

    def retornar(self):
        self.__controlador_sistema.abre_tela()
