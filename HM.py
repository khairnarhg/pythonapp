#Importing modules
from tkinter import*
from tkinter.font import Font
from PIL import ImageTk,Image
import random
import datetime
import mysql.connector
from tkinter import ttk
from tkinter import messagebox
import csv


room=[]
roomc=[]
day=[]
roomc2=[]




def csvfile():
    File1=open("rooms.csv","w", newline='')
    file1_write= csv.writer(File1, delimiter=',')
    new_var=[ 
            ['Basic','Standard NON-AC','Standard AC'],
            ['Single Window', 'Single Bed', 'Attached Bathrrom-hot/cold water', 'A table with drawers','Telephone'], 
            ['Double Window', 'Single Bed', 'Attached Bathrrom-hot/cold water', 'Teapoy','single Sofa','Telephone','Double Door Cupboard', 'Complementary Breakfast'],
            ['AC','Balcony',' Single Bed', 'Attached Bathrrom-hot/cold water', 'Teapoy','2 sofa','Telephone','Television','Double Door Cupboard','Complementary Breakfast', 'Free Room Service'], 
            ['Single Window', 'Double Bed', 'Attached Bathrrom-hot/cold water', 'A table with drawers','Telephone', 'A sofa'], 
            ['Double Window',' Double Bed', 'Attached Bathrrom-hot/cold water', 'Teapoy','Double Sofa','Telephone','Double Door Cupboard', 'Complementary Breakfast'],
            ['AC','Balcony', 'Double Bed', 'Attached Bathrrom-hot/cold water', 'Teapoy','2 sofa','Telephone','Television','Double Door Cupboard', 'Complementary Breakfast', 'Free Room Service'],
            ['Balcony','1 Double Bed + 1 single bed',' Attached Bathrrom-hot/cold water', 'A table with drawers','Telephone', 'A sofa cum bed'], 
            ['Balcony',' 1 Double Bed + 1 single bed', 'Attached Bathrrom-hot/cold water', 'Teapoy','Double Sofa cum bed','Telephone','Double Door Cupboard', 'Complementary Breakfast'],
            ['AC','Balcony', '1 Double Bed + 1 single bed','attached Bathrrom-hot/cold water',' Teapoy','2 sofa cum bed','Telephone','Television','Double Door Cupboard', 'Complementary Breakfast', 'Free Room Service'] ]
    file1_write.writerows(new_var)
    print("File Created") 
    File1.close()   
            
csvfile()  

def csvfile2():
    File4= open("menucard.csv",'w',newline='')
    file4_write=csv.writer(File4, delimiter=',')
    new_var3=[ 
             ['JATTU BHAI KA DHABA', 'MENU CARD'],
             [' BEVARAGES','1 Regular Tea............. 20.00','2 Masala Tea.............. 25.00','3 Coffee.................. 25.00','4 Cold Drink.............. 25.00','5 Bread Butter............ 30.00','6 Bread Jam............... 30.00','7 Veg. Sandwich........... 50.00','8 Veg. Toast Sandwich..... 50.00','9 Cheese Toast Sandwich... 70.00','10 Grilled Sandwich........ 70.00'],
             ['SOUPS','11 Tomato Soup............ 110.00','12 Hot & Sour............. 110.00','13 Veg. Noodle Soup....... 110.00','14 Sweet Corn............. 110.00','15 Veg. Munchow........... 110.00'],
             ['MAIN COURSE','16 Shahi Paneer........... 110.00','17 Kadai Paneer........... 110.00','18 Handi Paneer........... 120.00','19 Palak Paneer........... 120.00','20 Chilli Paneer.......... 140.00','21 Matar Mushroom......... 140.00','22 Mix Veg................ 140.00','23 Jeera Aloo............. 140.00',' 24 Malai Kofta............ 140.00','25 Aloo Matar............. 140.00',' 26 Dal Fry................ 140.00',' 27 Dal Makhani............ 150.00','28 Dal Tadka.............. 150.00'],
             [' ROTI','29 Plain Roti.............. 15.00','30 Butter Roti............. 15.00','31 Tandoori Roti........... 20.00','32 Butter Naan............. 20.00'] ,
             ['RICE','33 Plain Rice.............. 90.00','34 Jeera Rice.............. 90.00',' 35 Veg Pulao.............. 110.00','36 Peas Pulao............. 110.00'],
             ['SOUTH INDIAN','37 Plain Dosa............. 100.00','38 Onion Dosa............. 110.00',' 39 Masala Dosa............ 130.00','40 Paneer Dosa............ 130.00','41 Rice Idli.............. 130.00','42 Sambhar Vada........... 140.00'],
             ['ICE CREAM','43 Vanilla................. 60.00','44 Strawberry.............. 60.00','45 Pineapple............... 60.00','46 Butter Scotch........... 60.00'] ]
    file4_write.writerows(new_var3)
    print('File Created 2')
    File4.close()
csvfile2()
    
            

            

#Tkinter window
root=Tk()
root.geometry("1380x800")
root.title(' JBKD ')

#Fonts defined
font1= Font(family='times',size=30,underline=1, slant='roman')
font2=Font(family='Century Gothic', size= 20)
font3=Font(family='Century Gothic', size= 20)
font4=Font(family='Century Gothic', size= 15)
font5=Font(family='Century Gothic', size= 13)



#Bg images
bg1=PhotoImage(file="D:\IP\GREAT_PTyHON\Project 2022\morning picture b.png")
bg2=PhotoImage(file="D:\IP\GREAT_PTyHON\Project 2022\morning picture b.png")
img=ImageTk.PhotoImage(Image.open("D:\IP\GREAT_PTyHON\Project 2022\JBKD.png"))

#canvas
canvas1=Canvas(root,width=1380, height=800, bd=0, highlightthicknes=0)
canvas1.pack(fill='both', expand=True)

canvas1.create_image(0,0, image=bg1, anchor='nw')
canvas1.create_text(680,20,text="WELCOME TO JATTU BHAI KA DHABA!!!", font=font1, fill="White")
canvas1.create_image(1150,110, image=img)

#Buttons
butt1=Button(root, text='Booking', font=font2,bg='yellow', command=lambda: Booking())
butt2=Button(root, text='Rooms Info',font=font2,bg='yellow', command=lambda: roominfo())
butt3=Button(root, text='Menu Card',font=font2,bg='yellow',command=lambda: menucard())

butt6=Button(root, text='Exit',font=font2,bg='yellow',command= root.destroy)


butt1_window=canvas1.create_window(50, 350,anchor='nw',height=50, width=400,   window=butt1)
butt2_window=canvas1.create_window(50, 410,anchor='nw',height=50, width=400, window=butt2)
butt3_window=canvas1.create_window(50, 470,anchor='nw',height=50, width=400, window=butt3)

butt6_window=canvas1.create_window(50, 530,anchor='nw',height=50, width=400,  window=butt6)


def Booking():
    
    
    newwindow=Toplevel(root)
    newwindow.title('JBKD')
    newwindow.geometry('1380x800')
    canvas2=Canvas(newwindow,width=1380, height=800,bd=0, highlightthicknes=0)
    canvas2.pack(fill='both', expand=True)
    canvas2.create_image(0,0, image=bg2, anchor='nw')
    canvas2.create_text(700,20,text= "PLEASE PROVIDE THE FOLLOWING INFORMATION", font=font1, fill="white")

    canvas2.create_text(80,260,text= "First Name:", font=font3, fill="white", anchor='nw',)
    canvas2.create_text(80,300,text= "Last Name:", font=font3, fill="white", anchor='nw')
    canvas2.create_text(80,340,text= "Age:", font=font3, fill="white", anchor='nw')
    canvas2.create_text(80,380,text= "Govt. Approved CardName :", font=font3, fill="white", anchor='nw')
    canvas2.create_text(80,420,text= "Govt. Approved CardNo:", font=font3, fill="white", anchor='nw')
    canvas2.create_text(80,460,text= "Address:", font=font3, fill="white", anchor='nw')
    canvas2.create_text(80,500,text= "Phone No.:", font=font3, fill="white", anchor='nw')
    canvas2.create_text(80,540,text= "Email Id:", font=font3, fill="white", anchor='nw')
    canvas2.create_text(80,580,text= "CheckIn:", font=font3, fill="white", anchor='nw')
    canvas2.create_text(80,620,text= "CheckOut:", font=font3, fill="white", anchor='nw')
    canvas2.create_text(80,660,text= "Number of Adults:", font=font3, fill="white", anchor='nw')
    canvas2.create_text(80,700,text= "Number of Children:", font=font3, fill="white", anchor='nw')

    F_entry=Entry(newwindow, font=font4, width=15,fg='black', bd=0)
    l_entry=Entry(newwindow, font=font4, width=15,fg='black', bd=0)
    a_entry=Entry(newwindow, font=font4, width=15,fg='black', bd=0)
    go_entry=Entry(newwindow, font=font4, width=20,fg='black', bd=0)
    g_entry=Entry(newwindow, font=font4, width=40,fg='black', bd=0)
    A_entry=Entry(newwindow, font=font4, width=50,fg='black', bd=0)
    p_entry=Entry(newwindow, font=font4, width=20,fg='black', bd=0)
    e_entry=Entry(newwindow, font=font4, width=30,fg='black', bd=0)
    c_entry=Entry(newwindow, font=font4, width=15,fg='black', bd=0)
    ch_entry=Entry(newwindow, font=font4, width=15,fg='black', bd=0)
    na_entry=Entry(newwindow, font=font4, width=20,fg='black', bd=0)
    nc_entry=Entry(newwindow, font=font4, width=20,fg='black', bd=0)

    F_window=canvas2.create_window(260,270, anchor='nw', window=F_entry)
    l_window=canvas2.create_window(260,310, anchor='nw', window=l_entry)
    a_window=canvas2.create_window(260,350, anchor='nw', window=a_entry)
    go_window=canvas2.create_window(460,390, anchor='nw', window=go_entry)
    g_window=canvas2.create_window(430,430, anchor='nw', window=g_entry)
    A_window=canvas2.create_window(260,470, anchor='nw', window=A_entry)
    p_window=canvas2.create_window(260,510, anchor='nw', window=p_entry)
    e_window=canvas2.create_window(260,550, anchor='nw', window=e_entry)
    c_window=canvas2.create_window(260,590, anchor='nw', window=c_entry)
    ch_window=canvas2.create_window(260,630, anchor='nw', window=ch_entry)
    na_window=canvas2.create_window(340,670, anchor='nw', window=na_entry)
    nc_window=canvas2.create_window(360,710, anchor='nw', window=nc_entry)

    F_entry.insert(0, "Enter First Name")
    l_entry.insert(0, "Enter Last Name")
    a_entry.insert(0, "Enter Your Age")
    go_entry.insert(0,"Enter GACName")
    g_entry.insert(0, "Enter GACN")
    A_entry.insert(0, "Enter Address")
    p_entry.insert(0, "Enter PhoneNo")
    e_entry.insert(0, "Enter EmailId")
    c_entry.insert(0, "Enter Checkin")
    ch_entry.insert(0, "Enter checkout")
    na_entry.insert(0, "Enter no of Adults")
    nc_entry.insert(0, "Enter no of Children ")

    def date(c):
            if c[2]>= 2021 and c[2] <=2025:
                if c[1] !=0 and c[1] <=12:
                    if c[1]==2 and c[0] !=0 and c[0]<=31:
                        if c[2]%4==0 and c[0]<=29:
                            pass
                        elif c[0]<29:
                            pass
                        else:
                            messagebox.showinfo("Error", " Invalid Date")
                    elif c[1]<=7 and c[1]%2 !=0 and c[0]<=31:
                        pass
                    elif c[1]<=7 and c[1]%2==0 and c[0] <=30 and c[1] !=2:
                        pass
                    elif c[1] >= 8 and c[1]%2 == 0 and c[0] <= 31:
                        pass
                    elif c[1]>=8 and c[1]%2!=0 and c[0]<=30:
                        pass
                    else:
                        messagebox.showinfo("Error", " Invalid Date")
                else:
                    messagebox.showinfo("Error", " Invalid Date")
            else:
                messagebox.showinfo("Error", " Invalid Date")
    
    def Output():
        F=F_entry.get()
        l=l_entry.get()
        a=a_entry.get()
        go=go_entry.get()
        g=g_entry.get()
        A=A_entry.get()
        p=p_entry.get()
        e=e_entry.get()
        c=c_entry.get()
        ch=ch_entry.get()
        na=na_entry .get()
        nc=nc_entry .get()

        if F=="" and l=="" and a=="" and go=="" and g=="" and A=="" and p=="" and e=="" and c=="" and ch=="" and na=="" and nc=="":
            messagebox.showinfo("Error", "Pls provide full info")
        elif int(a_entry.get())< 18:
            messagebox.showinfo("Error", "18+ Age required")
        else:
            pass

        x=str(c_entry.get())
        x=x.split('/')
        ai=x
        ai[0]=int(ai[0])
        ai[1]=int(ai[1])
        ai[2]=int(ai[2])
        date(ai)

        y=str(ch_entry.get())
        y=y.split('/')
        bo=y
        bo[0]=int(bo[0])
        bo[1]=int(bo[1])
        bo[2]=int(bo[2])

        if bo[1]<ai[1] and bo[2]<ai[2]:
                    messagebox.showinfo("Error", " Checkout must fall after checkin")
        elif bo[1]==ai[1] and bo[2]==ai[2] and bo[0]<=ai[0]:
            messagebox.showinfo("Error", " Checkout must fall after checkin")
        else:
            pass  
        date(bo)
        d1=datetime.datetime(ai[2],ai[1],ai[0])
        d2=datetime.datetime(bo[2],bo[1],bo[0])
        d=(d2-d1).days
        day.append(d)

        if (int(na_entry.get())+int(nc_entry.get()))>8:
            messagebox.showinfo("Error", " Room not available for so many people, max=8")
        else:
            pass
        if len(str(p))>10:
            messagebox.showinfo("Error", " Insert valid phone number")
        else:
            pass
        global costid
        costid=((str(p)[7:9])+(str(F)[0:2])+(str(c)[0]+str(c)[1])+(str(ch)[0]+str(ch)[1]))
        global cd
        cd=str(costid)

        mydb=mysql.connector.connect(host='localhost', user='root', passwd='password', database='ur_database')
        if mydb.is_connected()==False:
            print('Error Connecting Mysql Database.')
        mycursor=mydb.cursor()
        mycursor.execute('USE JBKD;')
        mycursor.execute('''CREATE TABLE IF NOT EXISTS COSTINFO(
        COSTID VARCHAR(20),
        FIRSTNAME CHAR(20), 
        lASTNAME CHAR(20), 
        AGE VARCHAR(10),
        GACN CHAR (20), 
        GACNO VARCHAR(20),
        ADDRESS VARCHAR(60), 
        PHONENO VARCHAR(30),
        EMAILID VARCHAR(30), 
        CHECKIN VARCHAR(20),
        CHECKOUT VARCHAR(20), 
        ADULTS VARCHAR(10),
        CHILDREN VARCHAR(10));''')
        mycursor.execute("INSERT INTO COSTINFO(COSTID,FIRSTNAME, LASTNAME, AGE, GACN, GACNO, ADDRESS, PHONENO, EMAILID, CHECKIN, CHECKOUT, ADULTS,CHILDREN)VALUES(%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(cd,F,l,a,go, g, A, p, e, c, ch, na, nc))
        mydb.commit()
        messagebox.showinfo("Thank you","Record Inserted")
        
    MyButton=Button(newwindow, text="Submit",font=font4, width=20, bg="white", fg="black",command=lambda: Output())
    MyButton_Window=canvas2.create_window(450,750, anchor='nw', window=MyButton)
    MyButton3=Button(newwindow, text="Cancel",font=font4, width=20, bg="white", fg="black",command= newwindow.destroy)
    MyButton_Window=canvas2.create_window(200,750, anchor='nw', window=MyButton3)
       
    def rooms():
        newwindow.withdraw()
        newwindow12=Toplevel(newwindow)
        newwindow12.title('JBKD')
        newwindow12.geometry('1380x800')
        canvas3=Canvas(newwindow12,width=1380, height=800, bd=0, highlightthicknes=0)
        canvas3.pack(fill='both', expand=True)

        canvas3.create_image(0,0, image=bg1, anchor='nw')
        canvas3.create_text(700,20,text="Choose Your Desired Room", font=font1, fill="White")
        canvas3.create_text(290,150,text="Basic", font=font3, fill="White")
        canvas3.create_text(710,150,text="Standard Non AC", font=font3, fill="White")
        canvas3.create_text(1110,150,text="Standard AC", font=font3, fill="White")
        canvas3.create_text(380,350,text="Room Amenities are as follows", font=font3, fill="White")

        file2= open('rooms.csv','r')
        reader= csv.reader(file2)
        data=list(reader)
        
        
        
        def show1():
            room.append('Basic-Single Bed')
            roomc.append('1000/-')
            roomc2.append(1000)
            v1=StringVar(value=data[1])
            listbox1=Listbox(newwindow12, listvariable=v1, font=font4)
            listbox1_window=canvas3.create_window(180,370, anchor='nw' ,width=700,height=300, window=listbox1)

        def show2():
            room.append('Basic-Double Bed')
            roomc.append('1500/-')
            roomc2.append(1500)
            v1=StringVar(value=data[2])
            listbox1=Listbox(newwindow12, listvariable=v1, font=font4)
            listbox1_window=canvas3.create_window(180,370, anchor='nw' ,width=700,height=300, window=listbox1)

        def show3():
            room.append('Basic-Triple Bed')
            roomc.append('2000/-')
            roomc2.append(2000)
            v1=StringVar(value=data[3])
            listbox1=Listbox(newwindow12, listvariable=v1, font=font4)
            listbox1_window=canvas3.create_window(180,370, anchor='nw' ,width=700,height=300, window=listbox1)

        def show4():
            room.append('Standard(non-AC)-Single Bed')
            roomc.append('2000/-')
            roomc2.append(2000)
            v1=StringVar(value=data[4])
            listbox1=Listbox(newwindow12, listvariable=v1, font=font4)
            listbox1_window=canvas3.create_window(180,370, anchor='nw' ,width=700,height=300, window=listbox1)

        def show5():
            room.append('Standard(non-AC)-Double Bed')
            roomc.append('2500/-')
            roomc2.append(2500)
            v1=StringVar(value=data[5])
            listbox1=Listbox(newwindow12, listvariable=v1, font=font4)
            listbox1_window=canvas3.create_window(180,370, anchor='nw' ,width=700,height=300, window=listbox1)
        
        def show6():
            room.append('Standard(non-AC)-Triple Bed')
            roomc.append('3000/-')
            roomc2.append(3000)
            v1=StringVar(value=data[6])
            listbox1=Listbox(newwindow12, listvariable=v1, font=font4)
            listbox1_window=canvas3.create_window(180,370, anchor='nw' ,width=700,height=300, window=listbox1)
        
        def show7():
            room.append('Standard(AC)-Single Bed')
            roomc.append('3000/-')
            roomc2.append(3000)
            v1=StringVar(value=data[7])
            listbox1=Listbox(newwindow12, listvariable=v1, font=font4)
            listbox1_window=canvas3.create_window(180,370, anchor='nw' ,width=700,height=300, window=listbox1)
        
        def show8():
            room.append('Standard(AC)-Double Bed')
            roomc.append('3500/-')
            roomc2.append(3500)
            v1=StringVar(value=data[8])
            listbox1=Listbox(newwindow12, listvariable=v1, font=font4)
            listbox1_window=canvas3.create_window(180,370, anchor='nw' ,width=700,height=300, window=listbox1)
        
        def show9():
            room.append('Standard(AC)-Triple Bed')
            roomc.append('4000/-')
            roomc2.append(4000)
            v1=StringVar(value=data[9])
            listbox1=Listbox(newwindow12, listvariable=v1, font=font4)
            listbox1_window=canvas3.create_window(180,370, anchor='nw' ,width=700,height=300, window=listbox1)


        My_Button1=Button(newwindow12, text="Single Bed-Price:1000/-", font=font4,height=1, width=20, bg="white", fg= "black", command=lambda: show1() )
        My_Button2=Button(newwindow12, text="Double Bed-Price:1500/-", font=font4,height=1, width=20, bg="white", fg= "black",  command=lambda: show2())
        My_Button3=Button(newwindow12, text="Triple Bed-Price:2000/-", font=font4,height=1, width=20, bg="white", fg= "black", command=lambda: show3() )
        
        My_Button1_window=canvas3.create_window(170,170, anchor='nw' , window=My_Button1)
        My_Button2_window=canvas3.create_window(170,211, anchor='nw' , window=My_Button2)
        My_Button3_window=canvas3.create_window(170,251, anchor='nw' , window=My_Button3)

        My_Button4=Button(newwindow12, text="Single Bed-Price:2000/-", font=font4,height=1, width=20, bg="white", fg= "black", command=lambda: show4() )
        My_Button5=Button(newwindow12, text="Double Bed-Price:2500/-", font=font4,height=1, width=20, bg="white", fg= "black", command=lambda: show5() )
        My_Button6=Button(newwindow12, text="Triple Bed-Price:3000/-", font=font4,height=1, width=20, bg="white", fg= "black", command=lambda: show6() )

        My_Button4_window=canvas3.create_window(575,170, anchor='nw' , window=My_Button4)
        My_Button5_window=canvas3.create_window(575,211, anchor='nw' , window=My_Button5)
        My_Button6_window=canvas3.create_window(575,251, anchor='nw' , window=My_Button6)

        My_Button7=Button(newwindow12, text="Single Bed-Price:3000/-", font=font4,height=1, width=20, bg="white", fg= "black", command=lambda: show7() )
        My_Button8=Button(newwindow12, text="Double Bed-Price:3500/-", font=font4,height=1, width=20, bg="white", fg= "black", command=lambda: show8() )
        My_Button9=Button(newwindow12, text="Triple Bed-Price:4000/-", font=font4,height=1, width=20, bg="white", fg= "black", command=lambda: show9() )

        My_Button7_window=canvas3.create_window(1000,170, anchor='nw' , window=My_Button7)
        My_Button8_window=canvas3.create_window(1000,211, anchor='nw' , window=My_Button8)
        My_Button9_window=canvas3.create_window(1000,251, anchor='nw' , window=My_Button9)

        My_Button10=Button(newwindow12, text="Prev", font=font4,height=1, width=10, bg="white", fg= "black", command= lambda: newwindow.deiconify())
        My_Button10_window=canvas3.create_window(180,700, anchor='nw' , window=My_Button10)

        My_Button12=Button(newwindow12, text="Cancel", font=font4,height=1, width=10, bg="white", fg= "black", command= lambda: newwindow12.destroy())
        My_Button12_window=canvas3.create_window(580,700, anchor='nw' , window=My_Button12)

        def pay1():
            newwindow12.withdraw()
            newwindow1=Toplevel(newwindow12)
            newwindow1.title('JBKD')
            newwindow1.geometry('750x400')
            canvas4=Canvas(newwindow1,width=750, height=400, bd=0, highlightthicknes=0)
            canvas4.pack(fill='both', expand=True)
            canvas4.create_image(0,0, image=bg1, anchor='nw')
            canvas4.create_text(300,20,text="Payment", font=font1, fill="White")

            def bill1():
                
                F1=str(F_entry.get())
                l1=str(l_entry.get())
                a1=str(a_entry.get())
                go1=str(go_entry.get())
                g1=str(g_entry.get())
                A1=str(A_entry.get())
                p1=str(p_entry.get())
                e1=str(e_entry.get())
                c1=str(c_entry.get())
                ch1=str(ch_entry.get())
                na1=str(na_entry .get())
                nc1=str(nc_entry .get())

                roomc1=str(roomc2[0]*day[0])
                d1=int(roomc2[0]*day[0])
                gst= str(((18*(d1))/100) + d1)
                    
                newwindow2=Toplevel(newwindow1)
                newwindow2.title('JBKD')
                newwindow2.geometry('600x700')
                label1=Label(newwindow2,text='JATTU BHAI KA DHABA',font=font3).grid(row=0,column=0)
                label22=Label(newwindow2,text='Bill',font=font3).grid(row=1,column=0)
                label2=Label(newwindow2,text='Name:',font=font4).grid(row=2,column=0)
                label3=Label(newwindow2,text=F1+l1,font=font4).grid(row=2,column=1)
                label4=Label(newwindow2,text='Costumer Id:',font=font4).grid(row=3,column=0)
                label5=Label(newwindow2,text=cd,font=font4).grid(row=3,column=1)
                label6=Label(newwindow2,text='Phone NO:',font=font4).grid(row=4,column=0)
                label7=Label(newwindow2,text=p1,font=font4).grid(row=4,column=1)
                label8=Label(newwindow2,text='CHECKIN:',font=font4).grid(row=5,column=0)
                label9=Label(newwindow2,text=c1,font=font4).grid(row=5,column=1)
                label10=Label(newwindow2,text='CHECKOUT:',font=font4).grid(row=6,column=0)
                label11=Label(newwindow2,text=ch1,font=font4).grid(row=6,column=1)
                label12=Label(newwindow2,text='RoomType:',font=font4).grid(row=7,column=0)
                label13=Label(newwindow2,text=room[0],font=font4).grid(row=7,column=1)
                label14=Label(newwindow2,text='RoomCharges/day:',font=font4).grid(row=8,column=0)
                label15=Label(newwindow2,text=roomc[0],font=font4).grid(row=8,column=1)
                label16=Label(newwindow2,text='TotalRoomCharges:',font=font4).grid(row=9,column=0)
                label17=Label(newwindow2,text=roomc1,font=font4).grid(row=9,column=1)
                label18=Label(newwindow2,text='GST: 18%',font=font4).grid(row=10,column=0)
                label19=Label(newwindow2,text='Total charges:',font=font4).grid(row=11,column=0)
                label20=Label(newwindow2,text=gst,font=font4).grid(row=11,column=1)
                label21=Label(newwindow2,text='VISIT AGAIN',font=font4).grid(row=12,column=0)
                messagebox.showinfo("JBKD","Thanks For Booking at JBKD")
                newwindow1.destroy
                newwindow12.destroy
                file2.close()

            My_Button13=Button(newwindow1, text="Credit/Debit Card", font=font4,height=1, width=30, bg="white", fg= "black", command= lambda: bill1())
            My_Button13_window=canvas4.create_window(150,100, anchor='nw' , window=My_Button13)

            My_Button13=Button(newwindow1, text="Paytm/GooglePay/Phonepe", font=font4,height=1, width=30, bg="white", fg= "black", command= lambda: bill1())
            My_Button13_window=canvas4.create_window(150,140, anchor='nw' , window=My_Button13)

            My_Button13=Button(newwindow1, text="Using UPI Id", font=font4,height=1, width=30, bg="white", fg= "black", command= lambda: bill1())
            My_Button13_window=canvas4.create_window(150,180, anchor='nw' , window=My_Button13)

            My_Button13=Button(newwindow1, text="Cash On Delivery", font=font4,height=1, width=30, bg="white", fg= "black", command= lambda: bill1())
            My_Button13_window=canvas4.create_window(150,220, anchor='nw' , window=My_Button13)

        My_Button11=Button(newwindow12, text="Pay", font=font4,height=1, width=10, bg="white", fg= "black",command=lambda: pay1())
        My_Button11_window=canvas3.create_window(380,700, anchor='nw' , window=My_Button11)
    My_Button1=Button(newwindow, text="next", font=font4, width=10, bg="white", fg= "black",command=lambda: rooms())
    My_Button1_window=canvas2.create_window(700,750, anchor='nw' , window=My_Button1)    

def roominfo():
    root.withdraw()
    newwindow3=Toplevel(root)
    newwindow3.title('JBKD')
    newwindow3.geometry('1380x800')
    canvas6=Canvas(newwindow3,width=1380, height=800, bd=0, highlightthicknes=0)
    canvas6.pack(fill='both', expand=True)
    canvas6.create_image(0,0, image=bg1, anchor='nw')
    canvas6.create_text(700,20,text="Room Information", font=font1, fill="White")

    file3=open('rooms.csv','r')
    reader2=csv.reader(file3)
    info= list(reader2)

    
    v11=StringVar(value=info[1])
    v22=StringVar(value=info[2])
    v33=StringVar(value=info[3])
    v44=StringVar(value=info[4])
    v55=StringVar(value=info[5])
    v66=StringVar(value=info[6])
    v77=StringVar(value=info[7])
    v88=StringVar(value=info[8])
    v99=StringVar(value=info[9])
    
    canvas6.create_text(190,100,text="Basic-Single Bed:-Price-1000/-", font=font4, fill="White")
    mylistbox2=Listbox(newwindow3,listvariable=v11, font=font5)
    mylistbox2_window=canvas6.create_window(40,120, anchor='nw' ,width=400,height=150, window=mylistbox2)

    canvas6.create_text(680,100,text="Standard Non AC-Single Bed:-Price-2000/-", font=font4, fill="White")
    mylistbox2=Listbox(newwindow3,listvariable=v22, font=font5)
    mylistbox2_window=canvas6.create_window(480,120, anchor='nw' ,width=400,height=150, window=mylistbox2)

    canvas6.create_text(1120,100,text="Standard AC-Single Bed:-Price-3000/-", font=font4, fill="White")
    mylistbox2=Listbox(newwindow3,listvariable=v33, font=font5)
    mylistbox2_window=canvas6.create_window(940,120, anchor='nw' ,width=400,height=150, window=mylistbox2)

    canvas6.create_text(190,290,text="Basic-Double Bed:-Price-1500/-", font=font4, fill="White")
    mylistbox2=Listbox(newwindow3,listvariable=v44, font=font5)
    mylistbox2_window=canvas6.create_window(40,310, anchor='nw' ,width=400,height=150, window=mylistbox2)

    canvas6.create_text(680,290,text="Standard Non AC-Double Bed:-Price-2500/-", font=font4, fill="White")
    mylistbox2=Listbox(newwindow3,listvariable=v55, font=font5)
    mylistbox2_window=canvas6.create_window(480,310, anchor='nw' ,width=400,height=150, window=mylistbox2)

    canvas6.create_text(1120,290,text="Standard AC-Double Bed:-Price-3500/-", font=font4, fill="White")
    mylistbox2=Listbox(newwindow3,listvariable=v66, font=font5)
    mylistbox2_window=canvas6.create_window(940,310, anchor='nw' ,width=400,height=150, window=mylistbox2)

    canvas6.create_text(190,480,text="Basic-Triple Bed:-Price-2000/-", font=font4, fill="White")
    mylistbox2=Listbox(newwindow3,listvariable=v77, font=font5)
    mylistbox2_window=canvas6.create_window(40,500, anchor='nw' ,width=400,height=150, window=mylistbox2)

    canvas6.create_text(680,480,text="Standard Non AC-Triple Bed:-Price-3000/-", font=font4, fill="White")
    mylistbox2=Listbox(newwindow3,listvariable=v88, font=font5)
    mylistbox2_window=canvas6.create_window(480,500, anchor='nw' ,width=400,height=150, window=mylistbox2)

    canvas6.create_text(1120,480,text="Standard AC-Triple Bed:-Price-4000/-", font=font4, fill="White")
    mylistbox2=Listbox(newwindow3,listvariable=v99, font=font5)
    mylistbox2_window=canvas6.create_window(940,500, anchor='nw' ,width=400,height=150, window=mylistbox2)    

    def back():
        root.deiconify()
        newwindow3.destroy()

    button1=Button(newwindow3,text="Back", font=font4,height=1, width=10, bg="white", fg= "black", command= lambda: back() )
    button1_window=canvas6.create_window(1200,700, anchor='nw' , window=button1)   
def menucard():
    
    root.withdraw()
    newwindow4=Toplevel(root)
    newwindow4.title('JBKD')
    newwindow4.geometry('1380x800')
    canvas7=Canvas(newwindow4,width=1380, height=800, bd=0, highlightthicknes=0)
    canvas7.pack(fill='both', expand=True)
    canvas7.create_image(0,0, image=bg1, anchor='nw')
    canvas7.create_text(700,20,text="Menu Card", font=font1, fill="White")

    
    
    
    file4=open('menucard.csv','r')
    reader3=csv.reader(file4)
    info1= list(reader3)

    var2= StringVar(value=info1[0])
    var3= StringVar(value=info1[1])
    var4= StringVar(value=info1[2])
    var5= StringVar(value=info1[3])
    var6= StringVar(value=info1[4])
    var7= StringVar(value=info1[5])
    var8= StringVar(value=info1[6])
    var9= StringVar(value=info1[7])
    
    mylistbox2=Listbox(newwindow4,listvariable=var2, font=font5)
    mylistbox2_window=canvas7.create_window(480,70, anchor='nw' ,width=400,height=50, window=mylistbox2)

    mylistbox3=Listbox(newwindow4,listvariable=var3, font=font5)
    mylistbox3_window=canvas7.create_window(40,120, anchor='nw' ,width=400,height=150, window=mylistbox3)

    mylistbox4=Listbox(newwindow4,listvariable=var4, font=font5)
    mylistbox4_window=canvas7.create_window(480,120, anchor='nw' ,width=400,height=150, window=mylistbox4)

    mylistbox5=Listbox(newwindow4,listvariable=var4, font=font5)
    mylistbox5_window=canvas7.create_window(940,120, anchor='nw' ,width=400,height=150, window=mylistbox5)

    mylistbox6=Listbox(newwindow4,listvariable=var6, font=font5)
    mylistbox6_window=canvas7.create_window(40,310, anchor='nw' ,width=400,height=150, window=mylistbox6)

    mylistbox7=Listbox(newwindow4,listvariable=var7, font=font5)
    mylistbox7_window=canvas7.create_window(480,310, anchor='nw' ,width=400,height=150, window=mylistbox7)

    mylistbox8=Listbox(newwindow4,listvariable=var8, font=font5)
    mylistbox8_window=canvas7.create_window(940,310, anchor='nw' ,width=400,height=150, window=mylistbox8)

    mylistbox9=Listbox(newwindow4,listvariable=var9, font=font5)
    mylistbox9_window=canvas7.create_window(480,500, anchor='nw' ,width=400,height=150, window=mylistbox9)
    def back():
        root.deiconify()
        newwindow4.destroy()

    button1=Button(newwindow4,text="Back", font=font4,height=1, width=10, bg="white", fg= "black", command= lambda: back() )
    button1_window=canvas7.create_window(1200,700, anchor='nw' , window=button1)

    


    

    file4.close()
   

root.mainloop()    
