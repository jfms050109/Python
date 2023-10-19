alunos=["felipe",'joão','vitor','yago']
notas=[[10,10],[9,9],[10,10],[5,3]]

if len(alunos)==len(notas):
    for aluno in range(len(alunos)):
        soma=0
        for nota in notas[aluno]:
            soma+=nota
        print(alunos[aluno],soma/len(notas[aluno]))
elif(len(alunos)>len(notas)):
    print('algum aluno esta sem nota')
else:
    print('há mais notas do que alunos')
input()