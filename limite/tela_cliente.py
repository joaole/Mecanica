import PySimpleGUI as sg

class TelaCliente:
    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def init_opcoes(self):
        pass

    def tela_opcoes(self, dados_cliente=[], dados_veiculo=[]):
        sg.ChangeLookAndFeel('DarkTeal4')
        # Cabeçalhos da tabela
        header = ['Nome', 'Cpf', 'Telefone', 'Email']
        cabecalho = ['Modelo', 'Placa', 'KM']
        layout = [
            [sg.Text('-------- LISTA DE CLIENTE ----------', font=("Helvetica", 25))],
            [sg.Table(values=dados_cliente,
                      headings=header,
                      display_row_numbers=True,
                      auto_size_columns=True,
                      num_rows=min(15, len(dados_cliente)),
                      key='-TABLE-',
                      row_height=25)],
            [
                sg.Button('Incluir Cliente', key=1), sg.Button('Alterar Cliente', key=2),
                sg.Button('Excluir Cliente', key=4),
            ],

            [sg.Text('-------- LISTA DE VEICULO ----------', font=("Helvetica", 25))],
            [sg.Table(values=dados_veiculo,
                      headings=cabecalho,
                      display_row_numbers=True,
                      auto_size_columns=True,
                      num_rows=min(15, len(dados_veiculo)),
                      key='-TABLE-',
                      row_height=25)],
            [sg.Button('Incluir Veiculo', key=5),
             sg.Button('Alterar Veiculo', key=6), sg.Button('Excluir Veiculo', key=7)],  # This line was missing a comma
            [sg.Button('Voltar', key=0)]
        ]
        self.__window = sg.Window('SisTroca de Oleo').Layout(layout)

        button, values = self.open()
        cpf = None
        placa = None
        if values['-TABLE-']:
            cpf = dados_cliente[values['-TABLE-'][0]][1]
            placa = dados_cliente[values['-TABLE-'][0][5]]
            self.close()

        return {'opcao': button, 'cpf': cpf, 'placa': placa}

    def seleciona_cliente(self):
        cpf = input("CPF do cliente que deseja selecionar: ")
        return cpf

    def pega_codigo_modelo(self):
        codigo_modelo = input("CODIGO DE MODELO DO VEICULO: ")
        return codigo_modelo

    def pega_dados_moto(self):
        print("-------- DADOS MOTO ----------")
        placa_moto = input("Placa: ")
        km_moto = input("Kilometragem: ")

        return {"placa": placa_moto, "kilometragem": km_moto}

    def pega_dados_cliente(self, dados_cliente={'nome': '', 'cpf': '', 'email': '', 'telefone': ''}):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- DADOS CLIENTE ----------', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText(dados_cliente['nome'], key='nome')],
            [sg.Text('Telefone:', size=(15, 1)), sg.InputText(dados_cliente['telefone'], key='telefone')],
            [sg.Text('Email', size=(15, 1)), sg.InputText(dados_cliente['email'], key='email')],
            [sg.Text('Cpf:', size=(15, 1)), sg.InputText(dados_cliente['cpf'], key='cpf')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('SisTroca de Oleo').Layout(layout)

        button, values = self.open()
        nome = values['nome']
        telefone = values['telefone']
        email = values['email']
        cpf = values['cpf']

        self.close()
        return {"nome": nome, "telefone": telefone, "email": email, "cpf": cpf}

    def mostrar_cliente(self, dados_cliente):
        sg.ChangeLookAndFeel('DarkTeal4')
        # Cabeçalhos da tabela
        header = ['Nome', 'Cpf', 'Telefone', 'Email']
        layout = [
            [sg.Text('-------- LISTA DE CLIENTE ----------', font=("Helvetica", 25))],
            [sg.Table(values=dados_cliente,
                      headings=header,
                      display_row_numbers=True,
                      auto_size_columns=True,
                      num_rows=min(15, len(dados_cliente)),
                      key='-TABLE-',
                      row_height=25)],
            [
                sg.Button('Incluir Cliente', key=1), sg.Button('Alterar Cliente', key=2),
                sg.Button('Excluir Cliente', key=4), sg.Button('Incluir Veiculo', key=5),
                sg.Button('Alterar Veiculo', key=6), sg.Button('Excluir Veiculo', key=7)
            ],
            [sg.Button('Voltar', key=0)]
        ]
        self.__window = sg.Window('SisTroca de Oleo').Layout(layout)

        button, values = self.open()
        cpf = None
        placa = None
        if values['-TABLE-']:
            cpf = dados_cliente[values['-TABLE-'][0]][1]
            placa = dados_cliente[values['-TABLE-'][0][5]]
            self.close()

        return {'opcao': button, 'cpf': cpf, 'placa': placa}

    def mostra_veiculo(self, dados_veiculo):
        print("MODELO DO VEICULO: ", dados_veiculo["modelo"])
        print("KILOMETRAGEM: ", dados_veiculo["kilometragem"])
        print("PLACA: ", dados_veiculo["placa"])
        print("\n")

    def seleciona_moto(self):
        placa_moto = input("Placa da moto que deseja selecionar: ")
        return placa_moto

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
