# Suponha que você tenha um arquivo chamado "notas.txt" com o seguinte formato:
# Maria;8.5;4.5
# Pedro;7.0;7.5
# Ana;9.3;9.6

# Escreva um programa que:
# - Leia o arquivo
# - Calcule e exiba a média das notas
# - Mostre qual aluno teve a maior e a menor nota
from arquivo import * 

# Passo-a-Passo
arq = 'notas.txt'

#1. Verificar se o arquivo existe
if not file_exists(arq):
    print('Arquivo Não Encontrado')
    exit()

#2. Ler o Arquivo
content = read_file(arq)


#3. Calcular a media

#   Inicializando com o primeiro aluno
first_line = content[0].strip().split(';')
largest_avg = smallest_avg = average(float(first_line[1]), float(first_line[2]))
student_major = [first_line[0]]
student_minor = [first_line[0]]

for line in content[1:]:
    sharing = line.strip().split(';')
    name = sharing[0]
    media = average(float(sharing[1]), float(sharing[2]))

#4. Verificar qual aluno teve a maior e a menor nota
    if media > largest_avg:
        largest_avg = media
        student_major = [name]

    elif media == largest_avg:
        student_major.append(name)


    if media < smallest_avg:
        smallest_avg =  media
        student_minor = [name]
    elif media == smallest_avg:
        student_minor.append(name)

print(f'O aluno com maior nota: {", ".join(student_major)}, {largest_avg}')
print(f'O aluno com menor nota: {", ".join(student_minor)}, {smallest_avg}')


#4. Cria um novo arquivo com os alunos e sua respectiva media
save_averages(content)

