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
from kivy.lang import Builder
import numpy as np

#Builder.load_file('dealer/dealer.kv')
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
retailer_attr=[]
retailer_data=[]



cursor = db.cursor()
cursor.execute("USE auto_manufacture_management_system_new;")
db.commit()

class DealerWindow(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        self.display_sales()
        self.display_purchases()
        self.display_supplier()
        self.display_retailer()
    #--------------------------------------------------------------------   
    def update_sales_field(self):
        target = self.ids.right_nav_sales
        target.clear_widgets()
        e1 = TextInput(hint_text=sales_attr[0],size_hint_y=None,height=30)
        e2 = TextInput(hint_text=sales_attr[1],size_hint_y=None,height=30)
        e3 = TextInput(hint_text=sales_attr[2],size_hint_y=None,height=30)
        e4 = TextInput(hint_text=sales_attr[3],size_hint_y=None,height=30)
        e5 = TextInput(hint_text=sales_attr[4],size_hint_y=None,height=30)
        e6 = TextInput(hint_text=sales_attr[5],size_hint_y=None,height=30)
        e7 = TextInput(hint_text="Insert Transaction Code",size_hint_y=None,height=30)
        update = Button(text='Update',size_hint_y=None,height=30,
                        size_hint_x=None,
                        width=100,
                        on_release=lambda x: self.update_sales(e1.text,e2.text,e3.text,e4.text,e5.text,e6.text,e7.text))
        
        clear= Button(text='Clear',size_hint_x=None,width=100,on_release=lambda x:self.clear_sales(),size_hint_y=None,height=30)
        target.add_widget(e7)
        target.add_widget(e1)
        target.add_widget(e2)
        target.add_widget(e3)
        target.add_widget(e4)
        target.add_widget(e5)
        target.add_widget(e6)
        target.add_widget(update)
        target.add_widget(clear)
    def update_sales(self,a1,a2,a3,a4,a5,a6,a7):
        try:
            
            update_query = "UPDATE sales SET transaction_code = '%s', date_occured = '%s', transaction_amount = '%s',profit='%s',dealer='%s',retailer='%s' WHERE transaction_code = '%s';"
            cursor.execute(update_query % (a1,a2,a3,a4,a5,a6,a7))
            db.commit()
            content = self.ids.content_sales_table
            content.clear_widgets()
            self.display_post()
            pop = Popup(title="Sales updated", content=Label(text='Sales has been updated'),
                        size_hint=(None, None), size=(400, 150))
            pop.open()
        except Exception as e:
            print(e)
            pop = Popup(title="Error", content=Label(text='Sales not updated. Incorrect data values.'),
                        size_hint=(None, None), size=(500, 150))
            pop.open()
        
    def add_sales_field(self):
        target = self.ids.right_nav_sales
        target.clear_widgets()
        e1 = TextInput(hint_text=sales_attr[0],size_hint_y=None,height=30)
        e2 = TextInput(hint_text=sales_attr[1],size_hint_y=None,height=30)
        e3 = TextInput(hint_text=sales_attr[2],size_hint_y=None,height=30)
        e4 = TextInput(hint_text=sales_attr[3],size_hint_y=None,height=30)
        e5 = TextInput(hint_text=sales_attr[4],size_hint_y=None,height=30)
        e6 = TextInput(hint_text=sales_attr[5],size_hint_y=None,height=30)
        submit = Button(text='Add',
                        size_hint_x=None,
                        width=100,
                        on_release=lambda x: self.add_sales(e1.text,
                                                                e2.text,
                                                                e3.text,
                                                                e4.text,e5.text,e6.text),size_hint_y=None,height=30)
        clear= Button(text='Clear',size_hint_x=None,width=100,on_release=lambda x:self.clear_sales(),size_hint_y=None,height=30)
        target.add_widget(e1)
        target.add_widget(e2)
        target.add_widget(e3)
        target.add_widget(e4)
        target.add_widget(e5)
        target.add_widget(e6)
        target.add_widget(submit)
        target.add_widget(clear)

    def delete_sales_field(self):
        target = self.ids.right_nav_sales
        target.clear_widgets()
        e1 = TextInput(hint_text="Insert transaction code",size_hint_y=None,height=30)
        submit = Button(text='Delete',
                        size_hint_x=None,
                        width=100,
                        on_release=lambda x: self.delete_sales(e1.text),size_hint_y=None,height=30)
        clear= Button(text='Clear',size_hint_x=None,width=100,on_release=lambda x:self.clear_sales(),size_hint_y=None,height=30)
        target.add_widget(e1)
        target.add_widget(submit)
        target.add_widget(clear)
    def delete_sales(self,a1):
        try:
            content = self.ids.content_sales_table
            content.clear_widgets()
            delete_query = "DELETE FROM sales WHERE transaction_code='%s';"
            cursor.execute(delete_query % (a1))
            db.commit()
            self.display_sales()
            pop = Popup(title="Sales deleted", content=Label(text='Sales has been deleted'),
                        size_hint=(None, None), size=(400, 150))
            pop.open()
        except Exception as e:
            print(e)
            pop = Popup(title="Error", content=Label(text='Sales cannot be deleted.'),
                        size_hint=(None, None), size=(500, 150))
            pop.open()
    
        
    def clear_sales(self):
        self.add_sales_field()
        
    def add_sales(self,a1,a2,a3,a4,a5,a6):
        if a1 == "" or a2 == "" or a3 == "":
            pop = Popup(title="Missing Input", content=Label(text='Please enter all the required fields'),
                        size_hint=(None, None), size=(400, 150))
            pop.open()
        else:
            try:
                content = self.ids.content_sales_table
                content.clear_widgets()
                insert_query = "INSERT INTO sales VALUES ('%s','%s','%s','%s','%s','%s');"
                cursor.execute(insert_query % (a1,a2,a3,a4,a5,a6))
                db.commit()
                self.display_sales()
                pop = Popup(title="Sales added", content=Label(text='Sales has been added'),
                            size_hint=(None, None), size=(350, 150))
                pop.open()
            except Exception as e:
                print(e)
                pop = Popup(title="Error", content=Label(text=e),
                            size_hint=(None, None), size=(550, 150))
                pop.open()
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
    #------------------------------------------------------------------------
    def update_purchases_field(self):
        target = self.ids.right_nav_purchases
        target.clear_widgets()
        e1 = TextInput(hint_text=purchases_attr[0],size_hint_y=None,height=30)
        e2 = TextInput(hint_text=purchases_attr[1],size_hint_y=None,height=30)
        e3 = TextInput(hint_text=purchases_attr[2],size_hint_y=None,height=30)
        e4 = TextInput(hint_text=purchases_attr[3],size_hint_y=None,height=30)
        e5 = TextInput(hint_text=purchases_attr[4],size_hint_y=None,height=30)
        e7 = TextInput(hint_text="Insert Transaction Code",size_hint_y=None,height=30)
        update = Button(text='Update',size_hint_y=None,height=30,
                        size_hint_x=None,
                        width=100,
                        on_release=lambda x: self.update_purchases(e1.text,e2.text,e3.text,e4.text,e5.text,e7.text))
        
        clear= Button(text='Clear',size_hint_x=None,width=100,on_release=lambda x:self.clear_purchases(),size_hint_y=None,height=30)
        target.add_widget(e7)
        target.add_widget(e1)
        target.add_widget(e2)
        target.add_widget(e3)
        target.add_widget(e4)
        target.add_widget(e5)
        target.add_widget(update)
        target.add_widget(clear)
    def update_purchases(self,a1,a2,a3,a4,a5,a6):
        try:
            
            update_query = "UPDATE purchases SET transaction_code = '%s', date_occured = '%s', transaction_amount = '%s',dealer='%s',supplier='%s' WHERE transaction_code = '%s';"
            cursor.execute(update_query % (a1,a2,a3,a4,a5,a6))
            db.commit()
            content = self.ids.content_purchases_table
            content.clear_widgets()
            self.display_post()
            pop = Popup(title="purchases updated", content=Label(text='purchases has been updated'),
                        size_hint=(None, None), size=(400, 150))
            pop.open()
        except Exception as e:
            print(e)
            pop = Popup(title="Error", content=Label(text='purchases not updated. Incorrect data values.'),
                        size_hint=(None, None), size=(500, 150))
            pop.open()
        
    def add_purchases_field(self):
        target = self.ids.right_nav_purchases
        target.clear_widgets()
        e1 = TextInput(hint_text=purchases_attr[0],size_hint_y=None,height=30)
        e2 = TextInput(hint_text=purchases_attr[1],size_hint_y=None,height=30)
        e3 = TextInput(hint_text=purchases_attr[2],size_hint_y=None,height=30)
        e4 = TextInput(hint_text=purchases_attr[3],size_hint_y=None,height=30)
        e5 = TextInput(hint_text=purchases_attr[4],size_hint_y=None,height=30)
        submit = Button(text='Add',
                        size_hint_x=None,
                        width=100,
                        on_release=lambda x: self.add_purchases(e1.text,
                                                                e2.text,
                                                                e3.text,
                                                                e4.text,e5.text),size_hint_y=None,height=30)
        clear= Button(text='Clear',size_hint_x=None,width=100,on_release=lambda x:self.clear_purchases(),size_hint_y=None,height=30)
        target.add_widget(e1)
        target.add_widget(e2)
        target.add_widget(e3)
        target.add_widget(e4)
        target.add_widget(e5)
        target.add_widget(submit)
        target.add_widget(clear)

    def delete_purchases_field(self):
        target = self.ids.right_nav_purchases
        target.clear_widgets()
        e1 = TextInput(hint_text="Insert transaction code",size_hint_y=None,height=30)
        submit = Button(text='Delete',
                        size_hint_x=None,
                        width=100,
                        on_release=lambda x: self.delete_purchases(e1.text),size_hint_y=None,height=30)
        clear= Button(text='Clear',size_hint_x=None,width=100,on_release=lambda x:self.clear_purchases(),size_hint_y=None,height=30)
        target.add_widget(e1)
        target.add_widget(submit)
        target.add_widget(clear)
    def delete_purchases(self,a1):
        try:
            content = self.ids.content_purchases_table
            content.clear_widgets()
            delete_query = "DELETE FROM purchases WHERE transaction_code='%s';"
            cursor.execute(delete_query % (a1))
            db.commit()
            self.display_purchases()
            pop = Popup(title="purchases deleted", content=Label(text='purchases has been deleted'),
                        size_hint=(None, None), size=(400, 150))
            pop.open()
        except Exception as e:
            print(e)
            pop = Popup(title="Error", content=Label(text='purchases cannot be deleted.'),
                        size_hint=(None, None), size=(500, 150))
            pop.open()
    
        
    def clear_purchases(self):
        self.add_purchases_field()
        
    def add_purchases(self,a1,a2,a3,a4,a5):
        if a1 == "" or a2 == "" or a3 == "":
            pop = Popup(title="Missing Input", content=Label(text='Please enter all the required fields'),
                        size_hint=(None, None), size=(400, 150))
            pop.open()
        else:
            try:
                content = self.ids.content_purchases_table
                content.clear_widgets()
                insert_query = "INSERT INTO purchases VALUES ('%s','%s','%s','%s','%s');"
                cursor.execute(insert_query % (a1,a2,a3,a4,a5))
                db.commit()
                self.display_purchases()
                pop = Popup(title="purchases added", content=Label(text='purchases has been added'),
                            size_hint=(None, None), size=(350, 150))
                pop.open()
            except Exception as e:
                print(e)
                pop = Popup(title="Error", content=Label(text=e),
                            size_hint=(None, None), size=(550, 150))
                pop.open()
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
    #Purchases End
    #------------------------------------------------------------------------------------
    def update_retailer_field(self):
        target = self.ids.right_nav_retailer
        target.clear_widgets()
        e1 = TextInput(hint_text=retailer_attr[0],size_hint_y=None,height=30)
        e2 = TextInput(hint_text=retailer_attr[1],size_hint_y=None,height=30)
        e3 = TextInput(hint_text=retailer_attr[2],size_hint_y=None,height=30)
        e4 = TextInput(hint_text=retailer_attr[3],size_hint_y=None,height=30)
        e7 = TextInput(hint_text="Insert Transaction Code",size_hint_y=None,height=30)
        update = Button(text='Update',size_hint_y=None,height=30,
                        size_hint_x=None,
                        width=100,
                        on_release=lambda x: self.update_retailer(e1.text,e2.text,e3.text,e4.text,e7.text))
        
        clear= Button(text='Clear',size_hint_x=None,width=100,on_release=lambda x:self.clear_retailer(),size_hint_y=None,height=30)
        target.add_widget(e7)
        target.add_widget(e1)
        target.add_widget(e2)
        target.add_widget(e3)
        target.add_widget(e4)
        target.add_widget(update)
        target.add_widget(clear)
    def update_retailer(self,a1,a2,a3,a4,a5):
        try:
            
            update_query = "UPDATE retailer SET retailer_name = '%s', address = '%s', email = '%s',dealer='%s',contact_number='%s' WHERE retailer_name = '%s';"
            cursor.execute(update_query % (a1,a2,a3,a4,a5))
            db.commit()
            content = self.ids.content_retailer_table
            content.clear_widgets()
            self.display_retailer()
            pop = Popup(title="retailer updated", content=Label(text='retailer has been updated'),
                        size_hint=(None, None), size=(400, 150))
            pop.open()
        except Exception as e:
            print(e)
            pop = Popup(title="Error", content=Label(text='retailer not updated. Incorrect data values.'),
                        size_hint=(None, None), size=(500, 150))
            pop.open()
        
    def add_retailer_field(self):
        target = self.ids.right_nav_retailer
        target.clear_widgets()
        e1 = TextInput(hint_text=retailer_attr[0],size_hint_y=None,height=30)
        e2 = TextInput(hint_text=retailer_attr[1],size_hint_y=None,height=30)
        e3 = TextInput(hint_text=retailer_attr[2],size_hint_y=None,height=30)
        e4 = TextInput(hint_text=retailer_attr[3],size_hint_y=None,height=30)
        submit = Button(text='Add',
                        size_hint_x=None,
                        width=100,
                        on_release=lambda x: self.add_retailer(e1.text,
                                                                e2.text,
                                                                e3.text,
                                                                e4.text),size_hint_y=None,height=30)
        clear= Button(text='Clear',size_hint_x=None,width=100,on_release=lambda x:self.clear_retailer(),size_hint_y=None,height=30)
        target.add_widget(e1)
        target.add_widget(e2)
        target.add_widget(e3)
        target.add_widget(e4)
        target.add_widget(submit)
        target.add_widget(clear)

    def delete_retailer_field(self):
        target = self.ids.right_nav_retailer
        target.clear_widgets()
        e1 = TextInput(hint_text="Insert Name",size_hint_y=None,height=30)
        submit = Button(text='Delete',
                        size_hint_x=None,
                        width=100,
                        on_release=lambda x: self.delete_retailer(e1.text),size_hint_y=None,height=30)
        clear= Button(text='Clear',size_hint_x=None,width=100,on_release=lambda x:self.clear_retailer(),size_hint_y=None,height=30)
        target.add_widget(e1)
        target.add_widget(submit)
        target.add_widget(clear)
    def delete_retailer(self,a1):
        try:
            content = self.ids.content_retailer_table
            content.clear_widgets()
            delete_query = "DELETE FROM retailer WHERE retailer_name='%s';"
            cursor.execute(delete_query % (a1))
            db.commit()
            self.display_retailer()
            pop = Popup(title="retailer deleted", content=Label(text='retailer has been deleted'),
                        size_hint=(None, None), size=(400, 150))
            pop.open()
        except Exception as e:
            print(e)
            pop = Popup(title="Error", content=Label(text='retailer cannot be deleted.'),
                        size_hint=(None, None), size=(500, 150))
            pop.open()
    
        
    def clear_retailer(self):
        self.add_retailer_field()
        
    def add_retailer(self,a1,a2,a3,a4):
        if a1 == "" or a2 == "" or a3 == "":
            pop = Popup(title="Missing Input", content=Label(text='Please enter all the required fields'),
                        size_hint=(None, None), size=(400, 150))
            pop.open()
        else:
            try:
                content = self.ids.content_retailer_table
                content.clear_widgets()
                insert_query = "INSERT INTO retailer VALUES ('%s','%s','%s','%s');"
                cursor.execute(insert_query % (a1,a2,a3,a4))
                db.commit()
                self.display_retailer()
                pop = Popup(title="retailer added", content=Label(text='retailer has been added'),
                            size_hint=(None, None), size=(350, 150))
                pop.open()
            except Exception as e:
                print(e)
                pop = Popup(title="Error", content=Label(text=e),
                            size_hint=(None, None), size=(550, 150))
                pop.open()
    def display_retailer(self):
        content = self.ids.content_retailer_table
        cursor.execute("SELECT * FROM retailer;")
        retailer_data.clear()
        retailer_attr.clear()
        for i in cursor:
            retailer_data.append(i)
        cursor.execute("DESC retailer;")
        for i in cursor:
            retailer_attr.append(i[0])
        usertable = DataTable(retailer_data,retailer_attr)
        content.add_widget(usertable)
    #------------------------------------------------------------------------------------
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

    
        
        
    
        
            
    
        
        
    def change_screen(self,instance):
        if instance.text == 'Employee':
            self.ids.screen_mngr.current = 'content_emp'
        elif instance.text == 'rnd_engineer':
            self.ids.screen_mngr.current = 'content_rnd_engineer'
        elif instance.text == 'assembling_engineer':
            self.ids.screen_mngr.current = 'content_assembling_engineer'
        elif instance.text == 'dealer':
            self.ids.screen_mngr.current = 'content_dealer'
        elif instance.text == 'Product_details':
            self.ids.screen_mngr.current = 'content_'
        elif instance.text == 'sales':
            self.ids.screen_mngr.current = 'content_sales'
        elif instance.text == 'Sale Details':
            self.ids.screen_mngr.current = 'content_sale_products'
        elif instance.text == 'retailer':
            self.ids.screen_mngr.current = 'content_retailer'
        elif instance.text == 'purchases':
            self.ids.screen_mngr.current = 'content_purchases'
        elif instance.text == 'Purchase Details':
            self.ids.screen_mngr.current = 'content_purchase_products'
        elif instance.text == 'supplier':
            self.ids.screen_mngr.current = 'content_supplier'
        
    
        
class DealerApp(App):
    def build(self):
        return DealerWindow()

if __name__ == "__main__":
    op = DealerApp()
    op.run()
    
