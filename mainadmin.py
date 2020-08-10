from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.core.window import Window
from kivy.uix.popup import Popup
import mysql.connector
from utils.datatable import DataTable
import numpy as np
from kivy.lang import Builder

#Builder.load_file('admin.kv')
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="adminroot"
    )
print(db)
employee_attr=[]
employee_data= []
post_data = []
post_attr=[]
search_post_data=[]
rnd_engineer_attr=[]
rnd_engineer_data=[]
dealer_attr=[]
dealer_data=[]
sales_attr=[]
sales_data=[]
purchases_attr=[]
purchases_data=[]
supplier_attr=[]
supplier_data=[]
project_attr=[]
project_data=[]



cursor = db.cursor()
cursor.execute("USE auto_manufacture_management_system_new;")
db.commit()

class AdminWindow(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        #Employee
        self.display_employee()
        #post
        self.display_post()
        self.display_dealer()
        self.display_sales()
        self.display_purchases()
        self.display_supplier()
        self.display_project()

    def add_dealer_field(self):
        target = self.ids.right_nav_dealer
        target.clear_widgets()
        e1 = TextInput(hint_text=dealer_attr[0],size_hint_y=None,height=30)
        e2 = TextInput(hint_text=dealer_attr[1],size_hint_y=None,height=30)
        submit = Button(text='Add',
                        size_hint_x=None,
                        width=100,
                        on_release=lambda x: self.add_dealer(e1.text,e2.text),size_hint_y=None,height=30)
        clear= Button(text='Clear',size_hint_x=None,width=100,on_release=lambda x:self.clear_dealer(),size_hint_y=None,height=30)
        target.add_widget(e1)
        target.add_widget(e2)
        target.add_widget(submit)
        target.add_widget(clear)
    def add_dealer(self,a1,a2):
        if a1 == "" or a2 == "":
            pop = Popup(title="Missing Input", content=Label(text='Please enter all the required fields'),
                        size_hint=(None, None), size=(400, 150))
            pop.open()
        else:
            try:
                content = self.ids.content_dealer_table
                content.clear_widgets()
                insert_query = "INSERT INTO dealer VALUES ('%s','%s');"
                cursor.execute(insert_query % (a1,a2))
                db.commit()
                self.display_dealer()
                pop = Popup(title="Dealer added", content=Label(text="Dealer has been added"),
                            size_hint=(None, None), size=(350, 150))
                pop.open()
            except Exception as e:
                pop = Popup(title="Error", content=Label(text=e),
                            size_hint=(None, None), size=(550, 150))
                pop.open()
    def clear_dealer(self):
        self.add_dealer_field()

    def display_dealer(self):
        content = self.ids.content_dealer_table
        cursor.execute("SELECT * FROM dealer;")
        dealer_data.clear()
        dealer_attr.clear()
        for i in cursor:
            dealer_data.append(i)
        cursor.execute("DESC dealer;")
        for i in cursor:
            dealer_attr.append(i[0])
        usertable = DataTable(dealer_data,dealer_attr)
        content.add_widget(usertable)

    def update_post_field(self):
        target = self.ids.right_nav_post
        target.clear_widgets()
        e1 = TextInput(hint_text=post_attr[0],size_hint_y=None,height=30)
        e2 = TextInput(hint_text=post_attr[1],size_hint_y=None,height=30)
        e3 = TextInput(hint_text=post_attr[2],size_hint_y=None,height=30)
        e4 = TextInput(hint_text="Insert Branch",size_hint_y=None,height=30)
        e5 = TextInput(hint_text="Insert Title",size_hint_y=None,height=30)
        update = Button(text='Update',size_hint_y=None,height=30,
                        size_hint_x=None,
                        width=100,
                        on_release=lambda x: self.update_post(e1.text,e2.text,e3.text,e4.text,e5.text))
        
        clear= Button(text='Clear',size_hint_x=None,width=100,on_release=lambda x:self.clear_post(),size_hint_y=None,height=30)
        target.add_widget(e4)
        target.add_widget(e5)
        target.add_widget(e1)
        target.add_widget(e2)
        target.add_widget(e3)
        target.add_widget(update)
        target.add_widget(clear)
    def update_post(self,branch,title,salary,temp_branch,temp_title):
        try:
            update_query = "UPDATE post SET branch = '%s', title = '%s', salary = '%s' WHERE branch = '%s' AND title = '%s' ;"
            cursor.execute(update_query % (branch,title,salary,temp_branch,temp_title))
            db.commit()
            self.display_post()
            pop = Popup(title="post updated", content=Label(text='Position has been updated'),
                        size_hint=(None, None), size=(400, 150))
            pop.open()
        except Exception as e:
            print(e)
            pop = Popup(title="Error", content=Label(text='Post not updated. Incorrect data values.'),
                        size_hint=(None, None), size=(500, 150))
            pop.open()
        
    def add_post_field(self):
        target = self.ids.right_nav_post
        target.clear_widgets()
        e1 = TextInput(hint_text=post_attr[0],size_hint_y=None,height=30)
        e2 = TextInput(hint_text=post_attr[1],size_hint_y=None,height=30)
        e3 = TextInput(hint_text=post_attr[2],size_hint_y=None,height=30)
        submit = Button(text='Add',
                        size_hint_x=None,
                        width=100,
                        on_release=lambda x: self.add_post(e1.text,
                                                                e2.text,
                                                                e3.text),size_hint_y=None,height=30)
        clear= Button(text='Clear',size_hint_x=None,width=100,on_release=lambda x:self.clear_post(),size_hint_y=None,height=30)
        target.add_widget(e1)
        target.add_widget(e2)
        target.add_widget(e3)
        target.add_widget(submit)
        target.add_widget(clear)

    def delete_post_field(self):
        target = self.ids.right_nav_post
        target.clear_widgets()
        e1 = TextInput(hint_text="Insert Branch",size_hint_y=None,height=30)
        e2 = TextInput(hint_text="Insert Title",size_hint_y=None,height=30)
        submit = Button(text='Delete',
                        size_hint_x=None,
                        width=100,
                        on_release=lambda x: self.delete_post(e1.text,
                                                                e2.text),size_hint_y=None,height=30)
        clear= Button(text='Clear',size_hint_x=None,width=100,on_release=lambda x:self.clear_post(),size_hint_y=None,height=30)
        target.add_widget(e1)
        target.add_widget(e2)
        target.add_widget(submit)
        target.add_widget(clear)
    def delete_post(self,a1,a2):
        try:
            content = self.ids.content_post_table
            content.clear_widgets()
            delete_query = "DELETE FROM post WHERE branch='%s' AND title ='%s';"
            cursor.execute(delete_query % (a1,a2))
            db.commit()
            self.display_post()
            pop = Popup(title="Post deleted", content=Label(text='Post has been deleted'),
                        size_hint=(None, None), size=(400, 150))
            pop.open()
        except Exception as e:
            print(e)
            pop = Popup(title="Error", content=Label(text='Post cannot be deleted.'),
                        size_hint=(None, None), size=(500, 150))
            pop.open()
    
        
    def clear_post(self):
        self.add_post_field()
        
    def add_post(self,a1,a2,a3):
        if a1 == "" or a2 == "" or a3 == "":
            pop = Popup(title="Missing Input", content=Label(text='Please enter all the required fields'),
                        size_hint=(None, None), size=(400, 150))
            pop.open()
        else:
            try:
                content = self.ids.content_post
                content.clear_widgets()
                insert_query = "INSERT INTO post VALUES ('%s','%s','%s');"
                cursor.execute(insert_query % (a1,a2,a3))
                db.commit()
                self.display_post()
                pop = Popup(title="Position added", content=Label(text='Position has been added'),
                            size_hint=(None, None), size=(350, 150))
                pop.open()
            except Exception as e:
                print(e)
                pop = Popup(title="Error", content=Label(text=e),
                            size_hint=(None, None), size=(550, 150))
                pop.open()
    def display_post(self):
        content = self.ids.content_post_table
        content.clear_widgets()
        cursor.execute("SELECT * FROM post;")
        post_data.clear()
        post_attr.clear()
        print("get_post:",post_data)
        for i in cursor:
            post_data.append(i)
        cursor.execute("DESC post;")
        for i in cursor:
            post_attr.append(i[0])
        print("dispsot",post_data)
        print("disspoetarr",post_attr)
        usertable = DataTable(post_data,post_attr)
        content.add_widget(usertable)

    def delete_employee_field(self):
        target = self.ids.right_nav_emp
        target.clear_widgets()
        e1 = TextInput(hint_text="Insert Username",size_hint_y=None,height=30)
        submit = Button(text='Delete',
                        size_hint_x=None,
                        width=100,
                        on_release=lambda x: self.delete_employee(e1.text),size_hint_y=None,height=30)
        clear= Button(text='Clear',size_hint_x=None,width=100,on_release=lambda x:self.clear_employee(),size_hint_y=None,height=30)
        target.add_widget(e1)
        target.add_widget(submit)
        target.add_widget(clear)
    def delete_employee(self,a1):
        try:
            
            delete_query = "DELETE FROM employee WHERE username='%s';"
            cursor.execute(delete_query % (a1))
            db.commit()
            content = self.ids.content_emp_op
            content.clear_widgets()
            self.display_post()
            pop = Popup(title="Employee deleted", content=Label(text='Employee has been deleted'),
                        size_hint=(None, None), size=(400, 150))
            pop.open()
        except Exception as e:
            print(e)
            pop = Popup(title="Error", content=Label(text='Employee cannot be deleted.'),
                        size_hint=(None, None), size=(500, 150))
            pop.open()
    
    def update_employee_field(self):
        target = self.ids.right_nav_emp
        target.clear_widgets()
        e1 = TextInput(hint_text=employee_attr[0],size_hint_y=None,height=30)
        e2 = TextInput(hint_text=employee_attr[1],size_hint_y=None,height=30)
        e3 = TextInput(hint_text=employee_attr[2],size_hint_y=None,height=30)
        e4 = TextInput(hint_text=employee_attr[3],size_hint_y=None,height=30)
        e5 = TextInput(hint_text=employee_attr[4],size_hint_y=None,height=30)
        e6 = TextInput(hint_text=employee_attr[5],size_hint_y=None,height=30)
        e7 = TextInput(hint_text=employee_attr[6],size_hint_y=None,height=30)
        e8 = TextInput(hint_text=employee_attr[7],size_hint_y=None,height=30)
        e9 = TextInput(hint_text=employee_attr[8],size_hint_y=None,height=30)
        e10 = TextInput(hint_text=employee_attr[9],size_hint_y=None,height=30)
        e11 = TextInput(hint_text=employee_attr[10],size_hint_y=None,height=30)
        e12 = TextInput(hint_text=employee_attr[11],size_hint_y=None,height=30)
        e13 = TextInput(hint_text=employee_attr[12],size_hint_y=None,height=30)
        e14 = TextInput(hint_text="Search Username")
        Update = Button(text='Update',
                        size_hint_x=None,
                        width=100,
                        on_release=lambda x: self.update_employee(e1.text,
                                                                e2.text,
                                                                e3.text,
                                                                e4.text,
                                                                e5.text,
                                                                e6.text,
                                                                e7.text,
                                                                e8.text,
                                                                e9.text,
                                                                e10.text,
                                                                e11.text,e12.text,e13.text,e14.text),size_hint_y=None,height=30)
        clear= Button(text='Clear',size_hint_x=None,width=100,on_release=lambda x:self.clear_employee(),size_hint_y=None,height=30)
        target.add_widget(e14)
        target.add_widget(e1)
        target.add_widget(e2)
        target.add_widget(e3)
        target.add_widget(e4)
        target.add_widget(e5)
        target.add_widget(e6)
        target.add_widget(e7)
        target.add_widget(e8)
        target.add_widget(e9)
        target.add_widget(e10)
        target.add_widget(e11)
        target.add_widget(e12)
        target.add_widget(e13)
        target.add_widget(Update)
        target.add_widget(clear)
        
    def update_employee(self,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14):
        if a14 == "" :
            pop = Popup(title="Missing Input", content=Label(text='Please username'),
                        size_hint=(None, None), size=(400, 150))
            pop.open()
        else:
            try:
                content = self.ids.content_emp_op
                content.clear_widgets()
                update_query = "UPDATE employee SET username = '%s', passcode = '%s', first_name = '%s', middle_name = '%s', last_name = '%s', gender = '%s', date_of_birth = '%s', address = '%s', email = '%s', contact_number = '%s', emp_status = '%s', branch = '%s', post = '%s' WHERE username = '%s';"
                cursor.execute(update_query % (a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14))
                db.commit()
                self.display_employee()
                pop = Popup(title="Employee updated", content=Label(text='Employee has been updated'),
                            size_hint=(None, None), size=(400, 150))
                pop.open()
            except Exception as e:
                print(e)
                pop = Popup(title="Error", content=Label(text='Employee not updated. Incorrect data values.'),
                            size_hint=(None, None), size=(500, 150))
                pop.open()
                
    
    def add_employee_field(self):
        target = self.ids.right_nav_emp
        target.clear_widgets()
        e1 = TextInput(hint_text=employee_attr[0],size_hint_y=None,height=30)
        e2 = TextInput(hint_text=employee_attr[1],size_hint_y=None,height=30)
        e3 = TextInput(hint_text=employee_attr[2],size_hint_y=None,height=30)
        e4 = TextInput(hint_text=employee_attr[3],size_hint_y=None,height=30)
        e5 = TextInput(hint_text=employee_attr[4],size_hint_y=None,height=30)
        e6 = TextInput(hint_text=employee_attr[5],size_hint_y=None,height=30)
        e7 = TextInput(hint_text=employee_attr[6],size_hint_y=None,height=30)
        e8 = TextInput(hint_text=employee_attr[7],size_hint_y=None,height=30)
        e9 = TextInput(hint_text=employee_attr[8],size_hint_y=None,height=30)
        e10 = TextInput(hint_text=employee_attr[9],size_hint_y=None,height=30)
        e11 = TextInput(hint_text=employee_attr[10],size_hint_y=None,height=30)
        e12 = TextInput(hint_text=employee_attr[11],size_hint_y=None,height=30)
        e13 = TextInput(hint_text=employee_attr[12],size_hint_y=None,height=30)
        submit = Button(text='Add',size_hint_y=None,height=30,
                        size_hint_x=None,
                        width=100,
                        on_release=lambda x: self.add_employee(e1.text,
                                                                e2.text,
                                                                e3.text,
                                                                e4.text,
                                                                e5.text,
                                                                e6.text,
                                                                e7.text,
                                                                e8.text,
                                                                e9.text,
                                                                e10.text,
                                                                e11.text,e12.text,e13.text))
        clear= Button(text='Clear',size_hint_x=None,width=100,on_release=lambda x:self.clear_employee(),size_hint_y=None,height=30)
        target.add_widget(e1)
        target.add_widget(e2)
        target.add_widget(e3)
        target.add_widget(e4)
        target.add_widget(e5)
        target.add_widget(e6)
        target.add_widget(e7)
        target.add_widget(e8)
        target.add_widget(e9)
        target.add_widget(e10)
        target.add_widget(e11)
        target.add_widget(e12)
        target.add_widget(e13)
        target.add_widget(submit)
        target.add_widget(clear)
    
    def clear_employee(self):
        self.add_employee_field()
                
    def add_employee(self,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13):
        if a1 == "" or a2 == "" or a3 == "" or a4 == "" or a5 == "" or a6 == "" or a7 == "" or a8 == "" or a9 == "" or a10 == "" or a11 == "" or a12 == "":
            pop = Popup(title="Missing Input", content=Label(text='Please enter all the required fields'),
                        size_hint=(None, None), size=(400, 150))
            pop.open()
        else:
            try:
                content = self.ids.content_emp_op
                content.clear_widgets()
                insert_query = "INSERT INTO employee(username, passcode, first_name, middle_name, last_name, gender, date_of_birth, address, email, contact_number, emp_status, branch, post) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');"
                cursor.execute(insert_query % (a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13))
                db.commit()
                self.display_employee()
                pop = Popup(title="Employee added", content=Label(text='Employee has been added'),
                            size_hint=(None, None), size=(150, 150))
                pop.open()
            except Exception as e:
                print(e)
                pop = Popup(title="Error", content=Label(text=e),
                            size_hint=(None, None), size=(500, 150))
                pop.open()
            
    def display_employee(self):
        content = self.ids.content_emp_op
        cursor.execute("SELECT * FROM employee;")
        employee_data.clear()
        employee_attr.clear()
        print("get_employee:",employee_data)
        for i in cursor:
            employee_data.append(i)
        cursor.execute("DESC employee;")
        for i in cursor:
            employee_attr.append(i[0])
        print("disepm",employee_data)
        print("disarrt",employee_attr)
        usertable = DataTable(employee_data,employee_attr)
        content.add_widget(usertable)

    def display_purchases(self):
        content = self.ids.content_purchases_table
        cursor.execute("SELECT * FROM purchases;")
        purchases_data.clear()
        purchases_attr.clear()
        for i in cursor:
            purchases_data.append(i)
        cursor.execute("DESC purchases;")
        for i in cursor:
            purchases_attr.append(i[0])
        usertable = DataTable(purchases_data,purchases_attr)
        content.add_widget(usertable)
    def display_supplier(self):
        content = self.ids.content_supplier_table
        cursor.execute("SELECT * FROM supplier;")
        supplier_data.clear()
        supplier_attr.clear()
        for i in cursor:
            supplier_data.append(i)
        cursor.execute("DESC supplier;")
        for i in cursor:
            supplier_attr.append(i[0])
        usertable = DataTable(supplier_data,supplier_attr)
        content.add_widget(usertable)

    def display_project(self):
        content = self.ids.content_project_table
        cursor.execute("SELECT * FROM project;")
        project_data.clear()
        project_attr.clear()
        for i in cursor:
            project_data.append(i)
        cursor.execute("DESC project;")
        for i in cursor:
            project_attr.append(i[0])
        usertable = DataTable(project_data,project_attr)
        content.add_widget(usertable)
        
        
    def display_sales(self):
        content = self.ids.content_sales_table
        cursor.execute("SELECT * FROM sales;")
        sales_data.clear()
        sales_attr.clear()
        for i in cursor:
            sales_data.append(i)
        cursor.execute("DESC sales;")
        for i in cursor:
            sales_attr.append(i[0])
        usertable = DataTable(sales_data,sales_attr)
        content.add_widget(usertable)
        
            
    
        
        
    def change_screen(self,instance):
        if instance.text == 'Employee':
            self.ids.screen_mngr.current = 'content_emp'
        elif instance.text == 'rnd_engineer':
            self.ids.screen_mngr.current = 'content_rnd_engineer'
        elif instance.text == 'assembling_engineer':
            self.ids.screen_mngr.current = 'content_assembling_engineer'
        elif instance.text == 'dealer':
            self.ids.screen_mngr.current = 'content_dealer'
        elif instance.text == 'post':
            self.ids.screen_mngr.current = 'content_post_main'
        elif instance.text == 'sales':
            self.ids.screen_mngr.current = 'content_sales'
        elif instance.text == 'sale_products':
            self.ids.screen_mngr.current = 'content_sale_products'
        elif instance.text == 'retailer':
            self.ids.screen_mngr.current = 'content_retailer'
        elif instance.text == 'purchases':
            self.ids.screen_mngr.current = 'content_purchases'
        elif instance.text == 'purchase_products':
            self.ids.screen_mngr.current = 'content_purchase_products'
        elif instance.text == 'raw_material':
            self.ids.screen_mngr.current = 'content_raw_material'
        elif instance.text == 'supplier':
            self.ids.screen_mngr.current = 'content_supplier'
        elif instance.text == 'project':
            self.ids.screen_mngr.current = 'content_project'
        elif instance.text == 'project_material_requirements':
            self.ids.screen_mngr.current = 'content_project_material_requirements'
        elif instance.text == 'auto_engine':
            self.ids.screen_mngr.current = 'content_auto_engine'
        elif instance.text == 'chassis':
            self.ids.screen_mngr.current = 'content_chassis'
        elif instance.text == 'suspension':
            self.ids.screen_mngr.current = 'content_suspension'
        elif instance.text == 'wheel':
            self.ids.screen_mngr.current = 'content_wheel'
        elif instance.text == 'automobile':
            self.ids.screen_mngr.current = 'content_automobile'
        elif instance.text == 'assembling_plant':
            self.ids.screen_mngr.current = 'content_assembling_plant'
        
    
        
class AdminApp(App):
    def build(self):
        return AdminWindow()

if __name__ == "__main__":
    AdminApp().run()
    
