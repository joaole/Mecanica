import PySimpleGUI as sg

class TelaCliente:
    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def init_opcoes(self):
        pass

    def tela_opcoes(self, dados_cliente=[], dados_veiculo=[]):
        sg.theme('DarkTeal4')
        # Cabeçalhos da tabela
        header_cliente = ['Nome', 'Cpf', 'Telefone', 'Email']
        header_veiculo = ['Modelo', 'Placa', 'KM']
        layout = [
            [sg.Text('-------- LISTA DE CLIENTE ----------', font=("Helvetica", 25))],
            [sg.Table(values=dados_cliente,
                      headings=header_cliente,
                      display_row_numbers=True,
                      auto_size_columns=True,
                      num_rows=min(15, len(dados_cliente)),
                      key='-TABLE_CLIENTE-',
                      row_height=25)],
            [
                sg.Button('Incluir Cliente', key=1), sg.Button('Alterar Cliente', key=2),
                sg.Button('Excluir Cliente', key=4),
            ],

            [sg.Text('-------- LISTA DE VEICULO ----------', font=("Helvetica", 25))],
            [sg.Table(values=dados_veiculo,
                      headings=header_veiculo,
                      display_row_numbers=True,
                      auto_size_columns=True,
                      num_rows=min(15, len(dados_veiculo)),
                      key='-TABLE_VEICULO-',
                      row_height=25)],
            [
                sg.Button('Incluir Veiculo', key=5),
                sg.Button('Alterar Veiculo', key=6), sg.Button('Excluir Veiculo', key=7)
            ],

            [sg.Button('Voltar', key=0)]
        ]
        self.__window = sg.Window('SisTroca de Oleo').Layout(layout)

        button, values = self.open()
        cpf = None
        placa = None
        if values['-TABLE_CLIENTE-']:
            cpf = dados_cliente[values['-TABLE_CLIENTE-'][0]][1]
        if values['-TABLE_VEICULO-']:
            placa = dados_veiculo[values['-TABLE_VEICULO-'][0]][1]
        self.close()

        return {'opcao': button, 'cpf': cpf, 'placa': placa}

    def seleciona_cliente(self):
        layout = [
            [sg.Text('CPF do cliente que deseja selecionar:')],
            [sg.Input(key='-CPF-')],
            [sg.Button('OK'), sg.Button('Cancelar')]
        ]
        self.__window = sg.Window('Selecionar Cliente', layout)
        button, values = self.open()
        cpf = values['-CPF-'] if button == 'OK' else None
        self.close()
        return cpf

    def pega_codigo_modelo(self):
        layout = [
            [sg.Text('CODIGO DE MODELO DO VEICULO:')],
            [sg.Input(key='-CODIGO_MODELO-')],
            [sg.Button('OK'), sg.Button('Cancelar')]
        ]
        self.__window = sg.Window('Código do Modelo', layout)
        button, values = self.open()
        codigo_modelo = values['-CODIGO_MODELO-'] if button == 'OK' else None
        self.close()
        return codigo_modelo

    def pega_dados_moto(self):
        layout = [
            [sg.Text('-------- DADOS MOTO ----------')],
            [sg.Text('Placa:'), sg.Input(key='-PLACA-')],
            [sg.Text('Kilometragem:'), sg.Input(key='-KILOMETRAGEM-')],
            [sg.Button('OK'), sg.Button('Cancelar')]
        ]
        self.__window = sg.Window('Dados da Moto', layout)
        button, values = self.open()
        dados_moto = {
            "placa": values['-PLACA-'],
            "kilometragem": values['-KILOMETRAGEM-']
        } if button == 'OK' else None
        self.close()
        return dados_moto

    def pega_dados_cliente(self, dados_cliente={'nome': '', 'cpf': '', 'email': '', 'telefone': ''}):
        sg.theme('DarkTeal4')
        layout = [
            [sg.Text('-------- DADOS CLIENTE ----------', font=("Helvetica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText(dados_cliente['nome'], key='nome')],
            [sg.Text('Telefone:', size=(15, 1)), sg.InputText(dados_cliente['telefone'], key='telefone')],
            [sg.Text('Email:', size=(15, 1)), sg.InputText(dados_cliente['email'], key='email')],
            [sg.Text('Cpf:', size=(15, 1)), sg.InputText(dados_cliente['cpf'], key='cpf')],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]
        self.__window = sg.Window('SisTroca de Oleo').Layout(layout)
        button, values = self.open()
        if button == 'Confirmar':
            dados_cliente = {
                "nome": values['nome'],
                "telefone": values['telefone'],
                "email": values['email'],
                "cpf": values['cpf']
            }
        self.close()
        return dados_cliente

    def mostrar_cliente(self, dados_cliente):
        sg.theme('DarkTeal4')
        header = ['Nome', 'Cpf', 'Telefone', 'Email', 'Veiculo']
        dados_cliente = self.formatar_dados_modelo(dados_cliente)
        layout = [
            [sg.Text('-------- LISTA DE CLIENTE ----------', font=("Helvetica", 25))],
            [sg.Table(values=dados_cliente,
                      headings=header,
                      display_row_numbers=True,
                      auto_size_columns=True,
                      num_rows=min(15, len(dados_cliente)),
                      key='-TABLE-',
                      row_height=25)],
            [sg.Button('Voltar', key=0)]
        ]
        self.__window = sg.Window('SisTroca de Oleo').Layout(layout)
        button, values = self.open()
        self.close()
        return button

    def mostra_veiculo(self, dados_veiculo):
        sg.theme('DarkTeal4')
        header = ['Modelo', 'Placa', 'KM']
        layout = [
            [sg.Text('-------- LISTA DE VEICULO ----------', font=("Helvetica", 25))],
            [sg.Table(values=dados_veiculo,
                      headings=header,
                      display_row_numbers=True,
                      auto_size_columns=True,
                      num_rows=min(15, len(dados_veiculo)),
                      key='-TABLE-',
                      row_height=25)],
            [sg.Button('Voltar', key=0)]
        ]
        self.__window = sg.Window('SisTroca de Oleo').Layout(layout)
        button, values = self.open()
        self.close()
        return button

    def seleciona_moto(self):
        layout = [
            [sg.Text('Placa da moto que deseja selecionar:')],
            [sg.Input(key='-PLACA-')],
            [sg.Button('OK'), sg.Button('Cancelar')]
        ]
        self.__window = sg.Window('Selecionar Moto', layout)
        button, values = self.open()
        placa_moto = values['-PLACA-'] if button == 'OK' else None
        self.close()
        return placa_moto

    def formatar_dados_modelo(self, dados_modelo):
        # Garante que os dados_modelo sejam uma lista de listas de strings
        if isinstance(dados_modelo, list) and all(isinstance(linha, list) for linha in dados_modelo):
            return [[str(item) for item in linha] for linha in dados_modelo]
        return []

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.close()

    def open(self):
        button, values = self.__window.read()
        return button, values
