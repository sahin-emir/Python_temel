#Open CV

#import cv2 as cv
#import numpy as np
#####

import random

class oyun:
    isim;
    puan;
    bpuan;


    def __init__(self):
        self.apuan=0
        self.atoplam=0
        self.bpuan=0
        self.btoplam=0
        self.iyarpuan=0;
        self.kullanicipuan=0;

        self.oyna()

    def oyna(self):
        self.apuan=self.apuan+random.randrange(6)+1
        self.apuan=self.apuan+random.randrange(6)+1
        self.atoplam=self.atoplam+self.apuan
    
        self.bpuan=self.bpuan+random.randrange(6)+1
        self.bpuan=self.bpuan+random.randrange(6)+1
        self.btoplam=self.btoplam+self.bpuan
        self.galip()

    
    def galip(self):
        print ("a oyuncusu:"),self.apuan
        print ("b oyuncusu:"),self.bpuan
        if self.apuan<self.bpuan:
            print("b oyuncusu galip")

        if self.bpuan<self.apuan:
            print ("a oyuncusu galip")

        else:
            print ("puanlar esit")
            print ("--------------------------")
            self.apuan=0
            self.bpuan=0

    def oyunsonu(self):
        print ("a oyuncusunun toplam puanı:"),self.atoplam
        print ("b oyuncusunun toplam puanı:"),self.btoplam
        oran=float(self.atoplam)/float(self.btoplam)
        print ("toplam puanların oranı a/b:"),oran

    oyun1 = oyun()
    a=0
    while a<100:
        a=a+1
    oyun1.oyunubaslat()
    oyun1.oyunsonu()










#img=cv.imread("input/seeds.jpg")
#gri=cv.cvtColor(img,cv.COLOR_RGB2GRAY)
#ret,t=cv.threshold(gri,200,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)

#cv.imshow("t",t)
#c,h=cv.findContours(t,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)
#print("çekşrdek adedid ",len(c))
#cv.drawContours(img,c,-1,(255,0,0),3)
#cv.imshow("sonuc",img)

#cv.waitKey()


### görünütü çizgili yapma

#cap =cv.VideoCapture("input/vtest.avi")
#cikar=cv.createBackgroundSubtractorMOG2(history=100,
#                                       varThreshold=50,
#                                       detectShadows=True)

#while True:
#    c,goruntu=cap.read()
#    mask=cikar.apply(goruntu)

#    cv.imshow("orjinal",goruntu)
#    cv.imshow("arkaplansız",mask)

#    cv.waitKey()





#img=cv.imread("input/lena.jpg",0)
#kernel=np.ones((20,20),np.uint8)

#erozyon=cv.erode(img,kernel,iterations=1)
#dilasoyn=cv.dilate(img,kernel,iterations=1)
#kenar=cv.Canny(img,100,200)
#cv.imshow("i",img)
#cv.imshow("e",erozyon)
#cv.imshow("d",dilasoyn)
#cv.imshow("kenar",kenar)
#cv.waitKey()






##hedef="input/vtest.avi"

##cap=cv.VideoCapture(hedef)
##while True:
##    f,goruntu=cap.read()
##    g2=cv.cvtColor(goruntu,cv.COLOR_BGR2GRAY)

##    b1=cv.blur(g2,(5,5))
##    b2=cv.medianblur(g2,15)
##    b3=cv.GaussinBlur(g2,(15,15),0)

##    ## renk ayırma işlemi
##    #l=np.array([110,50,50])
##    #h=np.array([130,255,255])
##    #maske=cv.inRange(g2,l,h)

##    #sonuc=cv.bitwise_and(goruntu,goruntu,mask=maske)
##    cv.imshow("orj",g2)
##    cv.imshow("b1",b1)
##    cv.imshow("b2",b2)
##    cv.imshow("b3",b3)

##    #cv.imshow("sonuc",sonuc)
##    cv.waitKey(8)





## kendimiz görünüt oluşturulım
#img=np.zeros((512,512,3),np.uint8)

#cv.line(img,(156,156),(511,511),(255,255,0),5)
#cv.rectangle(img,(200,0),(510,128),(0,255,255),9)
#cv.imshow("goruntu",img)
#cv.waitKey()

#####

### video
#hedef="/input/vtest.avi"

#cap=cv.VideoCapture(hedef)## 0 ise kamaewra açar
#sayac=0

#while True:
#    dosyaadi=str(sayac)+".jpg"
#    sayac+=1

#    ret,goruntu=cap.read()
#    cv.imshow("Orjinal",goruntu)
#    cv.waitKey(8)

#    gri=cv.cvtColor(görüntü,cv.COLOR_RGB2GRAY)
#    cv.imshow("Gir sevire",gri)
#    cv.imwrite(dosyaadi,gri)
#    cv.waitKey(8)

#cap.release()






###########
## Resim görüntüleme

#resim=cv.imread("input/lena.jpg")
#print(type(resim))
#print(resim)

#cv.imshow("sonuç",resim)
#cv.imwrite("test/deneme.png",resim)

#cv.waitKey()

######

