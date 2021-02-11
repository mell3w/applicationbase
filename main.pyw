import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from tkinter import *
from tkinter import Canvas
import os
import shutil
from datetime import datetime





#------------------MONEY= Сдаёт
#------------------PRICE= Премия

class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()








    def init_main(self):
        toolbar = tk.Frame(bg='#d7d8e0', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X, expand = True)




        self.add_img = tk.PhotoImage(file='add.gif')
        btn_open_dialog = tk.Button(toolbar, text='Добавить заявку', command=self.open_dialog, bg='#d7d8e0', bd = 0, compound=tk.TOP, image=self.add_img)
        btn_open_dialog.pack(side=tk.LEFT)

        self.update_img = tk.PhotoImage(file='update.gif')
        btn_edit_dialog = tk.Button(toolbar, text='Редактировать', bg='#d7d8e0',bd=0, image=self.update_img, compound=tk.TOP, command=self.open_update_dialog)

        btn_edit_dialog.pack(side=tk.LEFT)

        self.delete_img = tk.PhotoImage(file='delete.gif')
        btn_delete = tk.Button(toolbar, text='Удалить', bg='#d7d8e0',bd=0, image=self.delete_img, compound=tk.TOP, command=self.delete_records)
        btn_delete.pack(side=tk.LEFT)

        self.search_img = tk.PhotoImage(file='search.gif')
        btn_search = tk.Button(toolbar, text='Поиск', bg='#d7d8e0', bd=0, image=self.search_img, compound=tk.TOP, command=self.open_search_dialog)
        btn_search.pack(side=tk.LEFT)

        self.shwrd = tk.PhotoImage(file='showreadyrecord.gif')
        btn_shwrd = tk.Button(toolbar, text='Выполненные', bg='#d7d8e0', bd=0, image=self.shwrd,
                              compound=tk.TOP,
                              command=self.view_ready_records)
        btn_shwrd.pack(side=tk.LEFT)



        self.ready_img=tk.PhotoImage(file='ready.gif')
        btn_ready = tk.Button(toolbar, text='Выполнено', bg='#d7d8e0', bd=0, image=self.ready_img, compound=tk.TOP, command=self.ready_check)
        btn_ready.pack(side=tk.LEFT)

        self.worker_img=tk.PhotoImage(file='man.gif')
        btn_worker = tk.Button(toolbar, text='Мастера', bg='#d7d8e0', bd=0, image=self.worker_img, compound=tk.TOP, command=self.worker)
        btn_worker.pack(side=tk.LEFT)


        self.sklad_img = tk.PhotoImage(file='sklad.gif')
        btn_sklad = tk.Button(toolbar, text='Учёт склада', bg='#d7d8e0', bd=0, image=self.sklad_img,compound=tk.TOP, command=self.open_sklad)
        btn_sklad.pack(side=tk.LEFT)

        self.finance_img=tk.PhotoImage(file='finance.gif')
        btn_finance = tk.Button(toolbar, text='Финансы', bg='#d7d8e0', bd=0, image=self.finance_img, compound=tk.TOP, command=self.open_finance)
        btn_finance.pack(side=tk.LEFT)

        self.sdal_img=tk.PhotoImage(file='sdal.gif')
        btn_sdal = tk.Button(toolbar, text='Сдал', bg='#d7d8e0', bd=0, image=self.sdal_img, compound=tk.TOP, command=self.sdal_true)
        btn_sdal.pack(side=tk.LEFT)

        self.refresh_img = tk.PhotoImage(file='refresh.gif')
        btn_refresh = tk.Button(toolbar, text='Обновить', bg='#d7d8e0', bd=0, image=self.refresh_img, compound=tk.TOP,
                                command=self.view_records)
        btn_refresh.pack(side=tk.LEFT)

        self.duble_img = tk.PhotoImage(file='copy.gif')
        btn_duble = tk.Button(toolbar, text='Дублировать', bg='#d7d8e0', bd=0, image=self.duble_img, compound=tk.TOP, command=self.duble_z)
        btn_duble.pack(side=tk.LEFT)

        self.print_img = tk.PhotoImage(file='print.gif')
        btn_print = tk.Button(toolbar, text='Печать', bg = '#d7d8e0', bd=0, image=self.print_img, compound=tk.TOP, command=self.print)
        btn_print.pack(side=tk.LEFT)

        self.txt_img = tk.PhotoImage(file='txt.gif')
        btn_txt = tk.Button(toolbar, text='Добавить в блокнот', bg = '#d7d8e0', bd=0, image=self.txt_img, compound=tk.TOP, command=self.vblock)
        btn_txt.pack(side=tk.LEFT)








        self.tree = ttk.Treeview(self, columns=('id','city','address','flat','tel','fio','description','money','price','other','master', 'data', 'status','closingdate','sdal'), height=40,show='headings')
        style = ttk.Style()
        style.configure("Treeview.Heading", font=(None, 10))


        self.tree.column('id', width=20, anchor=tk.CENTER)
        self.tree.column('city', width=150, anchor=tk.CENTER)
        self.tree.column('address', width=150, anchor=tk.CENTER)
        self.tree.column('flat', width=30, anchor=tk.CENTER)
        self.tree.column('tel', width=100, anchor=tk.CENTER)
        self.tree.column('fio', width=100, anchor=tk.CENTER)
        self.tree.column('description', width=250, anchor=tk.CENTER)
        self.tree.column('money', width=70, anchor=tk.CENTER)
        self.tree.column('price',width=70, anchor=tk.CENTER)
        self.tree.column('other', width=220, anchor=tk.CENTER)
        self.tree.column('master', width=100, anchor=tk.CENTER)
        self.tree.column('data',width=70, anchor=tk.CENTER)
        self.tree.column('status', width=80, anchor=tk.CENTER)
        self.tree.column('closingdate',width=100, anchor=tk.CENTER)
        self.tree.column('sdal', width=50, anchor=tk.CENTER)



        self.tree.heading('id', text = 'ID')
        self.tree.heading('city', text = 'Район')
        self.tree.heading('address',text='Адрес')
        self.tree.heading('flat', text='Квартира')
        self.tree.heading('tel', text='Телефон')
        self.tree.heading('fio', text='ФИО')
        self.tree.heading('description', text='Причины')
        self.tree.heading('money', text='Общая')
        self.tree.heading('price', text='Премия')
        self.tree.heading('other', text='Прочее')
        self.tree.heading('master', text='Мастер')
        self.tree.heading('data', text='Принята')
        self.tree.heading('status',text='Статус')
        self.tree.heading('closingdate',text='Закрыта')
        self.tree.heading('sdal', text='Сдал')
        self.tree.pack()

        self.tree.pack(side=tk.LEFT)
        scroll = tk.Scrollbar(self, command=self.tree.yview)
        scroll.pack(side=tk.LEFT, fill=tk.Y)
        self.tree.configure(yscrollcommand=scroll.set)




    def records(self, city, address, flat, tel, fio, description, money, price, other, master, keytm, keyrd, keymf, ykpseven, ykptwelve, status,mmyy, sdal):
        self.db.insert_data(city, address, flat, tel, fio, description, money, price, other, master, keytm, keyrd, keymf, ykpseven, ykptwelve, status, mmyy, sdal)
        self.view_records()


    def update_record(self, city, address, flat, tel, fio, description, money, price, other, master, keytm, keyrd, keymf, ykpseven, ykptwelve, status, mmyy, sdal):
        self.db.c.execute('''UPDATE mirodom SET city=?, address=?,flat=?,tel=?,fio=?, description=?, money=?, price=?, other=?, master=?, keytm=?, keyrd=?, keymf=?, ykpseven=?, ykptwelve=?, status=?, mmyy=?,sdal=? WHERE ID=?''',(city, address, flat, tel, fio, description, money, price, other, master, keytm, keyrd, keymf, ykpseven, ykptwelve, status, mmyy,sdal,  self.tree.set(self.tree.selection()[0], '#1'),))
        self.db.conn.commit()
        self.view_records()

    def view_records(self):
        self.db.c.execute('''SELECT id, city, address, flat, tel, fio, description, money, price, other, master,timestamp, status, closingdate, sdal  FROM mirodom''')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('','end', values = row) for row in self.db.c.fetchall()]

    def view_ready_records(self):
        self.db.c.execute('''SELECT id, city, address, flat, tel, fio, description, money, price, other, master,timestamp, status, closingdate,sdal FROM mirodom WHERE status='Выполнена' ''')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]




    def delete_records(self):
        choice = messagebox.askyesno("Удаление", "Вы действительно хотите удалить запись?")
        if choice:
            for selection_item in self.tree.selection():
                self.db.c.execute('''DELETE FROM mirodom WHERE id=?''', (self.tree.set(selection_item, '#1'),))
        self.db.conn.commit()
        self.view_records()



    def search_records(self, searchi):
        searching = ('%'+searchi + '%',)
        self.db.c.execute('''SELECT id, city, address, flat, tel, fio, description, money, price, other, master,timestamp, status, closingdate,sdal FROM mirodom WHERE description OR city OR address OR flat OR tel LIKE ?''', searching)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('','end',values=row) for row in self.db.c.fetchall()]

    def ready_check(self):
        cd = datetime.now()

        choice=messagebox.askyesno("Закрытие заявки", "Заявка будет отмечена как выполненная\nЖелаете продолжить?")
        if choice:
            for selection_item in self.tree.selection():
                self.db.c.execute('''UPDATE mirodom SET status='Выполнена'  WHERE id=?''', (self.tree.set(selection_item, '#1'),))
                deftime = datetime.now()
                self.db.c.execute('''UPDATE mirodom SET closingdate=? WHERE id=?''', (deftime, self.tree.set(selection_item, '#1'),))
        self.db.conn.commit()
        self.view_records()

    def sdal_true(self):
        sdalchoice=messagebox.askyesno("Деньги сданы", "Вы уже рассчиталисиь с матсером за эту заявку?\nЭти деньги больше не будут учитываться при подсчете финансов\nЖелаете продолжить?")
        if sdalchoice:
            for selection_item in self.tree.selection():
                self.db.c.execute('''UPDATE mirodom SET sdal='true'  WHERE id=?''', (self.tree.set(selection_item, '#1'),))
        self.db.conn.commit()
        self.view_ready_records()

    def duble_z(self):
        self.db.c.execute('''INSERT INTO mirodom (city, address , flat , tel , fio , description , money, price , other , master , keytm , keyrd , keymf , ykpseven , ykptwelve , timestamp , closingdate , status , mmyy , sdal) SELECT city, address , flat , tel , fio , description , money, price , other , master , keytm , keyrd , keymf , ykpseven , ykptwelve , timestamp , closingdate , status , mmyy , sdal FROM mirodom WHERE ID=?''',  self.tree.set(self.tree.selection()[0], '#1'), )
        self.view_records()

    def print(self):
        Print()


    def worker(self):
        Workers()

    def vblock(self):
        Vblock()


    def open_dialog(self):
        Child()


    def open_update_dialog(self):
        Update()

    def open_search_dialog(self):
        Search()


    def open_finance(self):
        Finance()


    def open_sklad(self):
        Sklad()



class Print(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.view = app
        self.db = db
        self.print_request()




    def init_child(self):
        self.title('Печать')
        self.geometry('650x600+300+200')
        self.resizable(False,False)
        self.text = Text(width=50, height=10)
        self.text.pack()


    def print_request(self):
        s= self.db.c.execute('''SELECT * FROM mirodom WHERE id=?''',
                          (self.view.tree.set(self.view.tree.selection()[0], '#1'),)).fetchone()


        a0 = str('\nНомер заявки: ')
        b0 = str( s[0])
        a1 = str("\nРайон: ")
        b1 = str(s[1])
        a2 = str("\nАдрес: ")
        b2 = str(s[2])
        a3 = str( "\nКваритра: ")
        b3 = str(s[3])
        a4 = str("\nТелефон: ")
        b4 = str(s[4])
        a5 = str( "\nФИО: ")
        b5 = str(s[5])
        a6 = str("\nПричины: ")
        b6 = str(s[6])
        a7 = str("\nОбщая стоимость заявки: ")
        b7 = str(s[7])
        a8 = str("\nПремия мастеру: ")
        b8 = str(s[8])
        a9 = str("\nПрочее: ")
        b9 = str(s[9])
        a10 = str("\nМастер: ")
        b10 = str(s[10])
        a11 = str("\nКлючи TM:")
        b11 = str(s[11])
        a12 = str("\nКлючи RD:")
        b12 = str(s[12])
        a13 = str("\nКлючи MF:")
        b13 = str(s[13])
        a14 = str("\nУПК-7: ")
        b14 = str(s[14])
        a15 = str("\nУПК-12: ")
        b15 = str(s[15])
        a16 = str("\nДата открытия: ")
        b16 = str(s[16])
        a17 =  str("\nСтатус заявки: ")
        b17 = str(s[17])
        a18 =  str("\nДата закрытия: ")
        b18 = str(s[18])
        a19 = str("\nММ/ГГ ")
        b19 = str(s[19])
        a20 = str("\nЗаявка расчитана: : ")
        b20 = str(s[20])
        p= a0+b0+a1+b1+a2+b2+a3+b3+a4+b4+a5+b5+a6+b6+a7+b7+a8+b8+a9+b9+a10+b10+a11+b11+a12+b12+a13+b13+a14+b14+a15+b15+a16+b16+a17+b17+a18+b18+a19+b19+a20+b20
        f1 = open("forprint.txt", 'w')
        f1.write(p)





        os.startfile("forprint.txt", "print")



class Vblock(tk.Toplevel):
    def __init__(self):
         super().__init__(root)
         #self.init_child()
         self.view = app
         self.db = db
         self.block_request()




    def init_child(self):
         self.title('Добавить в блокнот')
         self.geometry('650x600+300+200')
         self.resizable(False,False)
         self.text = Text(width=50, height=10)
         self.text.pack()
    def block_request(self):
        s= self.db.c.execute('''SELECT * FROM mirodom WHERE id=?''',
                          (self.view.tree.set(self.view.tree.selection(), '#1'),)).fetchone()


        otst = str('\n ')
        otstup  = str('\n=====================================================================================')
        otst2 = str('\n ')
        a0 = str('\nНомер заявки: ')
        b0 = str( s[0])
        a1 = str("\nРайон: ")
        b1 = str(s[1])
        a2 = str("\nАдрес: ")
        b2 = str(s[2])
        a3 = str( "\nКваритра: ")
        b3 = str(s[3])
        a4 = str("\nТелефон: ")
        b4 = str(s[4])
        a5 = str( "\nФИО: ")
        b5 = str(s[5])
        a6 = str("\nПричины: ")
        b6 = str(s[6])
        a7 = str("\nОбщая стоимость заявки: ")
        b7 = str(s[7])
        a8 = str("\nПремия мастеру: ")
        b8 = str(s[8])
        a9 = str("\nПрочее: ")
        b9 = str(s[9])
        a10 = str("\nМастер: ")
        b10 = str(s[10])
        a11 = str("\nКлючи TM:")
        b11 = str(s[11])
        a12 = str("\nКлючи RD:")
        b12 = str(s[12])
        a13 = str("\nКлючи MF:")
        b13 = str(s[13])
        a14 = str("\nУПК-7: ")
        b14 = str(s[14])
        a15 = str("\nУПК-12: ")
        b15 = str(s[15])
        a16 = str("\nДата открытия: ")
        b16 = str(s[16])
        a17 =  str("\nСтатус заявки: ")
        b17 = str(s[17])
        a18 =  str("\nДата закрытия: ")
        b18 = str(s[18])
        a19 = str("\nММ/ГГ ")
        b19 = str(s[19])
        a20 = str("\nЗаявка расчитана: : ")
        b20 = str(s[20])
        p= otst+otstup+ otst2+a0+b0+a1+b1+a2+b2+a3+b3+a4+b4+a5+b5+a6+b6+a7+b7+a8+b8+a9+b9+a10+b10+a11+b11+a12+b12+a13+b13+a14+b14+a15+b15+a16+b16+a17+b17+a18+b18+a19+b19+a20+b20
        f1 = open("forblock.txt", 'a')
        f1.write(p)
        f1.close()

        f = open("forblock.txt", "r")
        f.read()

    

class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()
        self.view = app

    def status_open(self, status):
        self.c.execute('''INSERT INTO mirodom (status) VALUES ('открыта')''')
        self.conn.commit()









    def init_child(self):
        self.title('Новая заявка')
        self.geometry('650x600+300+200')
        self.resizable(False,False)


        label_city=tk.Label(self, text='Район')
        label_city.place(x=50, y=50)
        label_address=tk.Label(self,text='Адрес')
        label_address.place(x=50, y = 80)
        label_flat=tk.Label(self, text='Квартира')
        label_flat.place(x=50,y=110)
        label_tel=tk.Label(self, text='Телефон')
        label_tel.place(x=50, y = 140)
        label_fio=tk.Label(self,text='ФИО')
        label_fio.place(x=50,y=170)
        label_description = tk.Label(self, text='Причины')
        label_description.place(x=50, y=200)
        label_money = tk.Label(self, text = 'Общая:')
        label_money.place(x=50, y =230)
        label_price = tk.Label(self, text='Премия:')
        label_price.place(x=50, y=260)
        label_other = tk.Label(self, text = 'Другое ')
        label_other.place(x=50, y=290)
        label_master = tk.Label(self, text='Мастер:')
        label_master.place(x=50, y=320)
        label_keytm=tk.Label(self,text='Ключ TM')
        label_keytm.place(x=50,y=350)
        label_keyrd = tk.Label(self, text = 'Ключ RD')
        label_keyrd.place(x=50, y=380)
        label_keymf = tk.Label(self, text='Ключ MF')
        label_keymf.place(x=50, y=410)
        label_ykpseven = tk.Label(self, text='УКП-7')
        label_ykpseven.place(x=50, y=440)
        label_ykptwelve = tk.Label(self, text='УКП-12')
        label_ykptwelve.place(x=50, y=470)
        label_status = tk.Label(self, text='Статус')
        label_status.place(x=50,y=500)
        label_mmyy = tk.Label(self, text='ММ/ГГ')
        label_mmyy.place(x=50, y = 530)





        self.entry_city = ttk.Combobox(self, values=[u'Петроградский',u'Фрунзенский',u'Всеволожск',u'Павлово',u'Приморский',u'ЖКК Заневка',u'Колтуши','д.Старая',u'Кузьмолово', u'Калининский',u'УК Охта-Сервис',u'пос.Разметелево',u'Щеглово', u'Янино'  ],width = 70)
        self.entry_city.place(x=200, y =50)

        self.entry_address=ttk.Entry(self,width = 70)
        self.entry_address.place(x=200, y=80)

        self.entry_flat=ttk.Entry(self,width = 70)
        self.entry_flat.place(x=200, y=110)

        self.entry_tel=ttk.Entry(self,width = 70)
        self.entry_tel.place(x=200, y=140)

        self.entry_fio=ttk.Entry(self,width = 70)
        self.entry_fio.place(x=200, y=170)

        self.entry_description= ttk.Entry(self,width = 70)
        self.entry_description.place(x=200, y=200)

        self.entry_money=ttk.Entry(self,width = 70)
        self.entry_money.insert(0, 0)
        self.entry_money.place(x=200,y=230)

        self.entry_price=ttk.Entry(self,width = 70)
        self.entry_price.insert(0, 0)
        self.entry_price.place(x=200,y=260)

        self.entry_other=ttk.Entry(self,width = 70)
        self.entry_other.place(x=200, y=290)

        self.entry_master=ttk.Entry(self,width = 70)
        self.entry_master.place(x=200, y=320)

        self.combobox = ttk.Combobox(self, values=[u'Николай М.', u'Андрей', u'Михаил', u'Герман', u'Николай С.', u'Илья', u'Дмитрий', u'Гена', u'Илья М.', u'Янина', u'Нина', u'Наталья', u'Владимир'],width = 67)
        self.combobox.current(0)
        self.combobox.place(x=200, y=320)

        self.entry_keytm = ttk.Entry(self, width=70)
        self.entry_keytm.insert(0, 0)
        self.entry_keytm.place(x=200, y=350)

        self.entry_keyrd = ttk.Entry(self, width=70)
        self.entry_keyrd.insert(0, 0)
        self.entry_keyrd.place(x=200, y=380)

        self.entry_keymf = ttk.Entry(self, width=70)
        self.entry_keymf.insert(0, 0)
        self.entry_keymf.place(x=200, y=410)

        self.entry_ykpseven = ttk.Entry(self, width=70)
        self.entry_ykpseven.insert(0, 0)
        self.entry_ykpseven.place(x=200, y=440)

        self.entry_ykptwelve = ttk.Entry(self, width=70)
        self.entry_ykptwelve.insert(0, 0)
        self.entry_ykptwelve.place(x=200, y=470)

        self.entry_status = ttk.Combobox(self, values=[u'Открыта', u'Выполнена'],width = 67)
        self.entry_status.current(0)
        self.entry_status.place(x=200, y=500)

        now = datetime.now()
        nowm = now.month
        nowy = now.year
        nowmy = str(nowm)
        nowyy= str(nowy)
        nownow= nowmy +'/'+ nowyy




        self.entry_mmyy = ttk.Entry(self, width=70)
        self.entry_mmyy.insert(INSERT, nownow)
        self.entry_mmyy.place(x=200,y=530)

        self.entry_sdal = ttk.Entry(self,width=1)
        self.entry_sdal.insert(0,'false')
        self.entry_sdal.place(x=200, y=700)








        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=570)



        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=220, y=570)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_city.get(),
                                                                       self.entry_address.get(),
                                                                       self.entry_flat.get(),
                                                                       self.entry_tel.get(),
                                                                       self.entry_fio.get(),
                                                                       self.entry_description.get(),
                                                                       self.entry_money.get(),
                                                                       self.entry_price.get(),
                                                                       self.entry_other.get(),
                                                                       self.combobox.get(),
                                                                       self.entry_keytm.get(),
                                                                       self.entry_keyrd.get(),
                                                                       self.entry_keymf.get(),
                                                                       self.entry_ykpseven.get(),
                                                                       self.entry_ykptwelve.get(),
                                                                       self.entry_status.get(),
                                                                       self.entry_mmyy.get(),
                                                                       self.entry_sdal.get()))
        self.btn_ok.bind('<Button-1>', lambda event: self.destroy(), add='+')
        self.grab_set()
        self.focus_set()









class Update(Child):
    def __init__(self):
        super().__init__()
        self.init_edit()
        self.db = db
        self.view = app
        self.default_data()

    def init_edit(self):
        self.title('Редактировать позицию')
        btn_edit = ttk.Button(self, text='Редактировать')
        btn_edit.place(x=205, y=570)
        btn_edit.bind('<Button-1>',  lambda event: self.view.update_record(self.entry_city.get(),
                                                                           self.entry_address.get(),
                                                                           self.entry_flat.get(),
                                                                           self.entry_tel.get(),
                                                                           self.entry_fio.get(),
                                                                           self.entry_description.get(),
                                                                           self.entry_money.get(),
                                                                           self.entry_price.get(),
                                                                           self.entry_other.get(),
                                                                           self.combobox.get(),
                                                                           self.entry_keytm.get(),
                                                                           self.entry_keyrd.get(),
                                                                           self.entry_keymf.get(),
                                                                           self.entry_ykpseven.get(),
                                                                           self.entry_ykptwelve.get(),
                                                                           self.entry_status.get(),
                                                                           self.entry_mmyy.get(),
                                                                           self.entry_sdal.get()))
        btn_edit.bind('<Button-1>', lambda event: self.destroy(), add='+')
        self.btn_ok.destroy()


    def default_data(self):
        self.db.c.execute('''SELECT * FROM mirodom WHERE id=?''', (self.view.tree.set(self.view.tree.selection()[0],'#1'),))
        row = self.db.c.fetchone()
        self.entry_city.insert(0, row[1])
        if row[1] == 'Петроградский':
            self.entry_city.current(0)
        elif row[1] == 'Фрунзенский':
            self.entry_city.current(1)
        elif row[1] == 'Всеволжск':
            self.entry_city.current(2)
        elif row[1] == 'Павлово':
            self.entry_city.current(3)
        elif row[1] == 'Приморский':
            self.entry_city.current(4)
        elif row[1] == 'ЖКК Заневка':
            self.entry_city.current(5)
        elif row[1]=='Колтуши':
            self.entry_city.current(6)
        elif row[1]=='д.Старая':
            self.entry_city.current(7)
        elif row[1]=='Кузьмолово':
            self.entry_city.current(8)
        elif row[1]=='Калининский':
            self.entry_city.current(9)
        elif row[1]=='УК Охта-Сервис':
            self.entry_city.current(10)
        elif row[1]=='пос.Разметелево':
            self.entry_city.current(11)
        elif row[1]=='Щеглово':
            self.entry_city.current(12)
        elif row[1]=='Янино':
            self.entry_city.current(13)
        self.entry_address.insert(0,row[2])
        self.entry_flat.insert(0, row[3])
        self.entry_tel.insert(0, row[4])
        self.entry_fio.insert(0, row[5])
        self.entry_description.insert(0, row[6])
        self.entry_money.delete(0, END)
        self.entry_money.insert(0, row[7])
        self.entry_price.delete(0, END)
        self.entry_price.insert(0, row[8])
        self.entry_other.insert(0,row[9])
        if row[10] == 'Николай М.':
            self.combobox.current(0)
        elif row[10] == 'Андрей':
            self.combobox.current(1)
        elif row[10] == 'Михаил':
            self.combobox.current(2)
        elif row[10] == 'Герман':
            self.combobox.current(3)
        elif row[10] == 'Николай С.':
            self.combobox.current(4)
        elif row[10] == 'Илья':
            self.combobox.current(5)
        elif row[10] == 'Дмитрий':
            self.combobox.current(6)
        elif row[10] == 'Гена':
            self.combobox.current(7)
        elif row[10] == 'Илья М.':
            self.combobox.current(8)
        elif row[10] == 'Янина':
            self.combobox.current(9)
        elif row[10] == 'Нина':
            self.combobox.current(10)
        elif row[10] == 'Наталья':
            self.combobox.current(11)
        elif row[10] == 'Владимир':
            self.combobox.current(12)
        self.entry_keytm.delete(0, END)
        self.entry_keytm.insert(0, row[11])
        self.entry_keyrd.delete(0, END)
        self.entry_keyrd.insert(0, row[12])
        self.entry_keymf.delete(0, END)
        self.entry_keymf.insert(0, row[13])
        self.entry_ykpseven.delete(0, END)
        self.entry_ykpseven.insert(0, row[14])
        self.entry_ykptwelve.delete(0, END)
        self.entry_ykptwelve.insert(0, row[15])
        if row[17] == 'Открыта':
            self.entry_status.current(0)
        elif row[17] == 'Выполнена':
            self.entry_status.current(1)
        self.entry_mmyy.delete(0, END)
        self.entry_mmyy.insert(0,row[19])
        self.entry_sdal.delete(0, END)
        self.entry_sdal.insert(0,row[20])





class Search(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_search()
        self.view = app




    def init_search(self):
        self.title('Поиск')
        self.geometry('400x220+400+300')
        self.resizable(True, True)

        self.focus_set()

        label_search=tk.Label(self, text='Поиск')
        label_search.place(x=50, y=50)

        self.entry_search = ttk.Entry(self)
        self.entry_search.place(x=100, y=50, width=200)


        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=200, y=100)

        btn_ok = ttk.Button(self, text='Поиск')
        btn_ok.place(x=100, y=100)
        btn_ok.bind('<Button-1>', lambda event: self.view.search_records(self.entry_search.get()))
        btn_ok.bind('<Button-1>', lambda event: self.destroy(), add='+')


class Workers(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.view = app
        self.db = db
        self.geometry('800x420+400+300')

        label_mast = tk.Label(self, text='Мастер')
        label_mast.place(x=20, y=30)

        self.entry_mast = ttk.Combobox(self,
                                       values=[u'Николай М.', u'Андрей', u'Михаил', u'Герман', u'Николай С.', u'Илья',
                                               u'Дмитрий', u'Гена', u'Илья М.', u'Янина', u'Нина', u'Наталья',
                                               u'Владимир'])
        self.entry_mast.current(0)
        self.entry_mast.place(x=20, y=50)

        label_stat = tk.Label(self, text='Статус')
        label_stat.place(x=170, y=30)

        self.entry_stat = ttk.Combobox(self, values=[u'Открыта', u'Выполнена'])
        self.entry_stat.current(0)
        self.entry_stat.place(x=170, y=50)

        self.btn_finance = tk.Button(self, text='Показать')
        self.btn_finance.place(x=250, y=300)
        self.btn_finance.bind('<Button-1>', lambda event: self.wstat())

    def wstat(self):
        con = self.db.c.execute('''SELECT id, city, address, flat, tel, fio, description, money, price, other, master,timestamp, status, closingdate, sdal FROM mirodom WHERE master=? AND status=? ''',
                            (self.entry_mast.get(), self.entry_stat.get()), ).fetchall()
        [self.view.tree.delete(i) for i in self.view.tree.get_children()]
        [self.view.tree.insert('', 'end', values=row) for row in con]

    def init_worker(self):
        self.title('Настроить показ мастеров')
        self.resizable(True,True)
        self.var1=BooleanVar()
        self.var1.set(1)







#======================================================================================================================#
#------------------------------------------------FINANCE---------------------------------------------------------------#
#======================================================================================================================#







class Finance(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.view = app
        self.db = db
        self.geometry('800x420+400+300')

        label_masf = tk.Label(self, text='Мастер')
        label_masf.place(x=20, y=30)

        self.entry_masf = ttk.Combobox(self, values= [u'Николай М.', u'Андрей', u'Михаил', u'Герман', u'Николай С.', u'Илья', u'Дмитрий', u'Гена', u'Илья М.', u'Янина', u'Нина', u'Наталья', u'Владимир'])
        self.entry_masf.current(0)
        self.entry_masf.place(x=20, y=50)

        label_perf = tk.Label(self, text='Период')
        label_perf.place(x=170, y=30)

        self.entry_perf = ttk.Combobox(self, values= [u'10/2020',u'11/2020',u'12/2020',u'1/2021',u'2/2021',u'3/2021',u'4/2021',u'5/2021',u'6/2021',u'7/2021',u'8/2021',u'9/2021',u'10/2021',u'11/2021',u'12/2021',u'1/2022',u'2/2022',u'3/2022',u'4/2022',u'5/2022',u'6/2022',u'7/2022',u'8/2022',u'9/2022',u'10/2022',u'11/2022',u'12/2022'])
        self.entry_perf.current(0)
        self.entry_perf.place(x=170,y=50)

        self.btn_finance = tk.Button(self, text='Рассчитать')
        self.btn_finance.place(x=250, y=300)
        self.btn_finance.bind('<Button-1>', lambda event: self.finance_ras())


#======================================================================================================================#


    def finance_ras(self):
        con = self.db.c.execute('''SELECT money FROM mirodom WHERE master=? AND mmyy=? AND status='Выполнена' AND sdal='false' ''', (self.entry_masf.get(), self.entry_perf.get()),)
        result=con.fetchall()
        c=0
        for x in result:
            c=sum(i[0] for i in result)
        label_ras=ttk.Label(self, text='Общая = '+ str(c))
        label_ras.place(x=20, y=150)

        con2 = self.db.c.execute('''SELECT price FROM mirodom WHERE master=? AND mmyy=? AND status='Выполнена' AND sdal='false' ''',(self.entry_masf.get(),self.entry_perf.get()),)
        result2 = con2.fetchall()
        y=0
        for x in result2:
            y = sum(i[0] for i in result2)
        label_ras2 = ttk.Label(self, text='Премия = '+str(y))
        label_ras2.place(x=170, y=150)

        sd= c-y

        label_sd = ttk.Label(self, text='Сдаёт ='+str(sd))
        label_sd.place(x=320, y=150)





#======================================================================================================================#


class Sklad(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_sklad()
        self.view = app
        self.db = db





    def init_sklad(self):
        self.title('Учёт склада')
        self.geometry('400x450+300+200')
        self.resizable(False,False)

        label_mas = tk.Label(self, text='Мастер')
        label_mas.place(x=20, y=30)

        self.entry_mas = ttk.Combobox(self,values= [u'Николай М.', u'Андрей', u'Михаил', u'Герман', u'Николай С.', u'Илья', u'Дмитрий', u'Гена', u'Илья М.', u'Янина', u'Нина', u'Наталья', u'Владимир'])
        self.entry_mas.current(0)
        self.entry_mas.place(x=20, y=50)



        label_period = tk.Label(self, text='Период')
        label_period.place(x=170, y=30)


        self.entry_period = ttk.Combobox(self, values=[u'10/2020',u'11/2020',u'12/2020',u'01/2021',u'02/2021',u'03/2021',u'04/2021',u'05/2021',u'06/2021',u'07/2021',u'08/2021',u'09/2021',u'10/2021',u'11/2021',u'12/2021',u'01/2022',u'02/2022',u'03/2022',u'04/2022',u'05/2022',u'06/2022',u'07/2022',u'08/2022',u'09/2022',u'10/2022',u'11/2022',u'12/2022'])
        self.entry_period.current(0)
        self.entry_period.place(x=170,y=50)

        masterget = self.entry_mas.get()
        periodget = self.entry_period.get()

        label_tm = tk.Label(self, text='Ключи ТМ')
        label_tm.place(x=20, y=90)

        self.btn_tm = ttk.Button(self, text='Посчитать')
        self.btn_tm.place(x=320, y=90)
        self.btn_tm.bind('<Button-1>', lambda event:self.tm())

#=========================================================================

        label_rd = tk.Label(self, text='Ключи RD')
        label_rd.place(x=20, y=120)

        self.btn_rd = ttk.Button(self, text='Посчитать')
        self.btn_rd.place(x=320, y=120)
        self.btn_rd.bind('<Button-1>', lambda event: self.rd())

#=========================================================================

        label_mf = tk.Label(self, text='Ключи MF')
        label_mf.place(x=20, y=150)

        self.btn_mf = ttk.Button(self, text='Посчитать')
        self.btn_mf.place(x=320, y=150)
        self.btn_mf.bind('<Button-1>', lambda event: self.mf())

#==========================================================================

        label_ykpseven = tk.Label(self, text='УКП - 7')
        label_ykpseven.place(x=20, y=180)

        self.btn_ykpseven = ttk.Button(self, text='Посчитать')
        self.btn_ykpseven.place(x=320, y=180)
        self.btn_ykpseven.bind('<Button-1>', lambda event: self.ykpseven())

#===========================================================================

        label_ykptwelve = tk.Label(self, text='УКП - 12')
        label_ykptwelve.place(x=20, y=210)

        self.btn_ykptwelve = ttk.Button(self, text='Посчитать')
        self.btn_ykptwelve.place(x=320, y=210)
        self.btn_ykptwelve.bind('<Button-1>', lambda event: self.ykptwelve())

#==========================================================================







    def tm(self):
        con = self.db.c.execute('''SELECT keytm FROM mirodom WHERE master=? AND mmyy=?''', (self.entry_mas.get(), self.entry_period.get()),)
        result = con.fetchall()
        c = 0
        for x in result:
            c = sum(i[0] for i in result)
        label_tm = ttk.Label(self, text= str(c))
        label_tm.place(x=170, y=90)

    def rd(self):
        con = self.db.c.execute('''SELECT keyrd FROM mirodom WHERE master=? AND mmyy=?''', (self.entry_mas.get(), self.entry_period.get()),)
        result = con.fetchall()
        c = 0
        for x in result:
            c = sum(i[0] for i in result)
        label_tm = ttk.Label(self, text= str(c))
        label_tm.place(x=170, y=120)

    def mf(self):
        con = self.db.c.execute('''SELECT keymf FROM mirodom WHERE master=? AND mmyy=?''', (self.entry_mas.get(), self.entry_period.get()),)
        result = con.fetchall()
        c = 0
        for x in result:
            c = sum(i[0] for i in result)
        label_tm = ttk.Label(self, text= str(c))
        label_tm.place(x=170, y=150)

    def ykpseven(self):
        con = self.db.c.execute('''SELECT ykpseven FROM mirodom WHERE master=? AND mmyy=?''', (self.entry_mas.get(), self.entry_period.get()),)
        result = con.fetchall()
        c = 0
        for x in result:
            c = sum(i[0] for i in result)
        label_tm = ttk.Label(self, text= str(c))
        label_tm.place(x=170, y=180)

    def ykptwelve(self):
        con = self.db.c.execute('''SELECT ykptwelve FROM mirodom WHERE master=? AND mmyy=?''', (self.entry_mas.get(), self.entry_period.get()),)
        result = con.fetchall()
        c = 0
        for x in result:
            c = sum(i[0] for i in result)
        label_tm = ttk.Label(self, text= str(c))
        label_tm.place(x=170, y=210)








#=============================================================================================================================================================

class DB:
    def __init__(self):
        self.conn = sqlite3.connect('mirodom.db')
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS mirodom (id integer primary key, city text, address text,flat  text, tel integer, fio text, description text, money int, price int, other text, master text, keytm int, keyrd int, keymf int, ykpseven int, ykptwelve int, timestamp datetime default CURRENT_TIMESTAMP, status text, closingdate, mmyy text, sdal text)''')
        self.conn.commit()

    def insert_data(self, city, address, flat, tel, fio, description, money, price, other, master, keytm, keyrd, keymf, ykpseven, ykptwelve, status, mmyy,sdal):
        self.c.execute('''INSERT INTO mirodom(city, address, flat, tel, fio, description, money, price, other, master, keytm, keyrd, keymf, ykpseven, ykptwelve, status, mmyy, sdal) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(city, address, flat, tel, fio, description, money, price, other, master, keytm, keyrd, keymf, ykpseven, ykptwelve, status, mmyy, sdal))
        self.conn.commit()


        


if __name__=="__main__":
    root = tk.Tk()
    db = DB()
    #bd=BD()
    app = Main(root)
    app.pack()
    root.title("МИРОДОМ")
    root.geometry("1575x600+400+200")
    root.resizable(True, True)
    root.mainloop()
