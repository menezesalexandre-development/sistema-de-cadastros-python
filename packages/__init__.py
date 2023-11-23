import PySimpleGUI as sg
from time import sleep


def arquivo_existe(arquivo):
    try:
        a = open(arquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(arquivo):
    try:
        a = open(arquivo, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print('Arquivo criado com sucesso!')


layout_ver_cadastros = list()


def ler_arquivo(arquivo):
    try:
        a = open(arquivo, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        global layout_ver_cadastros

        layout_ver_cadastros = [
            [sg.Text('PESSOAS CADASTRADAS:')],
        ]
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            new_register = {'name': dado[1], 'email': dado[1]}
            layout_ver_cadastros.append(new_register.copy())
            print(f'Nome: {dado[0]:5} | Email: {dado[1]}')
    finally:
        a.close()


def cadastrar(arquivo, nome='Desconhecido', email='Desconhecido'):
    try:
        a = open(arquivo, 'at')
    except:
        print(f'Houve um ERRO na hora de cadastrar')
    else:
        try:
            a.write(f'{nome}; {email}\n')
        except:
            print(f'Houve um erro no cadastro')
        else:
            print(f'Novo registro de {nome} adicionado')
            a.close()
