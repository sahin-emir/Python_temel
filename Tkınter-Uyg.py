
## tk-ınter
## arayüz kütüphanesi

#import tkinter as tk

#pencere=tk.Tk()        #bir form açmaya yarar.
#ilkE=tk.Label(text="Selamlar")
#ilkE.pack()
#l2=tk.Label(text="Naber")
#l2.pack()
#pencere.mainloop()

#from tkinter import *

#class deneme():
#    def __init__(self,metin,baslik):
#        self.l=Label(text=metin)
#        self.l.pack()
#        self.baslik=pencere.title(baslik)

#pencere=Tk()
#uygulama=deneme("1","Uyarı")
#uygulama2=deneme("Emir ...... ","Uyarı")

#mainloop()



#from tkinter import *

#k=Tk()
#label1=Label(
#    text="Tkınter",
#    foreground="red",
#    background="white"
#    )
#label1.pack(pady=20)
#label2=Label(
#    text="Tkınter",
#    fg="red",
#    bg="blue",
#    width=10,
#    height=20
#    )
#label2.config(font=("Times New Roman",20),fg="black")# Sonra güncelleme yapmak iin kullanılır

#label2.pack()
#mainloop()


#from tkinter import *

#pencere=Tk()
#pencere.geometry("300x200+10+2")
#pencere.resizable(width=False,height=False)
#pencere.mainloop()

#from tkinter import *


#def yazdir(self):
#    print("beykent")


#p=Tk()
#buton=Button(text="kaydet",
#             fg="red",
#             bg="black",
#             width=20,
#             height=20,
#             =p.quit)
#buton.pack(side=LEFT)

#b2=Button(text="2.buton",
#          fg="red",
#          bg="black",
#          width=20,
#          height=20,
#          command=yazdir
#          )
#b2.pack(side=RIGHT)


#p.mainloop()


#from tkinter import *


#def olustur():
#    dosya=("deneme.txt","w")
#    metin=metink.get()
#    dosya.write(metin)  



#p=Tk()

### Textbox
#metink=Entry()
#metink.pack()
#dugme=Button(text="oluştur",command=olustur)
#dugme.pack(pady=5)
#d2=Button(text="çıkış",command=p.quit)
#d2.pack(pady=5)

#p.mainloop()


#from tkinter import *


#class uygulama(Frame):
#    def deneme(self):
#        print("deneme çaloıştıur")

#    def oluştur(self):
#        self.cikis=Button(self)
#        self.cikis["text"]="çıkış"
#        self.cikis["fg"]="red"
#        self.cikis["command"]=self.quit
#        self.cikis.pack({"side":"left"})
#        ####
#        self.selam=Button(self)
#        self.selam["text"]="Deneme çalıştır"
#        self.selam["command"]=self.deneme
#        self.selam.pack({"side":"left"})
#        ###
#    def __init__(self,master=None):
#        Frame.__init__(self,master)
#        self.pack()
#        self.oluştur()

#pencere=Tk()
#uyg=uygulama(master=pencere)
#uyg.mainloop()
#p2=Tk()
#u2=uygulama(master=p2)
#p2.mainloop()

#p.destroy()
#from tkinter import *
#from tkinter.ttk import*

#p=Tk()

#degisken=StringVar()## tkinter ait değişkendir
#degisken.set("bir")
#veri=("bir","iki","üç","dört")
#combobox1=Combobox(p,values=veri)
#combobox1.pack()
#combobox1.place(x=60,y=50)

#listbox1=Listbox(p,height=10,selectmode="multiple")
#for i in veri:
#    listbox1.insert(END,i)

#listbox1.place(x=60,y=100)

#radiobuton=Radiobutton(p,text="Erkek",variable=0,value=1)
#radiobbuton2=Radiobutton(p,text="Kız",variable=0,value=2)

#radiobuton.place(x=200,y=200)
#radiobbuton2.place(x=220,y=220)

#chckboX=Checkbutton(p,text="Bilgisiyar",variable=0)
#chckboX1=Checkbutton(p,text="Makine",variable=1)

#chckboX.place(x=60,y=20)
#chckboX1.place(x=60,y=60)


#mainloop()


from tkinter import *

class Islem():
    def __init__(self,pencere):
        self.l1=Label(pencere,text="Birinci sayı")
        self.l2=Label(pencere,text="İkinci sayı")
        self.l3=Label(pencere,text="Sonuç :")

        self.t1=Entry(pencere)
        self.t2=Entry(pencere)
        self.t3=Entry(pencere)

        self.b1=Button(pencere,text="Topla",command=self.topla)
        self.b2=Button(pencere,text="çıkar",command=self.çıkar)
        self.b3=Button(pencere,text="Çarp",command=self.çarp)
        self.b4=Button(pencere,text="Böl",command=self.böl)

        self.l1.place(x=100,y=50)
        self.l2.place(x=100,y=75)
        self.l3.place(x=100,y=100)
        self.t1.place(x=200,y=50)
        self.t2.place(x=200,y=75)
        self.t3.place(x=200,y=100)
        self.b1.place(x=100,y=150)
        self.b2.place(x=150,y=150)
        self.b3.place(x=200,y=150)
        self.b4.place(x=250,y=150)

    def topla(self):
        self.t3.delete(0,"end")
        sayi1=int(self.t1.get())
        sayi2=int(self.t2.get())
        sonuc=sayi1+sayi2
        self.t3.insert(END,str(sonuc))
    def çıkar(self):
        self.t3.delete(0,"end")

        sayi1=int(self.t1.get())
        sayi2=int(self.t2.get())
        sonuc=sayi1-sayi2
        self.t3.insert(END,str(sonuc))
    def çarp(self):
        self.t3.delete(0,"end")

        sayi1=int(self.t1.get())
        sayi2=int(self.t2.get())
        sonuc=sayi1*sayi2
        self.t3.insert(END,str(sonuc))
    def böl(self):
        self.t3.delete(0,"end")

        sayi1=int(self.t1.get())
        sayi2=int(self.t2.get())
        sonuc=sayi1/sayi2
        self.t3.insert(END,str(sonuc))


pencere=Tk()
p1=Islem(pencere)
#p1.title("dör işlem")

pencere.mainloop()





