from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
import mysql.connector
from kivy.uix.popup import Popup

Builder.load_file('signin/kv/signin.kv')
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="adminroot"
    )
print(db)
#Class that hold rules and functions

#Builder.load_file('signin/signin.kv')
cursor = db.cursor()
cursor.execute("USE auto_manufacture_management_system_new;")
db.commit()
class SigninWindow(BoxLayout):
    def __init__(self,**kwargs):
        print("Loaded")
        super().__init__(**kwargs)
    def validate_user(self):
        user = self.ids.username_field
        pwd = self.ids.pwd_field
        stat = self.ids.status

        username = user.text
        password = pwd.text

        if username == "" and password == "":
            pop = Popup(title="Missing Input", content=Label(text='Please enter your username and password'),
                        size_hint=(None, None), size=(400, 150))
            pop.open()
        else:
            try:
                login_query = "SELECT username, passcode FROM employee WHERE username='%s' AND passcode='%s'"
                cursor.execute(login_query % (username, password))
                rs = cursor.fetchall()
                if rs:
                    getpost_query = "SELECT branch, post FROM employee WHERE username='%s'"
                    cursor.execute(getpost_query % username)
                    post = cursor.fetchone()
                    branch, post = post[0], post[1]
                    print(post)
                    if branch == "Executive" and post == 'CEO':
                        self.parent.parent.current = 'scrn_admin'
                    elif post == 'dealer' or post == 'Dealer':
                        self.parent.parent.current = 'scrn_dealer'
                        
                else:
                    pop = Popup(title="Access Denied", content=Label(text='No such user'),
                                size_hint=(None, None), size=(150, 150))
                    pop.open()
            except Exception as e:
                print(e)
                pop = Popup(title="Unknown Error", content=Label(text='Unknown error. Contact software vendor '
                                                                      'if the problem persists.'),
                            size_hint=(None, None), size=(500, 150))
                pop.open()
                
class SigninApp(App):
    def build(self):
        return SigninWindow()

if __name__ == "__main__":
    sa = SigninApp()
    sa.run()
