import random
from os import system
def criar_opcoes():
    opcoes=[]
    while True:
        opcao=input('digite uma opçao a ser adicionada ou exit para sair:\n')
        if opcao.lower()=="exit":
            break
        opcoes.append(opcao)
    return opcoes

while True:
    try:
        opcoes=criar_opcoes()
        print("resultado:")
        print(opcoes[random.randrange(len(opcoes))])
    except:
        print('adicone pelo menos um valor')
    input()
    system('cls')
    
