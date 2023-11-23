import PySimpleGUI as sg
from time import sleep

global a


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
    global a
    try:
        a = open(arquivo, 'rt')
    except:
        print('Erro ao ler o arquivo!')


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
