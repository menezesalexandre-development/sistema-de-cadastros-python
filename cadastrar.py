from packages import *
from interface_functions import *

arquivo_cadastros = 'cadastros.txt'
if not arquivo_existe(arquivo_cadastros):
    print('Arquivo não encontrado!')
    criar_arquivo(arquivo_cadastros)

if __name__ == '__main__':
    main()

