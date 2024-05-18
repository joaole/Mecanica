from entidade.oleo import Oleo
from controlador_oleo import ControladorOleo
from controlador_cliente import ControladorCliente
from controlador_fornecedor import ControladorFornecedor


class ControladorSistema:
    def __init__(self):
        pass

    def validar_cpf(self, cpf: str) -> bool:
        cpf = ''.join(filter(str.isdigit, cpf))

        if len(cpf) != 11 or cpf == cpf[0] * 11:
            return False

        for i in range(9, 11):
            soma = sum(int(cpf[j]) * (i + 1 - j) for j in range(i))
            digito = (soma * 10) % 11
            if digito == 10:
                digito = 0
            if cpf[i] != str(digito):
                return False
        return True

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

    def cadastrar_oleo(self, fornecedor, marca, expessura):
        codigo = 0
        novo_oleo = Oleo(fornecedor, marca, expessura, codigo)
        ControladorOleo.inclui_oleo(fornecedor, marca, expessura, codigo)

    def cadastrar_cliente(self, nome, telefone, email, cpf):
        if self.validar_cpf(cpf) is True:
            ControladorCliente.inclui_cliente(nome, telefone, email, cpf)

    def cadastrar_fornecedor(self, nome, telefone, email, cnpj):
        pass
