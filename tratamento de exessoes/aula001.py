while True:
    def dividir(n1,n2):
        
        try:
            
            n1=float(n1.replace(",", "."))
            n2=float(n2.replace(",", "."))
            return n1/n2
        except:
            return'mude os valores e tente novamente'


    print(dividir(str(input()),str(input())))
