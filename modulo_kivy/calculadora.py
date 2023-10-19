from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import Layout

class MainApp(App):
    def build(self):
        main_layout = Layout(orientation='horizontal')

        main_layout.add_widget(Label(text='oi'))

        return main_layout
app=MainApp()   
app.run()