import PySimpleGUI as sg
from packages import *
from time import sleep


def ver_cadastros():
    layout_pre = dict()
    from cadastrar import arquivo_cadastros

    try:
        a = open(arquivo_cadastros, 'rt')
    except:
        print('Erro ao ler o arquivo!')

    layout = [
        [sg.Text("LISTA DE CADASTROS: ", key="new")],
    ]

    c = 0
    for linha in a:
        dado = linha.split(';')
        dado[1] = dado[1].replace('\n', '')
        new_register = [sg.Text(f'Nome: {dado[0]} | E-mail: {dado[1]}')]
        layout.append(new_register)
        print(f'Nome: {dado[0]:5} | Email: {dado[1]}')
        c += 1

    layout.append([sg.Button('Sair')])
    window = sg.Window("Visualizar cadastros", layout, modal=True)
    choice = None
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Sair':
            break

    window.close()


def main():
    layout_cadastrar = [
        [sg.Text('Cadastre na nossa newsletter em Python')],
        [sg.InputText(key='name')],
        [sg.InputText(key='email')],
        [sg.Button('Cadastrar')],
        [sg.Text(key='cadastro_status')],
        [sg.Button('Ver cadastros'), sg.Button('Sair do sistema')],
    ]
    window = sg.Window('Newsletter com Python', layout_cadastrar)

    while True:
        cadastros_list = list()
        cadastros_dict = dict()

        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Sair do sistema':
            break

        if event == 'Cadastrar':
            from cadastrar import arquivo_cadastros
            new_name = values['name']
            new_email = values['email']
            cadastros_dict['name'] = new_name
            cadastros_dict['email'] = new_email
            cadastros_list.append(cadastros_dict.copy())
            window['cadastro_status'].update('Cadastrado com sucesso!')
            cadastrar(arquivo_cadastros, new_name, new_email)
            print(cadastros_list)
            sleep(0.5)
            window['name'].update('')
            window['email'].update('')
            window['cadastro_status'].update('')

        if event == 'Ver cadastros':
            ver_cadastros()


    window.close()
