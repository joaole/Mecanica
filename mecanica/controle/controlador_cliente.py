from entidade.cliente import Cliente
from entidade.veiculo import Veiculo
from entidade.modelo import Modelo


class ControladorCliente:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_cliente = TelaCliente()
        self.__clientes = []

    def pega_cliente_por_cpf(self, cpf: int):
        

    def inclui_cliente(self, nome, telefone, email, cpf):
        novo_cliente = Cliente(nome, telefone, email, cpf)
        for cliente in self.__clientes:
            if cliente.cpf == cpf:
                return None
        else:
            self.__clientes.append(novo_cliente)
            return novo_cliente

    def altera_cliente_nome(self, cpf, nome):
        for cliente in self.__clientes:
            if cliente.cpf == cpf:
                cliente.nome = nome
        else:
            return None

    def altera_cliente_email(self, cpf, novo_email):
        for cliente in self.__clientes:
            if cliente.cpf == cpf:
                cliente.email = novo_email
        else:
            return None

    def altera_cliente_telefone(self, cpf, novo_telefone):
        for cliente in self.__clientes:
            if cliente.cpf == cpf:
                cliente.telefone = novo_telefone
        else:
            return None

    def altera_cliente_cpf(self, cpf, novo_cpf):
        for cliente in self.__clientes:
            if cliente.cpf == cpf:
                cliente.cpf = novo_cpf

    def exclui_cliente(self, cpf):
        for cliente in self.__clientes:
            if cliente.cpf == cpf:
                self.__clientes.remove(cliente)
                return cliente
        else:
            return None

    def seleciona_cliente(self, cpf):
        for cliente in self.__clientes:
            if cliente.cpf == cpf:
                return cliente
        else:
            return None

    def inclui_veiculo(self, cpf, placa_moto, km_moto, modelo):
        if isinstance(cpf, int) and isinstance(placa_moto, str) and isinstance(modelo, Modelo):
            novo_veiculo = Veiculo(placa_moto, km_moto, modelo)
        for cliente in self.__clientes:
            if cliente.cpf == cpf:
                for veiculo in cliente.veiculos:
                    if veiculo.placa_moto == placa_moto:
                        return None
                else:
                    cliente.inclui_veiculo(novo_veiculo)
                    return novo_veiculo
        else:
            return None

    def exclui_veiculo(self, cpf, placa_moto):
        for cliente in self.__clientes:
            if cliente.cpf == cpf:
                for veiculo in cliente.veiculos:
                    if veiculo.placa_moto == placa_moto:
                        cliente.exclui_veiculo(veiculo)
                        return veiculo
                    else:
                        return None
        else:
            return None

    def altera_placa_veiculo(self, cpf, placa_moto, nova_placa):
        for cliente in self.__clientes:
            if cliente.cpf == cpf:
                for veiculo in cliente.veiculos:
                    if veiculo.placa_moto == placa_moto:
                        veiculo.placa_moto = nova_placa

    def altera_km_veiculo(self, cpf, placa_moto, nova_km):
        for cliente in self.__clientes:
            if cliente.cpf == cpf:
                for veiculo in cliente.veiculos:
                    if veiculo.placa_moto == placa_moto:
                        veiculo.km_moto = nova_km
                        return veiculo
        else:
            return None
