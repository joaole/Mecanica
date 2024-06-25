import PySimpleGUI as sg

class TelaFornecedor():
  def __init__(self):
    self.__window = None
    self.init_opcoes()


  def tela_opcoes(self, dados_fornecedor = []):
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
      [sg.Button('Voltar')]
    ]
    self.__window = sg.Window('SisTroca de Oleo').Layout(layout)

    button, values = self.open()
    cnpj = None
    if values['-TABLE-']:
      cnpj = dados_fornecedor[values['-TABLE-'][0]][1]
      self.close()

    return {'opcao': button, 'cnpj': cnpj}

  def init_opcoes(self):
    #sg.theme_previewer()
    sg.ChangeLookAndFeel('DarkTeal4')
    layout = [
      [sg.Text('-------- Fornecedor ----------', font=("Helvica", 25))],
      [sg.Text('Escolha sua opção', font=("Helvica", 15))],
      [sg.Radio('Incluir Fornecedor', "RD1", key='1')],
      [sg.Radio('Listar Fornecedores', "RD1", key='3')],
      [sg.Radio('Retornar', "RD1", key='0')],
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    ]
    self.__window = sg.Window('SisTrica de Oleo').Layout(layout)

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  # opção de tratamento: adicionar um if e só coletar nome e telefone se o button é 'Confirmar'
  def pega_dados_fornecedor(self, dados_fornecedor = {'nome': ''}):
    sg.ChangeLookAndFeel('DarkTeal4')
    layout = [
      [sg.Text('-------- DADOS FORNECEDOR ----------', font=("Helvica", 25))],
      [sg.Text('Nome:', size=(15, 1)), sg.InputText(dados_fornecedor['nome'], key='nome')],
      [sg.Text('Telefone:', size=(15, 1)), sg.InputText('', key='telefone')],
      [sg.Text('Email', size=(15, 1)), sg.InputText('', key='email')],
      [sg.Text('Cnpj:', size=(15, 1)), sg.InputText('', key='cnpj')],
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    ]
    self.__window = sg.Window('SisTroca de Oleo').Layout(layout)

    button, values = self.open()
    nome = values['nome']
    telefone = values['telefone']
    email = values['email']
    cnpj= values['cnpj']

    self.close()
    return {"nome": nome, "telefone": telefone, "email": email, "cnpj": cnpj}

  def mostra_fornecedor(self, dados_fornecedor):
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
        sg.Button('Incluir Fornecedor', key=1), sg.Button('Alterar Fornecedor', key=2), sg.Button('Excluir Fornecedor', key=4)
      ],
      [sg.Button('Voltar')]
    ]
    self.__window = sg.Window('SisTroca de Oleo').Layout(layout)

    button, values = self.open()
    if values['-TABLE-']:
      cnpj = dados_fornecedor[values['-TABLE-'][0]][1]
      self.close()

    return {'opcao': button, 'cnpj': cnpj}

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def seleciona_fornecedor(self):
    pass
  def mostra_mensagem(self, msg):
    sg.popup("", msg)

  def close(self):
    self.__window.Close()

  def open(self):
    button, values = self.__window.Read()
    return button, values
