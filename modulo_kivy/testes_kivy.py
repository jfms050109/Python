import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
from cronometro import cronometro
import time

class MainApp(App):
    global hora
    global segundo
    global minuto
    global horas
    global segundos 
    global minutos
    hora="00"
    segundo="00"
    minuto="00"
    horas=0
    segundos=0 
    minutos=0
    def build(self):
        Clock.schedule_interval(self.atualizar_texto, 1.0)
        self.label= Label(text="teste", size_hint=(10,10),pos_hint={'center_x': .5, 'center_y': .5}, font_size=100)
        return self.label
    def atualizar_texto(self, dt):
        global hora
        global segundo
        global minuto
        global horas
        global segundos 
        global minutos
        
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
        
        self.momento = f"{hora}:{minuto}:{segundo}"
        #time.sleep(1)
        self.label.text = self.momento

        
if __name__ == "__main__":
    MainApp().run()
    