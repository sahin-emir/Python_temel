
import tkinter as tk
from tkinter.ttk import*

from tkinter.filedialog import askopenfilename,asksaveasfilename

## dosya açma

def dosyaAc():

    yol=askopenfilename(
        filetypes[("metin dosyaları","*.txt"),("Tüm Dosyalar","*.*")])
    if not yol:
        return
    t1.delete(1.0,tk.END)

    with open (yol,"r") as gDosya:
        metin=gDosya.read()
        t1.insert(tk.END,text)
    pencere.Title("Düzenleme ekranı ")

def dosyakaydet():
    yol=asksaveasfilenname(
        filetypes=[("Metin dosyaları","*.txt"),("Tüm dosyalar","*.*")])
    if not yol:return

    with open (yol,"w") as aDosya:
        metin=t1.get(1.0,tk.END)
        aDosya.write(metin)
    pencere.Title("dosya kaydetme  ekranı ")

pencere=tk.Tk()
pencere.rowconfigure(0,minsize=400,weight=1)
pencere.columnconfigure(1,minsize=400,weight=1)
t1=tk.Text(pencere)
butonlaryerleşimi=tk.Frame(pencere,relief=tk.RAISED,bd=2)
b1=tk.Button(butonlaryerleşimi,text="Aç",command=dosyaAc)
b2=tk.Button(butonlaryerleşimi,text="Kaydet",command=dosyakaydet)
b1.grid(row=0,column=0)
b2.grid(row=1,column=0)
t1.grid(row=1,column=0)
butonlaryerleşimi.grid(row=0,column=0)

pencere.mainloop()
