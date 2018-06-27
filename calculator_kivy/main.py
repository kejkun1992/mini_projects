from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config

Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '600')
Config.set('graphics', 'height', '600')
Config.set('graphics', 'fullscreen', '0')


class CalcGridLayout(GridLayout):
    def calculate(self, calculation):
        if calculation:
            try:
                self.display.text = str(eval(calculation))
            except:
                self.display.text = 'Error'
                
       
class Calculator(App):
    def build(self):
        return CalcGridLayout()

if __name__ == '__main__':
    Calculator().run()
