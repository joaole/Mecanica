import PySimpleGUI as sg

class TelaModelo:
    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def init_opcoes(self):
        pass

    def tela_opcoes(self, dados_modelo=[]):
        sg.ChangeLookAndFeel('DarkTeal4')
        # Ensure the header matches the data structure
        header = ['nome', 'expessura', 'quantidade_oleo', 'codigo']
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
                    codigo = dados_modelo[values['-TABLE-'][0]][3]
                    self.close()
                    return {'opcao': button, 'codigo': codigo}

            if button == 4:
                if values['-TABLE-']:
                    codigo = dados_modelo[values['-TABLE-'][0]][3]
                    self.close()
                    return {'opcao': button, 'codigo': codigo}

    def pega_dados_modelo(self, dados_modelo={'nome': '', 'quantidade_oleo': '', 'expessura': ''}):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- DADOS MODELO ----------', font=("Helvetica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText(dados_modelo['nome'], key='nome')],
            [sg.Text('Quantidade de Oleo:', size=(15, 1)), sg.InputText(dados_modelo['quantidade_oleo'], key='quantidade_oleo')],
            [sg.Text('Expessura:', size=(15, 1)), sg.InputText(dados_modelo['expessura'], key='expessura')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('SisTroca de Oleo').Layout(layout)

        button, values = self.open()
        nome = values['nome']
        quantidade_oleo = values['quantidade_oleo']
        expessura = values['expessura']

        self.close()
        return {"nome": nome, "Quantidade de oleo": quantidade_oleo, "expessura": expessura}

    def mostrar_modelo(self, dados_modelo):
        sg.ChangeLookAndFeel('DarkTeal4')
        header = ['Nome', 'Quantidade Oleo', 'Expessura', 'Codigo']
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
        self.__window = sg.Window('SisTroca de Oleo').Layout(layout)

        button, values = self.open()
        codigo = None
        if values['-TABLE-']:
            codigo = dados_modelo[values['-TABLE-'][0]][3]
        self.close()

        return codigo

    def mostra_oleo_modelo(self, dados_oleo):
        print("CNPJ DO FORNECEDOR: ", dados_oleo["fornecedor"])
        print("MARCA OLEO: ", dados_oleo["marca"])
        print("CODIGO DO OLEO: ", dados_oleo["codigo"])
        print("VALOR DO OLEO: ", dados_oleo["valor"])
        print("\n")

    def seleciona_modelo(self):
        codigo = input("CODIGO do modelo que deseja selecionar: ")
        return codigo

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
