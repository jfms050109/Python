class calc:
    def __init__(self,n1=0,n2=0) -> None:
        self.n1=n1
        self.n2=n2 

    def soma(self):
        try:
            return float(self.n1)+float(self.n2)
        except:
            return"verifique os valores e tente novamente"
    def sub(self):
        try:
            return float(self.n1)-float(self.n2)
        except:
            return "verifique os valores e tente novamente"
    def mult(self):
        try:
            return float(self.n1)*float(self.n2)
        except:
            return "verifique os valores e tente novamente"
    def div(self):
        try:
            return float(self.n1)/float(self.n2)
        except:
            return"verifique os valores e tente novamente"

while True:
    c=calc(str(input().replace(',','.')),str(input().replace(',','.')))
    print(c.div())