def file_exists(filename):
    "Verifica se o arquivo existe e retorna 'True' or 'False'"
    try:
        with open(f'{filename}', 'r') as file:
            file.read()
    except FileNotFoundError:
        return False
    else:
        return True


def create_file(filename):
    "Cria um arquivo se não ouver um arquivo criado com determinado nome"
    try:
        with open(f'{filename}', 'w') as file:
            file.write('')
    except Exception as erro:
        print(f'\033[;31m ERRO! {erro}\033[m \nFalha ao criar o arquivo: {filename}')
    else:
        print(f'Arquivo {filename} criado com Sucesso!')


def read_file(filename):
    "Lê o arquivo chamado"
    try:
        with open(f'{filename}', 'r', encoding='utf-8') as file:
            content = file.readlines()
        return content
    except FileNotFoundError:
        print(f'Problema na leitura do Arquivo: {filename}')
    except Exception as erro:
        print(f'\033[;31m ERRO! {erro}\033[m \nAo Tentar ler o arquivo: {filename}')


def save_averages(content, filename='medias.txt'):
    "Salva as medias dos alunos em uma arquivo."
    try: 
        with open(filename, 'w', encoding='utf-8') as file:
            for line in  content:
                sharing = line.strip().split(';')
                name = sharing[0]
                media = average(float(sharing[1]), float(sharing[2]))
                file.write(f'{name};{media:.2f}\n')
        print(f"Arquivo '{filename}' criado com sucesso!")
    except Exception as erro:
        print(f'\033[;31m ERRO! {erro}\033[m \nAo salvar as medias no arquivo: {filename}')


def average(grade1=0, grade2=0):
    "Calcula a media"
    return (grade1 + grade2) / 2
   