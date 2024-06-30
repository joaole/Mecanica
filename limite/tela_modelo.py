import PySimpleGUI as sg

class TelaModelo:
    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def init_opcoes(self):
        pass

    def formatar_dados_modelo(self, dados_modelo):
        # Garante que os dados_modelo sejam uma lista de listas de strings
        if isinstance(dados_modelo, list) and all(isinstance(linha, list) for linha in dados_modelo):
            return [[str(item) for item in linha] for linha in dados_modelo]
        return []

    def tela_opcoes(self, dados_modelo=[]):
        sg.ChangeLookAndFeel('DarkTeal4')
        header = ['Nome', 'Expessura', 'Quantidade de Oleo', 'Codigo']
        dados_modelo = self.formatar_dados_modelo(dados_modelo)
        layout = [
            [sg.Text('-------- LISTA DE MODELOS ----------', font=("Helvetica", 25))],
            [sg.Table(values=dados_modelo,
                      headings=header,
                      display_row_numbers=True,
                      auto_size_columns=True,
                      num_rows=min(15, len(dados_modelo)),
                      key='-TABLE-',
                      row_height=25)],
            [
                sg.Button('Incluir Modelo', key=1), sg.Button('Alterar Modelo', key=2),
                sg.Button('Excluir Modelo', key=4)
            ],
            [sg.Button('Voltar', key=0)]
        ]
        self.__window = sg.Window('SisTroca de Oleo', layout)

        while True:
            button, values = self.open()

            if button in (None, 0):
                self.close()
                return {'opcao': button, 'codigo': None}

            if button == 1:
                self.close()
                return {'opcao': button, 'codigo': None}

            if button == 2 or button == 4:
                if values['-TABLE-']:
                    codigo = dados_modelo[values['-TABLE-'][0]][3]
                    self.close()
                    return {'opcao': button, 'codigo': int(codigo)}

    def pega_dados_modelo(self, dados_modelo={'nome': '', 'quantidade_oleo': '', 'expessura': ''}):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- DADOS MODELO ----------', font=("Helvetica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText(dados_modelo['nome'], key='nome')],
            [sg.Text('Quantidade de Oleo:', size=(15, 1)), sg.InputText(dados_modelo['quantidade_oleo'], key='quantidade_oleo')],
            [sg.Text('Expessura:', size=(15, 1)), sg.InputText(dados_modelo['expessura'], key='expessura')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('SisTroca de Oleo', layout)

        button, values = self.open()
        nome = values['nome']
        quantidade_oleo = values['quantidade_oleo']
        expessura = values['expessura']

        self.close()
        return {"nome": nome, "Quantidade de oleo": quantidade_oleo, "expessura": expessura}

    def mostrar_modelo(self, dados_modelo):
        sg.ChangeLookAndFeel('DarkTeal4')
        header = ['Nome', 'Quantidade Oleo', 'Expessura', 'Codigo']
        dados_modelo = self.formatar_dados_modelo(dados_modelo)
        layout = [
            [sg.Text('-------- SELECIONAR MODELO ----------', font=("Helvetica", 25))],
            [sg.Table(values=dados_modelo,
                      headings=header,
                      display_row_numbers=True,
                      auto_size_columns=True,
                      num_rows=min(15, len(dados_modelo)),
                      key='-TABLE-',
                      row_height=25)],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]
        self.__window = sg.Window('SisTroca de Oleo', layout)

        button, values = self.open()
        codigo = None
        if values['-TABLE-']:
            codigo = dados_modelo[values['-TABLE-'][0]][3]
        self.close()

        return int(codigo) if codigo is not None else None

    def seleciona_modelo(self, dados_modelo):
        sg.ChangeLookAndFeel('DarkTeal4')
        header = ['Nome', 'Quantidade Oleo', 'Expessura', 'Codigo']
        dados_modelo = self.formatar_dados_modelo(dados_modelo)
        layout = [
            [sg.Text('-------- SELECIONAR MODELO ----------', font=("Helvetica", 25))],
            [sg.Table(values=dados_modelo,
                      headings=header,
                      display_row_numbers=True,
                      auto_size_columns=True,
                      num_rows=min(15, len(dados_modelo)),
                      key='-TABLE-',
                      row_height=25)],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]
        self.__window = sg.Window('SisTroca de Oleo', layout)

        button, values = self.open()
        codigo = None
        if values['-TABLE-']:
            codigo = dados_modelo[values['-TABLE-'][0]][3]
        self.close()

        return int(codigo) if codigo is not None else None

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
