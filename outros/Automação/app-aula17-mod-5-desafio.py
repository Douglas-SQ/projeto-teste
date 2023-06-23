import os

frutas =['abacaxi','acerola','manga','goiaba','maçã']
cores=['azul','amarelo','vermelho','preto','verde']
linguagens=['c','c++','c#','python','f#']
# Desafio 1 - Crie um novo arquivo chamado frutas.txt 
# e insira dentro dele todos as 5 frutas que estão na lista de frutas
with open ('frutas.txt','w',newline='', encoding='utf-8') as arquivo:
    for fruta in frutas:
        arquivo.write(fruta + os.linesep)
    

# Desafio 2 - Imprima na tela todas as linhas que estao dentro do arquivo frutas.txt
with open ('frutas.txt','r') as arquivo:
    for linha in arquivo:
        print(linha)

# Desafio 3 - Sem apagar os dados que já estão dentro de frutas.txt, 
# adicione todas as cores que estão dentro da sua lista de cores ao arquivos frutas.txt

with open ('frutas.txt','r+',newline='',encoding='utf-8') as arquivo:
    for linha in arquivo:
        print(linha)
    for cor in cores:
        arquivo.write(cor + os.linesep)

# Desafio 4 - Crie um novo arquivo chamado 'Top 5 Linguagens.txt' 
# e popule o arquivo, de forma com que cada linuguagem ocupe apenas uma linha.

with open ('Top 5 Linguagens.txt','w',newline='',encoding='utf-8') as arquivo:
    for linguagem in linguagens:
        arquivo.write(linguagem+os.linesep)

# BONUS - Como você poderia criar vários arquivos diferentes usando um laço for 
# e strings dinâmicos(f'{}'), e também não escrever nada dentro deles?

nome_arquivos=['arq1','arq2','arq3']

for nome in nome_arquivos:
    with open(f'{nome}.txt','w')as arquivo:
        print(f'{nome}.txt')
                                                                                                               

# BONUS - Como você poderia criar vários arquivos diferentes usando um laço for
# solução professor com desafio um pouco diferente utilizando formatos diferentes de arquivo

arquivos=['musicas.mp3','foto.jpg','senhas.txt','relatorio.pdf']
for arquivo in arquivos:
    with open(arquivo,'w') as arquivo:
        pass
    


