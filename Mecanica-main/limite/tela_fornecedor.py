import PySimpleGUI as sg

class TelaFornecedor():
    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def tela_opcoes(self, dados_fornecedor=[]):
        sg.ChangeLookAndFeel('DarkTeal4')
        # Cabeçalhos da tabela
        header = ['Nome', 'Cnpj', 'Telefone', 'Email']
        layout = [
            [sg.Text('-------- LISTA DE FORNECEDORES ----------', font=("Helvetica", 25))],
            [sg.Table(values=dados_fornecedor,
                      headings=header,
                      display_row_numbers=True,
                      auto_size_columns=True,
                      num_rows=min(15, len(dados_fornecedor)),
                      key='-TABLE-',
                      row_height=25)],
            [
                sg.Button('Incluir Fornecedor', key=1), sg.Button('Alterar Fornecedor', key=2),
                sg.Button('Excluir Fornecedor', key=4)
            ],
            [sg.Button('Voltar', key=0)]
        ]
        self.__window = sg.Window('SisTroca de Oleo').Layout(layout)

        button, values = self.open()
        cnpj = None
        if values['-TABLE-']:
            cnpj = dados_fornecedor[values['-TABLE-'][0]][1]
            self.close()

        return {'opcao': button, 'cnpj': cnpj}

    def init_opcoes(self):
        pass

    def pega_dados_fornecedor(self, dados_fornecedor={'nome': '', 'telefone': '', 'email': '', 'cnpj': ''}):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- DADOS FORNECEDOR ----------', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText(dados_fornecedor['nome'], key='nome')],
            [sg.Text('Telefone:', size=(15, 1)), sg.InputText(dados_fornecedor['telefone'], key='telefone')],
            [sg.Text('Email', size=(15, 1)), sg.InputText(dados_fornecedor['email'], key='email')],
            [sg.Text('Cnpj:', size=(15, 1)), sg.InputText(dados_fornecedor['cnpj'], key='cnpj')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('SisTroca de Oleo').Layout(layout)

        button, values = self.open()
        nome = values['nome']
        telefone = values['telefone']
        email = values['email']
        cnpj = values['cnpj']

        self.close()
        return {"nome": nome, "telefone": telefone, "email": email, "cnpj": cnpj}

    def tela_opcoes(self, dados_fornecedor=[]):
        sg.ChangeLookAndFeel('DarkTeal4')
        header = ['Nome', 'Cnpj', 'Telefone', 'Email']
        layout = [
            [sg.Text('-------- LISTA DE FORNECEDORES ----------', font=("Helvetica", 25))],
            [sg.Table(values=dados_fornecedor,
                      headings=header,
                      display_row_numbers=True,
                      auto_size_columns=True,
                      num_rows=min(15, len(dados_fornecedor)),
                      key='-TABLE-',
                      row_height=25)],
            [
                sg.Button('Incluir Fornecedor', key=1), sg.Button('Alterar Fornecedor', key=2),
                sg.Button('Excluir Fornecedor', key=4)
            ],
            [sg.Button('Voltar', key=0)]
        ]
        self.__window = sg.Window('SisTroca de Oleo').Layout(layout)

        while True:
            button, values = self.open()

            if button in (None, 0):
                self.close()
                return {'opcao': button, 'cnpj': None}

            if button == 1:
                self.close()
                return {'opcao': button, 'cnpj': None}

            if button == 2:
                if values['-TABLE-']:
                    cnpj = dados_fornecedor[values['-TABLE-'][0]][1]
                    self.close()
                    return {'opcao': button, 'cnpj': cnpj}

            if button == 4:
                if values['-TABLE-']:
                    cnpj = dados_fornecedor[values['-TABLE-'][0]][1]
                    self.close()
                    return {'opcao': button, 'cnpj': cnpj}

    def seleciona_fornecedor(self, dados_fornecedor):
        sg.ChangeLookAndFeel('DarkTeal4')
        header = ['Nome', 'Cnpj', 'Telefone', 'Email']
        layout = [
            [sg.Text('-------- SELECIONAR FORNECEDOR ----------', font=("Helvetica", 25))],
            [sg.Table(values=dados_fornecedor,
                      headings=header,
                      display_row_numbers=True,
                      auto_size_columns=True,
                      num_rows=min(15, len(dados_fornecedor)),
                      key='-TABLE-',
                      row_height=25)],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]
        self.__window = sg.Window('SisTroca de Oleo').Layout(layout)

        button, values = self.open()
        cnpj = None
        if values['-TABLE-']:
            cnpj = dados_fornecedor[values['-TABLE-'][0]][1]
        self.close()

        return cnpj

    def mostrar_fornecedor(self, dados_fornecedor):
        sg.ChangeLookAndFeel('DarkTeal4')
        header = ['Nome', 'Cnpj', 'Telefone', 'Email']
        layout = [
            [sg.Text('-------- SELECIONAR FORNECEDOR ----------', font=("Helvetica", 25))],
            [sg.Table(values=dados_fornecedor,
                      headings=header,
                      display_row_numbers=True,
                      auto_size_columns=True,
                      num_rows=min(15, len(dados_fornecedor)),
                      key='-TABLE-',
                      row_height=25)],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]
        self.__window = sg.Window('SisTroca de Oleo').Layout(layout)

        button, values = self.open()
        cnpj = None
        if values['-TABLE-']:
            cnpj = dados_fornecedor[values['-TABLE-'][0]][1]
        self.close()

        return cnpj

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
