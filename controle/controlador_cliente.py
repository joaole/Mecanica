from entidade.cliente import Cliente
from entidade.veiculo import Veiculo
from limite.tela_cliente import TelaCliente
from persistencia.cliente_dao import CLienteDAO
import re


class ControladorCliente:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_cliente = TelaCliente()
        self.__cliente_dao = CLienteDAO()

    def listar_clientes(self):
        if self.__cliente_dao.get_size() == 0:
            return self.__tela_cliente.mostra_mensagem("ATENCAO: Nenhum cliente cadastrado.")
        for cliente in self.__cliente_dao.get_all():
            self.__tela_cliente.mostra_cliente({
                "nome": cliente.nome,
                "telefone": cliente.telefone,
                "cpf": cliente.cpf,
                "email": cliente.email
            })

    def pega_cliente_por_cpf(self, cpf: int):
        for cliente in self.__cliente_dao.get_all():
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

    def inclui_cliente(self, cpf=None, placa=None):
        dados = self.__tela_cliente.pega_dados_cliente()
        cpf = dados["cpf"]
        telefone = dados["telefone"]
        email = dados["email"]

        if not self.verifica_cpf(cpf):
            self.__tela_cliente.mostra_mensagem("ATENÇÃO: CPF inválido")
            return
        if not self.verifica_telefone(telefone):
            self.__tela_cliente.mostra_mensagem("ATENÇÃO: Telefone inválido")
            return
        if not self.verifica_email(email):
            self.__tela_cliente.mostra_mensagem("ATENÇÃO: Email inválido")
            return

        novo_cliente = Cliente(dados["nome"], telefone, email, cpf)
        if self.pega_cliente_por_cpf(novo_cliente.cpf) is None:
            self.__cliente_dao.add(novo_cliente)
            self.__tela_cliente.mostra_mensagem(f"{novo_cliente.nome} cadastrado com sucesso.")
        else:
            self.__tela_cliente.mostra_mensagem("ATENÇÃO: CPF duplicado")

    def altera_cliente(self):
        self.listar_clientes()
        cpf_cliente = self.__tela_cliente.seleciona_cliente()
        cliente = self.pega_cliente_por_cpf(cpf_cliente)
        if cliente is not None:
            novos_dados_cliente = self.__tela_cliente.pega_dados_cliente()
            if not self.verifica_cpf(novos_dados_cliente["cpf"]):
                self.__tela_cliente.mostra_mensagem("ATENÇÃO: CPF inválido")
                return
            if not self.verifica_telefone(novos_dados_cliente["telefone"]):
                self.__tela_cliente.mostra_mensagem("ATENÇÃO: Telefone inválido")
                return
            if not self.verifica_email(novos_dados_cliente["email"]):
                self.__tela_cliente.mostra_mensagem("ATENÇÃO: Email inválido")
                return
            cliente.nome = novos_dados_cliente["nome"]
            cliente.cpf = novos_dados_cliente["cpf"]
            cliente.email = novos_dados_cliente["email"]
            cliente.telefone = novos_dados_cliente["telefone"]
            self.__tela_cliente.mostra_mensagem("Cliente alterado com sucesso")
        else:
            self.__tela_cliente.mostra_mensagem("ATENÇÃO: Cliente não existente")

    def exclui_cliente(self):
        self.listar_clientes()
        cpf_cliente = self.__tela_cliente.seleciona_cliente()
        cliente = self.pega_cliente_por_cpf(cpf_cliente)
        if cliente is not None:
            self.__cliente_dao.remove(cliente)
        else:
            self.__tela_cliente.mostra_mensagem("ATENÇÃO: Cliente não existente")

    def inclui_veiculo(self):
        self.listar_clientes()
        cpf = self.__tela_cliente.seleciona_cliente()
        cliente = self.pega_cliente_por_cpf(cpf)
        if cliente is not None:
            modelo = self.__controlador_sistema.controlador_modelo.pega_modelo_por_codigo(self.__controlador_sistema.controlador_modelo.lista_modelos())
            if modelo is not None:
                dados = self.__tela_cliente.pega_dados_moto()
                if modelo is not None:
                    nova_moto = Veiculo(dados["placa"], dados["kilometragem"], modelo)
                    if self.pega_moto_por_placa(cliente, nova_moto.placa_moto) is None:
                        cliente.inclui_veiculo(nova_moto)
                        self.__cliente_dao.atualiza()
                        self.__tela_cliente.mostra_mensagem("Veiculo cadastrado com sucesso")
                    else:
                        self.__tela_cliente.mostra_mensagem("ATENÇÃO: Veículo já cadastrado.")
                else:
                    self.__tela_cliente.mostra_mensagem("ATENCAO: Modelo nao existente")
            else:
                self.__tela_cliente.mostra_mensagem("ATENCAO: Nenhum modelo cadastrado.")
        else:
            self.__tela_cliente.mostra_mensagem("ATENÇÃO: Cliente não existe")

    def exclui_veiculo(self):
        self.listar_clientes()
        cpf = self.__tela_cliente.seleciona_cliente()
        cliente = self.pega_cliente_por_cpf(cpf)
        if cliente is not None:
            self.listar_veiculos_cliente(cliente)
            placa_moto = self.__tela_cliente.seleciona_moto()
            moto = self.pega_moto_por_placa(cliente, placa_moto)
            if moto is not None:
                cliente.veiculos.remove(moto)
                self.__cliente_dao.atualiza()
                self.__tela_cliente.mostra_mensagem("Veiculo removido com sucesso.")
            else:
                self.__tela_cliente.mostra_mensagem("ATENÇÃO: Moto não cadastrada")
        else:
            self.__tela_cliente.mostra_mensagem("ATENÇÃO: Cliente não cadastrado")

    def altera_veiculo(self):
        self.listar_clientes()
        cpf_cliente = self.__tela_cliente.seleciona_cliente()
        cliente = self.pega_cliente_por_cpf(cpf_cliente)
        if cliente is not None:
            self.listar_veiculos_cliente(cliente)
            placa = self.__tela_cliente.seleciona_moto()
            novos_dados_moto = self.__tela_cliente.pega_dados_moto()
            for veiculo in cliente.veiculos:
                if veiculo.placa_moto == placa:
                    veiculo.placa_moto = novos_dados_moto["placa"]
                    veiculo.km_moto = novos_dados_moto["kilometragem"]
                    self.__tela_cliente.mostra_mensagem("Veiculo alterado com sucesso")
                    break
            else:
                self.__tela_cliente.mostra_mensagem("ATENÇÃO: Nenhum veículo cadastrado com esta placa.")
        else:
            self.__tela_cliente.mostra_mensagem("ATENÇÃO: Nenhum cliente cadastrado com este CPF")

    def listar_veiculos(self):
        self.listar_clientes()
        cpf = self.__tela_cliente.seleciona_cliente()
        cliente = self.pega_cliente_por_cpf(cpf)
        if cliente is not None:
            self.listar_veiculos_cliente(cliente)
        if len(cliente.veiculos) == 0:
            self.__tela_cliente.mostra_mensagem("ATENCAO: Nenhum veiculo cadastrado.")

    def listar_veiculos_cliente(self, cliente):
        for veiculo in cliente.veiculos:
            self.__tela_cliente.mostra_veiculo({
                    "modelo": veiculo.modelo.nome,
                    "kilometragem": veiculo.km_moto,
                    "placa": veiculo.placa_moto
                })

    def verifica_cpf(self, cpf):
        cpf = ''.join(filter(str.isdigit, cpf))
        if len(cpf) != 11:
            return False

        if cpf == cpf[0] * 11:
            return False

        def calcula_digito(cpf, pesos):
            soma = sum(int(digito) * peso for digito, peso in zip(cpf, pesos))
            resto = soma % 11
            return 0 if resto < 2 else 11 - resto
        pesos1 = range(10, 1, -1)
        pesos2 = range(11, 1, -1)
        digito1 = calcula_digito(cpf[:9], pesos1)
        digito2 = calcula_digito(cpf[:10], pesos2)
        return cpf[-2:] == f"{digito1}{digito2}"

    def verifica_telefone(self, telefone):
        telefone = ''.join(filter(str.isdigit, telefone))
        return len(telefone) in [10, 11]

    def verifica_email(self, email):
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email) is not None

    def abre_tela(self):
        lista_opcoes = {
            1: self.inclui_cliente,
            2: self.altera_cliente,
            3: self.listar_clientes,
            4: self.exclui_cliente,
            5: self.inclui_veiculo,
            6: self.altera_veiculo,
            7: self.exclui_veiculo,
            8: self.listar_veiculos,
            0: self.retornar
        }

        lista_cliente = []
        for cliente in self.__cliente_dao.get_all():
            lista_cliente.append([cliente.nome, cliente.cpf, cliente.telefone,
                                  cliente.email, cliente.veiculos])
        dados_tela = self.__tela_cliente.tela_opcoes(lista_cliente)
        opcao = dados_tela['opcao']
        if opcao in lista_opcoes:
            if opcao == 0:
                lista_opcoes[opcao]()
            else:
                lista_opcoes[opcao](dados_tela.get('cpf', 'placa'))
        else:
            self.__tela_cliente.mostra_mensagem('Opção Inválida')

    def retornar(self):
        self.__controlador_sistema.abre_tela()
