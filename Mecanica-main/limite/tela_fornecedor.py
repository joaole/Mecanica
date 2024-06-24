import PySimpleGUI as sg

class TelaFornecedor():
  def __init__(self):
    self.__window = None
    self.init_opcoes()

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def tela_opcoes(self):
    self.init_opcoes()
    button, values = self.open()
    if values['1']:
      opcao = 1
    if values['2']:
      opcao = 2
    # cobre os casos de Retornar, fechar janela, ou clicar cancelar
    #Isso faz com que retornemos a tela do sistema caso qualquer uma dessas coisas aconteca
    if values['0'] or button in (None, 'Cancelar'):
      opcao = 0
    self.close()
    return opcao

  def init_opcoes(self):
    #sg.theme_previewer()
    sg.ChangeLookAndFeel('DarkTeal4')
    layout = [
      [sg.Text('-------- FORNECEDORES ----------', font=("Helvica", 25))],
      [sg.Text('Escolha sua opção', font=("Helvica", 15))],
      [sg.Radio('Incluir Fornecedor', "RD1", key='1')],
      [sg.Radio('Listar Fornecedores', "RD1", key='2')],
      [sg.Radio('Retornar', "RD1", key='0')],
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    ]
    self.__window = sg.Window('SisTroca de Oleo').Layout(layout)

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  # opção de tratamento: adicionar um if e só coletar nome e telefone se o button é 'Confirmar'
  def pega_dados_fornecedor(self):
    sg.ChangeLookAndFeel('DarkTeal4')
    layout = [
      [sg.Text('-------- DADOS FORNECEDOR ----------', font=("Helvica", 25))],
      [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
      [sg.Text('Telefone:', size=(15, 1)), sg.InputText('', key='telefone')],
      [sg.Text('CNPJ:', size=(15, 1)), sg.InputText('', key='cnpj')],
      [sg.Text('EMAIL:', size=(15, 1)), sg.InputText('', key='email')],
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    ]
    self.__window = sg.Window('FORNECEDOR').Layout(layout)

    button, values = self.open()
    nome = values['nome']
    telefone = values['telefone']
    cnpj = values['cnpj']
    email = values['email']

    self.close()
    return {"nome": nome, "telefone": telefone, "cnpj": cnpj, 'email': email}

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def mostra_fornecedor(self, dados_fornecedor):
    layout = [
              [sg.Table(values= dados_fornecedor, headings=['nome', 'cnpj'], max_col_width=25, background_color='DarkTeal4',
                        auto_size_columns=True,
                        display_row_numbers=True,
                        justification='right',
                        num_rows=20,
                        alternating_row_color='lightyellow',
                        key='-TABLE-',
                        tooltip='This is a table')],

              [sg.Button('Incluir', key=1), sg.Button('Alterar', key=2)], sg.Button('Excluir', key=3), sg.Button('Voltar', key=0),
    ]

    self.__window = sg.Window('Lista de Fornecedores', layout)

    button, values = self.open()

    self.close()
    return button, values

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def seleciona_fornecedor(self):
    sg.ChangeLookAndFeel('DarkTeal4')
    layout = [
      [sg.Text('-------- SELECIONAR FORNECEDOR ----------', font=("Helvica", 25))],
      [sg.Text('Digite o CNPJ do fornecedor que deseja selecionar:', font=("Helvica", 15))],
      [sg.Text('CNPJ:', size=(15, 1)), sg.InputText('', key='cnpj')],
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    ]
    self.__window = sg.Window('Seleciona Fornecedor').Layout(layout)

    button, values = self.open()
    cnpj = values['cnpj']
    self.close()
    return cnpj

  def mostra_mensagem(self, msg):
    sg.popup("", msg)

  def close(self):
    self.__window.Close()

  def open(self):
    button, values = self.__window.Read()
    return button, values
