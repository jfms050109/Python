import random
class pessoa:
    def __init__(self,nome="",idade=0,sexo=False,cpf=0):
        self.nome=nome
        self.sexo=sexo
        self.idade=idade
        self.cpf=cpf
    def gerar_cpf(self):
        self.cpf
        if self.cpf==0:
            self.cpf=random.randrange(0,999)
            print(self.cpf)
        else:
            print(f"{self.nome} já possui um cpf")
    especie="humano"
    

p1=pessoa("joão")
print(p1.especie)


while True:
    class pessoa:
        
        def __init__(self,nome="",idade=0,sexo=False,cpf=0):
            self.nome=nome
            self.sexo=sexo
            self.idade=idade
            self.cpf=cpf
        def gerar_cpf(self):
            
            self.cpf
            if self.cpf==0:
                self.cpf=random.randrange(0,999)
                print(self.cpf)
            else:
                print(f"{self.nome} já possui um cpf")

    
    p1.gerar_cpf()
    print(p1.cpf)
    p1.gerar_cpf()
    input()