class aluno(object):
    def __init__(self, name):
        self.name = name
    def add_notas(self,n1,n2):
        self.n1=n1
        self.n2=n2
    def mostrar_informaçoes(self):
        try:
            statz=((self.n1+self.n2)/2>=6)
            if statz:
                print(f"aluno {self.name} foi aprovado com média {(self.n1+self.n2)/2}")
            else:
                print(f"aluno {self.name} foi reprovado com média {(self.n1+self.n2)/2}")
        except:
            print("defina as notas e depois veja as informações")

while True:
    a1=aluno(input("nome do aluno: "))
    try:
        a1.add_notas(float(input("nota1: ").replace(",",".")),float(input("nota2: ").replace(",",".")))
    except:
        print("digite numeros nos espaços para nota")
    a1.mostrar_informaçoes()