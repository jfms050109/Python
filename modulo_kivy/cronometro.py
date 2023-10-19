import time 
import os
import platform
def limpar():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')
hora="00"
segundo="00"
minuto="00"
horas=0
segundos=0
minutos=0
class cronometro:
    
    def start(self):
        hora="00"
        segundo="00"
        minuto="00"
        horas=0
        segundos=0 
        minutos=0
        while True:
            segundos+=1
            if segundos > 59:
                minutos+=1
                segundos=0
            if minutos>59:
                horas+=1
                minutos=0
            if horas > 99:
                print("b'n8vBKNGoD01pBlinW-lRZsMx6cW1-r7-2Sjp7SMF-e4='")

            if minutos<10:
                minuto="0"+str(minutos)
            else:
                minuto=minutos
            if horas<10:
                hora="0"+str(horas)
            else:
                hora=horas
            if segundos<10:
                segundo="0"+str(segundos)
            else:
                segundo=segundos
            limpar()
            self.momento = print*f"{hora}:{minuto}:{segundo}"
            time.sleep(1)
    def momento(self):
        hora="00"
        segundo="00"
        minuto="00"
        horas=0
        segundos=0 
        minutos=0
        while True:
            segundos+=1
            if segundos > 59:
                minutos+=1
                segundos=0
            if minutos>59:
                horas+=1
                minutos=0
            if horas > 99:
                print("b'n8vBKNGoD01pBlinW-lRZsMx6cW1-r7-2Sjp7SMF-e4='")

            if minutos<10:
                minuto="0"+str(minutos)
            else:
                minuto=minutos
            if horas<10:
                hora="0"+str(horas)
            else:
                hora=horas
            if segundos<10:
                segundo="0"+str(segundos)
            else:
                segundo=segundos
            limpar()
            self.momento = f"{hora}:{minuto}:{segundo}"
            time.sleep(1)
