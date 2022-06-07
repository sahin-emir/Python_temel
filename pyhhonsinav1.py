
import random as rnd


class Oyun():

    def __init__(self,isim,apuan,bpuan):
        self.isim=isim
        self.apuan=apuan
        self.bpuan=bpuan

    def oyna(self):
        while True:
            if(self.bpuan>95):
                print("bilgisayar kazandı")
                print("bilgisayar puanı "+self.bpuan)
                break
            if(self.apuan>95):
                print("Kazandınız puanınız"+self.apuan)
                break
            if(self.bpuan<5):
                print("bilgisayar kaybettin kazandızınız")
                break
            if(self.apuan<5):
                print("puandan dolayı  kaybettiniz")
                break
            ksayi=rnd.randint(1,7)
            lsayi=rnd.randint(1,7)
    
            if(ksayi> lsayi):
                print("kazandınız")
                self.bpuan-=10
                self.apuan+=10
                print("puanınız ",self.apuan," b puan ",self.bpuan)
            if(ksayi< lsayi):
                print("Kaybettiniz")
                self.bpuan+=10
                self.apuan-=10
                print("puanınız ",self.apuan," b puan ",self.bpuan)
    
            if(ksayi==lsayi):
                print("berabere ")
                self.bpuan-=5
                self.apuan+=5
                print("puanınız ",self.apuan," b puan ",self.bpuan)


isim=input("isim girinii")
apuan=int(input("kaç puanla başlamak istersiniz "))
bpuan=int(input("kaç bpuanla başlamak istersiniz "))
oyuncu=Oyun(isim,apuan,bpuan)
oyuncu.oyna()


import random as rnd
import time

i=1
while True:
    liste=[None]*100
    print(i,"deneme")
    i+=1
    baslangiczaman=time.time()
    for i in range(0,len(liste)):
        liste[i]=rnd.randint(1,100)

    if(liste.count(20)>2 and (liste.count(5)>3)):
        print("sayılar bulundu ")
        print("20 rakam adedi",liste.count(20))
        print("5 rakam adedi",liste.count(5))
        break
    else:
        print("işlem devam ediyor")
        print("20 rakam adedi",liste.count(20))
        print("5 rakam adedi",liste.count(5))
        
bitis=time.time()-baslangiczaman   
print("kod ",bitis*10,"saniye kadar çalıştı ") 
    
    
    import os 
os.getcwd()
liste=["a","b","c","d"]

dosya=open("ilkt.txt","w")
for i in liste:
    dosya.write(i+"ln")
    
dosya.close()
