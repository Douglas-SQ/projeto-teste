"""
Criar aqu
"""

import os

with open ("celulares.txt", "w") as arquivo:
           arquivo.write("celular 1")

#with open("nomes.txt","a",newline='') as arquivo:
 #       arquivo.write('amanda'+ os.linesep)

""" nomes=['lucas','carol','jeff','douglas']
with open('nomes.txt','a',newline='') as arquivo:
        for nome in nomes:
                arquivo.write(nome + os.linesep)


numeros=[1,2,3,4,5,6]
with open('numeros.txt','a',newline='') as arquivo:
        for numero in numeros:
                arquivo.write(str(numero)+os.linesep)
 """
""" with open('nomes.txt','r')as arquivo:
        for linha in arquivo:
                print(linha) """

with open ('numeros.txt','r+') as arquivo:
        for linha in arquivo:
            print(linha)
        arquivo.write('9000')

