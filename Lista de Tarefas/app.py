import PySimpleGUI as sg


# Função para criar a janela inicial
def criar_janela_inicial():
    sg.theme('DarkBlue4')

    # Layout da linha de tarefa
    linha_tarefa = [
        [sg.Checkbox(''), sg.Input('')]
    ]

    # Layout da janela principal
    layout = [
        [sg.Frame('Tarefas', layout=linha_tarefa, key='container')],
        [sg.Button('Nova Tarefa'), sg.Button('Resetar')]
    ]

    return sg.Window('To-do List', layout=layout, finalize=True)


# Função para limpar as tarefas atuais
def limpar_tarefas():
    global tarefas_atuais
    tarefas_atuais = []


# Janela
janela = criar_janela_inicial()
tarefas_atuais = []  # Armazena as tarefas atuais

# Regras
while True:
    event, values = janela.read()

    # Fechar a janela
    if event == sg.WIN_CLOSED:
        break

    # Adicionar nova tarefa
    if event == 'Nova Tarefa':
        janela.extend_layout(janela['container'], [[sg.Checkbox(''), sg.Input('')]])

    # Resetar
    elif event == 'Resetar':
        limpar_tarefas()
        janela['container'].update()

