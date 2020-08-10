from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.lang import Builder

#Class that hold rules and functions

#Builder.load_file('signin/signin.kv')

class SigninWindow(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
    def validate_user(self):
        user = self.ids.username_field
        pwd = self.ids.pwd_field
        stat = self.ids.status

        username = user.text
        password = pwd.text

        if username == '' or password == '':
            stat.text = '[color=#FF0000]username or password required[/color]'
        else:
            if username == 'admin' and password == 'admin':
                stat.text = '[color=#00FF00]logged in[/color]'
            else:
                stat.text = '[color=#FF0000]Invalid[/color]'
                
class SigninApp(App):
    def build(self):
        return SigninWindow()

if __name__ == "__main__":
    sa = SigninApp()
    sa.run()
