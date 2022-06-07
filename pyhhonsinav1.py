
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
