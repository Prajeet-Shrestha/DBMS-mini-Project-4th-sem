from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
import mysql.connector
import numpy as np

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="adminroot"
    )
cursor = db.cursor()
cursor.execute("USE auto_manufacture_management_system;")
cursor.execute("SELECT * FROM employee;")
employee_attr=[]
employee_data= []
for i in cursor:
    employee_data.append(i)
cursor.execute("DESC employee;")
for i in cursor:
    employee_attr.append(i[0])

Builder.load_string('''
<DataTable>:
    id: main_win
    RecycleView:
        viewclass: 'CustLabel'
        id: table_floor
        RecycleGridLayout:
            id: table_floor_layout
            cols: 5
            default_size: (None,250)
            default_size_hint: (1,None)
            size_hint_y: None
            height: self.minimum_height
            spacing: 5
            
<CustLabel@Label>:
    bcolor: (1,1,1,1)
    canvas.before:
        Color:
            rgba: root.bcolor
        Rectangle:
            size: self.size
            pos: self.pos
    ''')
class DataTable(BoxLayout):
    def __init__(self,row_data='',col_data='',**kwargs):
        super().__init__(**kwargs)
        table_data=[]
        col_titles = col_data
        self.colums = len(col_titles)
        row_len = len(row_data)
        for t in col_titles:
            table_data.append({'text':str(t),'size_hint_y': None,'height':30,'bcolor':(.02,.45,.45,1)})
        for r in range(row_len):
            for t in range(len(col_titles)):
                table_data.append({'text':str(row_data[r][t]),'size_hint_y': None,'height':30,'bcolor':(.02,.25,.25,1)})

        self.ids.table_floor_layout.cols = self.colums
        self.ids.table_floor.data = table_data

class DataTableApp(App):
    def build(self):
        return DataTable()

if __name__ == "__main__":
    op = DataTableApp()
    op.run()
    
