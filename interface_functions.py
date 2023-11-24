import PySimpleGUI as sg
from packages import *
from time import sleep

emails_list = list()
layout = list()

def ver_cadastros():
    from cadastrar import arquivo_cadastros
    global layout

    try:
        a = open(arquivo_cadastros, 'rt')
    except:
        print('Erro ao ler o arquivo!')

    layout = [
        [sg.Text("LISTA DE CADASTROS: ", key="new")],
    ]

    for linha in a:
        try:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            dado[2] = dado[2].replace('\n', '')
            if dado[1] != ' ':
                new_register = [sg.Text(f'Nome: {dado[0]} | E-mail: {dado[1]} | Nascimento: {dado[2]}')]
                print(f'Nome: {dado[0]:5} | Email: {dado[1]:5} | Nascimento: {dado[2]}')
                layout.append(new_register)
                emails_list.append(dado[1])
            else:
                print(f'Não foi possível mostrar o registro da linha {linha}')
        except IndexError:
            print(f'Não foi possível mostrar um registro da linha {linha}')

    layout.append([sg.Button('Sair')])
    window = sg.Window("Visualizar cadastros", layout, modal=True)
    choice = None
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Sair':
            break

    window.close()


def main():
    try:
        layout_cadastrar = [
            [sg.Text('Cadastre em nosso sistema feito em Python')],
            [sg.Text('Nome:')],
            [sg.InputText(key='name')],
            [sg.Text('E-mail:')],
            [sg.InputText(key='email')],
            [sg.Text('Data de Nascimento (YYYY-MM-DD):')],
            [sg.InputText(key='data_nasc')],
            [sg.Button('Cadastrar')],
            [sg.Text(key='cadastro_status')],
            [sg.Button('Ver cadastros'), sg.Button('Sair do sistema')],
        ]
        window = sg.Window('Sistema de cadastros', layout_cadastrar)

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
                new_data_nasc = values['data_nasc']
                cadastros_dict['name'] = new_name
                cadastros_dict['email'] = new_email
                cadastros_dict['data_nasc'] = new_data_nasc
                cadastros_list.append(cadastros_dict.copy())
                window['cadastro_status'].update('Cadastrado com sucesso!')
                cadastrar(arquivo_cadastros, new_name, new_email, new_data_nasc)
                print(cadastros_list)
                sleep(0.5)
                window['name'].update('')
                window['email'].update('')
                window['data_nasc'].update('')
                window['cadastro_status'].update('')

            if event == 'Ver cadastros':
                ver_cadastros()
    except KeyboardInterrupt:
        print('Programa interrompido por ação externa.')


    window.close()
