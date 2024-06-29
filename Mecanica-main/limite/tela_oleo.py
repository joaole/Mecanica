import PySimpleGUI as sg

class TelaOleo:
    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def init_opcoes(self):
        pass

    def tela_opcoes(self, dados_oleo=[]):
        sg.ChangeLookAndFeel('DarkTeal4')
        # Cabeçalhos da tabela
        header = ['fornecedor', 'marcar', 'expessura', 'valor', 'codigo']
        layout = [
            [sg.Text('-------- LISTA DE OLEOS----------', font=("Helvetica", 25))],
            [sg.Table(values=dados_oleo,
                      headings=header,
                      display_row_numbers=True,
                      auto_size_columns=True,
                      num_rows=min(15, len(dados_oleo)),
                      key='-TABLE-',
                      row_height=25)],
            [
                sg.Button('Incluir Oleo', key=1), sg.Button('Alterar Oleo', key=2),
                sg.Button('Excluir Oleo', key=4)
            ],
            [sg.Button('Voltar', key=0)]
        ]
        self.__window = sg.Window('SisTroca de Oleo').Layout(layout)

        while True:
            button, values = self.open()

            if button in (None, 0):
                self.close()
                return {'opcao': button, 'codigo': None}

            if button == 1:
                self.close()
                return {'opcao': button, 'codigo': None}

            if button == 2:
                if values['-TABLE-']:
                    codigo = dados_oleo[values['-TABLE-'][0]][4]
                    self.close()
                    return {'opcao': button, 'codigo': codigo}

            if button == 4:
                if values['-TABLE-']:
                    codigo = dados_oleo[values['-TABLE-'][0]][4]
                    self.close()
                    return {'opcao': button, 'codigo': codigo}

    def seleciona_fornecedor(self, dados_fornecedor ):
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

    def seleciona_oleo(self):
        codigo = input("Codigo do oleo que deseja selecionar: ")
        return codigo

    def seleciona_expessura(self):
        expessura = input("Expessura do oleo que deseja selecionar: ")
        return expessura

    '''
    def mostrar_oleo(self, dados_oleo):
        sg.ChangeLookAndFeel('DarkTeal4')
        header = ['Fornecedor', 'Marca', 'Expessura', 'valor', 'Codigo']
        layout = [
            [sg.Text('-------- SELECIONAR OLEO ----------', font=("Helvetica", 25))],
            [sg.Table(values=dados_oleo,
                      headings=header,
                      display_row_numbers=True,
                      auto_size_columns=True,
                      num_rows=min(15, len(dados_oleo)),
                      key='-TABLE-',
                      row_height=25)],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]
        self.__window = sg.Window('SisTroca de Oleo').Layout(layout)

        button, values = self.open()
        codigo = None
        if values['-TABLE-']:
            cnpj = dados_oleo[values['-TABLE-'][0]][1]
        self.close()

        return codigo
    '''
    def pega_dados_oleo(self, dados_fornecedor={'marca': '', 'expessura': '', 'valor': ''}):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- DADOS FORNECEDOR ----------', font=("Helvica", 25))],
            [sg.Text('Marca:', size=(15, 1)), sg.InputText(dados_fornecedor['marca'], key='marca')],
            [sg.Text('Expessura:', size=(15, 1)), sg.InputText(dados_fornecedor['expessura'], key='expessura')],
            [sg.Text('Valor:', size=(15, 1)), sg.InputText(dados_fornecedor['valor'], key='valor')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('SisTroca de Oleo').Layout(layout)

        button, values = self.open()
        marca = values['marca']
        expessura = values['expessura']
        valor = values['valor']

        self.close()
        return {"marca": marca, "expessura": expessura, "valor": valor}

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
