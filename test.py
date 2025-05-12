arq = 'Arquivos/Analise de Notas/notas.txt'

def criar(nome):
    try:
        with open(f'{nome}', 'w') as arquivo:
            arquivo.write('')
    except Exception as erro:
        print(f'\033[;31m ERRO! {erro}\033[m \nFalha ao criar o arquivo: {nome}')
    else:
        print(f'Arquivo {nome} criado com Sucesso!')

criar(arq)