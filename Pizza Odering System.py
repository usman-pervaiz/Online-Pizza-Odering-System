from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import ttk
#import tkinter as tk
import sqlite3
import csv




conn=sqlite3.connect("Pizza System.db")
c=conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS order_details(
            Customer_Name text,
            Address text,
            Phone_No integer,
            Pizza_Types text,
            Pizza_Quantity integer,
            Pizza_Size text,
            Pizza_Prise integer
            )""")

class Pizza_Odering_System:
    def __init__(self):
        self.root=Tk()
        self.root.title("Pizza Odering System")
        self.root.geometry("620x400")

    def Stock(self):
        top=Toplevel()
        top.title("Menu")
        top.geometry("1120x1200")

        title_menu="Welcome may you love your menu"
        title_Menu_Label=Label(top,text=title_menu,font='Helvetica 18 bold')
        title_Menu_Label.grid(row=0,column=1,columnspan=4,padx=(0,300))

        #Chicken Tikka Menu
        Chicken_tika_img=ImageTk.PhotoImage(Image.open("image/Chicken_tika.PNG"))
        Chicken_tika_label=Label(top,image=Chicken_tika_img)
        Chicken_tika_label.grid(row=1,column=0)
        menu_Chicken_tika="""
                Price:
                    Small  = 300
                    Medium = 500
                    Large  = 800"""
                        
        Chicken_tika_prise_label=Label(top,text=menu_Chicken_tika,font=2)
        Chicken_tika_prise_label.grid(row=2,column=0,padx=(0,100))

        #Chicken Fajita Menu
        Chicken_Fajita_img=ImageTk.PhotoImage(Image.open("image/Chicken_fatija.PNG"))
        Chicken_Fajita_label=Label(top,image=Chicken_Fajita_img)
        Chicken_Fajita_label.grid(row=1,column=1)
        menu_Chicken_tika="""
                Price:
                    Small  = 350
                    Medium = 550
                    Large  = 850"""
                        
        Chicken_tika_prise_label=Label(top,text=menu_Chicken_tika,font=2)
        Chicken_tika_prise_label.grid(row=2,column=1,padx=(0,100))

        #Creamy Melt Menu
        Creamy_Melt_img=ImageTk.PhotoImage(Image.open("image/Cremy melt.PNG"))
        Creamy_Melt_label=Label(top,image=Creamy_Melt_img)
        Creamy_Melt_label.grid(row=1,column=3)
        menu_Creamy_Melt="""
                Price:
                    Small  = 320
                    Medium = 520
                    Large  = 820"""
                        
        Creamy_Melt_prise_label=Label(top,text=menu_Creamy_Melt,font=2)
        Creamy_Melt_prise_label.grid(row=2,column=3,padx=(0,100))

        #Chicken Tikka Supreme Menu
        Chicken_tika_Supreme_img=ImageTk.PhotoImage(Image.open("image/Chicken_tika_supreme.PNG"))
        Chicken_tika_Supreme_label=Label(top,image=Chicken_tika_Supreme_img)
        Chicken_tika_Supreme_label.grid(row=1,column=4)
        menu_Chicken_tika_Supreme="""
                Price:
                    Small  = 380
                    Medium = 580
                    Large  = 880"""
                        
        Chicken_tika_Supreme_prise_label=Label(top,text=menu_Chicken_tika_Supreme,font=2)
        Chicken_tika_Supreme_prise_label.grid(row=2,column=4,padx=(0,50))

        #Afghani Tikka Menu
        Afghani_Tikka_img=ImageTk.PhotoImage(Image.open("image/Afgani_tikka.PNG"))
        Afghani_Tikka_label=Label(top,image=Afghani_Tikka_img)
        Afghani_Tikka_label.grid(row=3,column=0,pady=(50,0))
        menu_Afghani_Tikka="""
                Price:
                    Small  = 420
                    Medium = 520
                    Large  = 920"""
                        
        Chicken_tika_prise_label=Label(top,text=menu_Afghani_Tikka,font=2)
        Chicken_tika_prise_label.grid(row=4,column=0,padx=(0,100))

        #Seekh Kebab Overload Menu
        Seekh_Kebab_Overload_img=ImageTk.PhotoImage(Image.open("image/Sikkh kawab overload.PNG"))
        Seekh_Kebab_Overload_label=Label(top,image=Seekh_Kebab_Overload_img)
        Seekh_Kebab_Overload_label.grid(row=3,column=1,pady=(50,0))
        menu_Seekh_Kebab_Overload="""
                Price:
                    Small  = 400
                    Medium = 500
                    Large  = 800"""
                        
        Seekh_Kebab_Overload_prise_label=Label(top,text=menu_Seekh_Kebab_Overload,font=2)
        Seekh_Kebab_Overload_prise_label.grid(row=4,column=1,padx=(0,100))

        #BBQ Buzz Menu
        BBQ_Buzz_img=ImageTk.PhotoImage(Image.open("image/BBQ Buzz.PNG"))
        BBQ_Buzz_label=Label(top,image=BBQ_Buzz_img)
        BBQ_Buzz_label.grid(row=3,column=3,pady=(50,0))
        menu_Chicken_tika="""
                Price:
                    Small  = 350
                    Medium = 550
                    Large  = 850"""
                        
        Chicken_tika_prise_label=Label(top,text=menu_Chicken_tika,font=2)
        Chicken_tika_prise_label.grid(row=4,column=3,padx=(0,100))

        #Behari Menu
        Behari_img=ImageTk.PhotoImage(Image.open("image/Behari.PNG"))
        Behari_label=Label(top,image=Behari_img)
        Behari_label.grid(row=3,column=4,pady=(50,0))
        menu_Chicken_tika="""
                Price:
                    Small  = 300
                    Medium = 500
                    Large  = 800"""
                        
        Chicken_tika_prise_label=Label(top,text=menu_Chicken_tika,font=2)
        Chicken_tika_prise_label.grid(row=4,column=4,padx=(0,50))




        close_menu_btn=Button(top,text="Close Menu",width=30,borderwidth=4,font=2,command=top.destroy)
        close_menu_btn.grid(row=5,column=0,columnspan=4,padx=(300,0),pady=(10,0))



        
        top.mainloop()

        

    def CustomerWants(self):
        global Pizza_Flaver_lst
        Pizza_Flaver_lst=["Chicken Tikka","Chicken Fajita","Creamy Melt",
                          "Chicken Tikka Supreme","Afghani Tikka",
                          "Seekh Kebab Overload","BBQ Buzz","Behari"]
        global pizza_Size_list
        pizza_Size_list=["Small","Medium","Large"]

        
        '''Pizza_Flaver_lst_label=""
        for i in range(len(Pizza_Flaver_lst)//2):
            Pizza_Flaver_lst_label += Pizza_Flaver_lst[i] +" \t" +Pizza_Flaver_lst[i+1] + "\n"'''

        flaver_title_label=Label(self.root,text='Pizza Odering List',font='Helvetica 18 bold')
        flaver_title_label.grid(row=0,column=1,columnspan=2)
        
        global clicked
        clicked=StringVar()
        clicked.set(Pizza_Flaver_lst[0])
        Suggestion_Falver_Label=Label(self.root,text="Which Pizza Falver do you want:")
        Suggestion_Falver_Label.grid(row=2,column=0,padx=(10,0),pady=10)
        Flaver_drop=OptionMenu(self.root,clicked,*Pizza_Flaver_lst)
        Flaver_drop.grid(row=2,column=1,padx=5,pady=10,ipadx=40)
        
        
        global Size_of_pizza
        Size_of_pizza=StringVar()
        Size_of_pizza.set(pizza_Size_list[0])
        pizza_size_label=Label(self.root,text="Select your pizza size:")
        pizza_size_label.grid(row=3,column=0,padx=(10,0))
        Size_dropdown=OptionMenu(self.root,Size_of_pizza,*pizza_Size_list)
        Size_dropdown.grid(row=3,column=1,padx=5,pady=10,ipadx=40)
        
        
        Welcome_label="""Hello Welcome to our oline Pizza
Delivery System may you enjoy our delicius
pizza and enjoy your time"""
        pizza_list_label=Label(self.root,text=Welcome_label,font=14)
        pizza_list_label.grid(row=1,column=1)
        
        CustomerWants_button=Button(self.root,text="Select Flaver",width=30,borderwidth=4,command=self.CustomerDetail)
        CustomerWants_button.grid(row=4,column=1,columnspan=2,padx=5)

        Avability_stock_bth=Button(self.root,text="Open Menu",width=30,borderwidth=4,command=self.Stock)
        Avability_stock_bth.grid(row=5,column=1,columnspan=2,padx=5,pady=5)

        Security_head_bth=Button(self.root,text="Adminstrater Button",width=30,borderwidth=4,command=self.View)
        Security_head_bth.grid(row=6,column=1,columnspan=2,padx=5,pady=5)
    def csv_save(self):
        head=["Customer Name","Address","Phone Number","Pizza Name","Quantity","Size","Price","ID"]
        with open('Pizza Customers.csv','a') as i:
            z=csv.writer(i,dialect='excel')
            z.writerow(head)
        with open('Pizza Customers.csv','a',newline='') as f:
            w=csv.writer(f,dialect='excel')
            for x in records:
                w.writerow(x)
    def Dataview(self):
        if (User_Entry.get()== "18B-006-CS" or User_Entry.get()== "18b-006-cs") and (Password_Entry.get()=="12345678"):
            top_pop=Toplevel()
            top_pop.title("Order Data")
            top_pop.geometry("1390x650")
            self.Quary()
            frm=Frame(top_pop)
            frm.grid(row=0,column=0,columnspan=6)#side=tk.LEFT,padx=20)

            tv=ttk.Treeview(frm,column=(1,2,3,4,5,6,7),show="headings",height=len(records))
            tv.pack()
            tv.heading(1,text="Customer Name")
            tv.heading(2,text="Address")
            tv.heading(3,text="Phone Number")
            tv.heading(4,text="Pizza Name")
            tv.heading(5,text="Quantity")
            tv.heading(6,text="Size")
            tv.heading(7,text="Price")

            #for i in range(len(records)):
            for record in records:
                tv.insert('','end',values=record)
            close_button=Button(top_pop,text='Close',width=20,borderwidth=4,command=top_pop.destroy)
            close_button.grid(row=1,column=0,padx=(500,0))
            csv_button=Button(top_pop,text="Save To Excel",width=20,borderwidth=4,command=self.csv_save)
            csv_button.grid(row=1,column=1,padx=(0,500))
            
            '''#print(records)

            title_top="Customer Name\t\t\tAddress\t\t\tPhone Number\t\t\tPizza Name\t\t\tQuantity\t\t\tSize\t\t\tPrice"
            title_label_top=Label(top_pop,text=title_top).pack()
            Data_records=""
            for i in records:
                Data_records+=i[0] +"\t\t\t"+i[1] +"\t\t\t "+str(i[2]) +"\t\t\t"+i[3]+"\t\t\t"+str(i[4]) +"\t\t\t"+i[5]+ "\t\t\t"+str(i[6])+"\n"
            Label(top_pop,text=Data_records).pack()'''
            window.destroy()
            window.mainloop()
        else:
            top_pop2=Toplevel()
            top_pop2.title("Error")
            top_pop2.geometry("280x100")
            mylabel=Label(top_pop2,text="You may enter wrong Password or User Name")
            mylabel.pack()
            btn=Button(top_pop2,text="OK",width=20,borderwidth=4,command=top_pop2.destroy)
            btn.pack(pady=(10,0))
            User_Entry.delete(0,END)
            Password_Entry.delete(0,END)
            
    def View(self):
        global window
        window=Tk()
        window.title("Adminstrater Window")
        window.geometry("400x160")

        title_label=Label(window,text="Admistrater Info",font=14)
        title_label.grid(row=0,column=1,columnspan=2)
        global User_Entry
        User_Entry=Entry(window,width=30)
        User_Entry.grid(row=1,column=1)
        User_Entry_label=Label(window,text="Enter your userName:")
        User_Entry_label.grid(row=1,column=0)

        global Password_Entry
        Password_Entry=Entry(window,width=30)
        Password_Entry.grid(row=2,column=1)
        Password_Entry_label=Label(window,text="Enter Admistration password:")
        Password_Entry_label.grid(row=2,column=0)

        btn_logic=Button(window,text="Login",width=20,borderwidth=4,command=self.Dataview)
        btn_logic.grid(row=3,column=0,columnspan=2,pady=(10,0))
        

        
    def CustomerDetailData(self):
        self.PizzaPriceSet()
        conn=sqlite3.connect("Pizza System.db")
        c=conn.cursor()
        c.execute("INSERT INTO order_details VALUES(:c_name,:adr,:Ph,:type,:Qu,:size,:prise)",
                  {
                      'c_name':CustomerName.get(),
                      'adr':Address.get(),
                      'Ph':PhoneNo.get(),
                      'type':clicked.get(),
                      'Qu':Quantity.get(),
                      'size':Size_of_pizza.get(),
                      'prise':prize_set
                      }
                  )
        conn.commit()
        conn.close()
        
        #CustomerName.delete(0,END)
        #Address.delete(0,END)
        #PhoneNo.delete(0,END)
        #Quantity.delete(0,END)
        self.OrderDeatil()
        app.destroy()
        
        
        
    def CustomerDetail(self):
        global app
        app=Tk()
        app.title("Customer Detail")
        app.geometry("410x190")

        global CustomerName
        global Address
        global PhoneNo
        global Quantity
        
        CustomerName=Entry(app,width=30)
        CustomerName.grid(row=0,column=1,padx=20,pady=(10,0))
        Address=Entry(app,width=30)
        Address.grid(row=1,column=1,padx=20)
        PhoneNo=Entry(app,width=30)
        PhoneNo.grid(row=2,column=1,padx=20)
        Quantity=Entry(app,width=30)
        Quantity.grid(row=3,column=1,padx=20)
        
        CustomerNameLabel=Label(app,text="Enter your name:")
        CustomerNameLabel.grid(row=0,column=0,pady=(10,0))
        AddressLabel=Label(app,text="Enter your Address:")
        AddressLabel.grid(row=1,column=0)
        PhoneNoLabel=Label(app,text="Enter your Phone No:")
        PhoneNoLabel.grid(row=2,column=0)
        QuantityLabel=Label(app,text="How many Pizza do you want:")
        QuantityLabel.grid(row=3,column=0)
        
        
        
        
        CustomerDetail_button=Button(app,text="Order",width=30,borderwidth=4,command=self.CustomerDetailData)
        CustomerDetail_button.grid(row=4,column=1,columnspan=2,padx=5,pady=(10,0))

        
        
    
    def PizzaPriceSet(self):
        if Size_of_pizza.get()=="Small":
            Pizza_Flaver_Prise_lst={"Chicken Tikka":300,"Chicken Fajita":350,"Creamy Melt":320,
                              "Chicken Tikka Supreme":380,"Afghani Tikka":420,
                              "Seekh Kebab Overload":400,"BBQ Buzz":350,"Behari":360}
        elif Size_of_pizza.get()=="Medium":
            Pizza_Flaver_Prise_lst={"Chicken Tikka":500,"Chicken Fajita":550,"Creamy Melt":520,
                              "Chicken Tikka Supreme":580,"Afghani Tikka":520,
                              "Seekh Kebab Overload":500,"BBQ Buzz":550,"Behari":560}
        elif Size_of_pizza.get()=="Large":
            Pizza_Flaver_Prise_lst={"Chicken Tikka":800,"Chicken Fajita":850,"Creamy Melt":820,
                              "Chicken Tikka Supreme":880,"Afghani Tikka":920,
                              "Seekh Kebab Overload":800,"BBQ Buzz":850,"Behari":860}
        #print(Quantity.get())
        #print(Pizza_Flaver_Prise_lst[clicked.get()])
        global prize_set
        prize_set=Pizza_Flaver_Prise_lst[clicked.get()]*int(Quantity.get())
    def Delete_Order(self):
        self.Quary()
        conn=sqlite3.connect("Pizza System.db")
        c=conn.cursor()
        c.execute("DELETE from order_details WHERE oid="+str(records[-1][-1]))
        delete_response=messagebox.showinfo("Your your order is deleted","Thankyou")
        conn.commit()
        top.destroy()
        top.mainloop()
        
        
    def Quary(self):
        conn=sqlite3.connect("Pizza System.db")
        c=conn.cursor()
        c.execute("SELECT *,oid FROM order_details")
        global records
        records=c.fetchall()
        conn.commit()
        conn.close()
        #print(records[-1][-1])

        
            
        

    '''def update_order(self):
        pass
    
    def edit_detail(self):
        global editor
        editor=Tk()
        editor.title("Update Order")
        editor.geometry("400x400")


        self.Quary()
        
        
        #Create Global Variable for text box names and Checkbox
        global CustomerName_editor
        global Address_editor
        global PhoneNo_editor
        global clicked_editor
        global Size_editor
        global Quantity_editor

            
        #Create text boxes
        CustomerName_editor=Entry(editor,width=30)
        CustomerName_editor.grid(row=0,column=1,padx=20,pady=(10,0))
        Address_editor=Entry(editor,width=30)
        Address_editor.grid(row=1,column=1,padx=20)
        PhoneNo_editor=Entry(editor,width=30)
        PhoneNo_editor.grid(row=2,column=1,padx=20)
        Quantity_editor=Entry(editor,width=30)
        Quantity_editor.grid(row=3,column=1,padx=20)
        
        CustomerName_editor.insert(0,records[-1][0])
        Address_editor.insert(0,records[-1][1])
        PhoneNo_editor.insert(0,records[-1][2])
        Quantity_editor.insert(0,records[-1][4])
        
            
        #Create text boxes labels
        CustomerName_label=Label(editor,text="Customer Name")
        CustomerName_label.grid(row=0,column=0,pady=(10,0))
        Address_label=Label(editor,text="Address")
        Address_label.grid(row=1,column=0)
        PhoneNo_label=Label(editor,text="Phone No")
        PhoneNo_label.grid(row=2,column=0)
        Quantity_label=Label(editor,text="Quantity")
        Quantity_label.grid(row=3,column=0)
        

        
        

        edit_btn=Button(editor,text="Save Change",command=self.update_order)
        edit_btn.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=145)
        #app.destroy()'''
        

    def Message(self):
        response=messagebox.showinfo("Enjoy Your Order","Thankyou")
        top.destroy()
        top.mainloop()
        
        
        
    def OrderDeatil(self):
        global top
        top=Toplevel()
        top.title("Oder Detail")
        top.geometry("600x120")
        Detail_Set=CustomerName.get()+" your order of "+str(Quantity.get())+" "+Size_of_pizza.get()+"\n"+clicked.get()+ " Pizza is generated at the price of "+str(prize_set)
        order_label=Label(top,text=Detail_Set,font=10)
        order_label.grid(row=0,column=0,columnspan=2,pady=(4,0),padx=80)
        #Update_Button=Button(top,text="Change order",width=20,borderwidth=4,command=self.edit_detail)
        #Update_Button.grid(row=1,column=2,pady=8)
        Ok_Button=Button(top,text="Ok",width=20,borderwidth=4,command=self.Message)
        Ok_Button.grid(row=1,column=1,pady=8)
        Delete_Button=Button(top,text="Delete",width=20,borderwidth=4,command=self.Delete_Order)
        Delete_Button.grid(row=1,column=0,pady=8)
        
        
        

p=Pizza_Odering_System()
p.CustomerWants()

conn.commit()
conn.close()







