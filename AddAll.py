from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from signin.pysignin import SigninWindow
from dealer.pydealer import DealerWindow
from mainadmin import AdminWindow
from kivy.lang import Builder

Builder.load_file('main.kv')

class MainWindow(Screen):
    signin_widget = SigninWindow()
    admin_widget = AdminWindow()
    dealer_widget = DealerWindow()
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.ids.scrn_signin.add_widget(self.signin_widget)
        self.ids.scrn_admin.add_widget(self.admin_widget)
        self.ids.scrn_dealer.add_widget(self.dealer_widget)

    
        
class MainApp(App):
    def build(self):
        return MainWindow()

if __name__ == "__main__":
    MainApp().run()
    
