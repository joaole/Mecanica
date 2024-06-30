import PySimpleGUI as sg

class TelaSistema:
    def __init__(self):
        self.__window = None
        self.init_components()

    def tela_opcoes(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        self.init_components()
        button, values = self.__window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['4']:
            opcao = 4
        if values['5']:
            opcao = 5

        # cobre os casos de voltar, não clicar em nada e fechar janela, ou clicar cancelar
        if button in (None, 'Cancelar', 'Finalizassss Sistema'):
            opcao = 0
        self.close()
        return opcao

    def close(self):
        self.__window.Close()

    def init_components(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Bem vindo ao SisTroca de Oleo!', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Fornecedor', "RD1", key='1')],
            [sg.Radio('Oleos', "RD1", key='2')],
            [sg.Radio('Modelos', "RD1", key='3')],
            [sg.Radio('Clientes', "RD1", key='4')],
            [sg.Radio('Troca de Oleo', "RD1", key='5')],
            [sg.Button('Confirmar'), sg.Cancel('Finalizassss Sistema')]
        ]
        self.__window = sg.Window('SisTroca de Oleo').Layout(layout)
