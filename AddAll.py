from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from dealer.pydealer import DealerWindow
from signin.pysignin import SigninWindow
from mainadmin import AdminWindow
from kivy.lang import Builder


class MainWindow(BoxLayout):
    admin_widget = AdminWindow()
    signin_widget = SigninWindow()
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        
        self.ids.s_in.add_widget(self.admin_widget)
class MainApp(App):
    def buid(self):
        return MainWindow()

if __name__=='__main__':
    MainApp().run()
