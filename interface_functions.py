import PySimpleGUI as sg
from packages import *
from time import sleep

def open_window():
    layout = [[sg.Text("New Window", key="new")]]
    window = sg.Window("Second Window", layout, modal=True)
    choice = None
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
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


    window.close()
