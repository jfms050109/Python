from kivy.app import App
from kivy.uix.button import Button

red=[1,0,0,1]

class MainApp(App):
    def build(self):
        btn= Button(text='clique se acha o ezequiel gay',background_color=red,size_hint=(1,.5),pos_hint={'center_x':.5,'center_y':.5})

        btn.bind(on_press=self.on_press_button)

        return btn
    def on_press_button(self,isnstance):
        print('o ezequiel é gay')
if __name__=="__main__":
    app= MainApp()
    app.run()
