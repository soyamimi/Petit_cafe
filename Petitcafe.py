from tkinter import*
from tkinter import messagebox, PhotoImage
from tkinter import PhotoImage, Label, LabelFrame
import tkinter.font as tkFont
import tkinter.ttk
from PIL import Image, ImageTk
import pyzbar.pyzbar as pyzbar
import cv2

reduction = 0
total_price=0
i=0
menu = {'café':2,'latte':4,'thé':3,'smoothie':5}



class CoffeeShop():
    def __init__(self):
        self.window = Tk()
        self.window.title("Petit café")
        self.window.geometry("500x500")
        self.window.resizable(0, 0)
        self.window.configure(background='white')

        label = Label(self.window, text=" \nBonjour,\n Faites votre choix : \n", background='white')
        label.place(x=120,y=10)
        fontlabel = tkFont.Font(family="Simsun",size=10)
        label.configure(font=fontlabel)

        imgcafe = Image.open("C:/Users/840 G6/Desktop/Projet/python/coffeeshop/espresso.png")
        img = imgcafe.resize((100, 100), Image.ANTIALIAS)
        photoImg = ImageTk.PhotoImage(img)
        coffee = Button(self.window, image=photoImg, command=self.coffee, padx=10,pady=10, width=100)
        coffee.place(x=40,y=80)

        labelcafe=Label(self.window,text='Café\n2‎€00',pady=5, padx=5,background='white')
        labelcafe.place(x=75,y=190)

        imglatte  = Image.open("C:/Users/840 G6/Desktop/Projet/python/coffeeshop/latte.jpg")
        img = imglatte.resize((100, 100), Image.ANTIALIAS)
        photoImg2 = ImageTk.PhotoImage(img)
        latte = Button(self.window, image=photoImg2, command=self.latte, width=100)
        latte.place(x=180,y=80)

        labellatte = Label(self.window, text='Latte\n4€00', pady=5, padx=5, background='white')
        labellatte.place(x=212, y=189)

        imgsmoothie = Image.open("C:/Users/840 G6/Desktop/Projet/python/coffeeshop/smoothie.jpg")
        img = imgsmoothie.resize((100, 100), Image.ANTIALIAS)
        photoImg3 = ImageTk.PhotoImage(img)
        smoothie = Button(self.window, image=photoImg3, command=self.smoothie,width=100)
        smoothie.place(x=40, y=250)

        labelsmoothie = Label(self.window, text='Smoothie\n5€00', pady=5, padx=5, background='white')
        labelsmoothie.place(x=61, y=360)

        imgtea = Image.open("C:/Users/840 G6/Desktop/Projet/python/coffeeshop/tea.jpg")
        img = imgtea.resize((100, 100), Image.ANTIALIAS)
        photoImg4 = ImageTk.PhotoImage(img)
        tea = Button(self.window, image=photoImg4, command=self.tea, width=100)
        tea.place(x=180, y=250)

        labeltea = Label(self.window, text='Tea\n3€00', pady=5, padx=5, background='white')
        labeltea.place(x=213, y=360)

        labelcommande = Label(self.window,text='votre commande')
        labelcommande.place(x=360,y=40)
        labelcommande.configure(font=fontlabel)
        self.buttonvalider = Button(self.window, text="Valider",fg='green',command=self.valider)
        self.buttonvalider.place(x=400,y=410)

        self.treeview = tkinter.ttk.Treeview(self.window, columns=["Prix"])
        self.treeview.place(x=330,y=80)

        self.treeview.column("#0", width=90)
        self.treeview.heading("#0", text="Article")

        self.treeview.column("Prix", width=60, anchor="e")
        self.treeview.heading("Prix", text="Prix (€)", anchor="center")

        self.label2 = Label(self.window,text="Prix total =",background='white')
        self.label2.place(x=330,y=350)
        self.window.mainloop()

    def coffee(self):
        global total_price
        global menu
        global i
        i=i+1
        total_price = total_price + menu['café']
        self.treeview.insert("",i,text="café", values=(menu["café"]))
        self.label2['text'] = "Prix total =     {}€ ".format(total_price)

    def latte(self):
        global total_price
        global menu
        global i
        i=i+1
        total_price = total_price + menu['latte']
        self.treeview.insert("",i,text="latte",values=(menu["latte"]))
        self.label2['text'] = "Prix total =     {}€ ".format(total_price)

    def smoothie(self):
        global total_price
        global menu
        global i
        i=i+1
        total_price = total_price + menu['smoothie']
        self.treeview.insert("",i,text="smoothie",values=(menu["smoothie"]))
        self.label2['text'] = "Prix total =     {}€ ".format(total_price)

    def tea(self):
        global total_price
        global menu
        global i
        i = i + 1
        total_price = total_price + menu['thé']
        self.treeview.insert("", i, text="thé", values=(menu["thé"]))
        self.label2['text'] = "Prix total =     {}€ ".format(total_price)

    def carte(self):
        global total_price
        camera_port = 0
        cap = cv2.VideoCapture(camera_port, cv2.CAP_DSHOW)
        while (cap.isOpened()):
            ret, img = cap.read()
            if not ret:
                continue
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            decoded = pyzbar.decode(gray)
            for d in decoded:
                x, y, w, h = d.rect
                barcode_data = d.data.decode("utf-8")
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
                text = '%s' % (barcode_data)
            cv2.imshow('img', img)
            key = cv2.waitKey(1)
            if key == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

        if text == 'Client':
            total_price = total_price * 0.9
            self.label2['text'] = ("Prix total =     {}€\n(10% de réduction appliquée)".format(total_price))

    def valider(self):
        Client = Button(self.window, text="Carte de fidelité", fg='green', command=self.carte)
        Client.place(x=300, y=410)
        self.buttonvalider['text'] = ("Payer")
        self.buttonvalider['fg']=('blue')
        self.buttonvalider['command']=(self.payer)

    def payer(self):
        messagebox.showinfo("Paiement","Inserez votre carte bleue\n\n >>>>>>>>>>>>>>>\n\nPréparation en cours...\n")


CoffeeShop()
