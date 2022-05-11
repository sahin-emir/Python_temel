#### NUMPY KÜTÜPHANESİ

### quiz %20
### vize %30
### final sınavı %50  var bunlar liste yapısında tutulsun ortalamasaı bulunsun
### unjagged arrays 
###  düzenli dizi olmalı

##import numpy as np

##quiz=[100,20,50,67,92]
##vize=[50,100,90,63,95]
##final=[100,80,85,20,0]

##quiz=np.array(quiz);
##vize=np.array(vize);
##final=np.array(final);

##Dsonunot=((quiz*0.2)+(vize*0.3)+(final*0.5))
##print(type(Dsonunot))

##print(Dsonunot)

##print("50 puan altı notlar")
##gectimi=Dsonunot>50
##print(gectimi)

#################################################

##import numpy as np

##nDizi=np.arange(1,100)
##print(nDizi)
##d1=np.arange(1,100,2)
##print(d1)

##d6=np.arange(20,dtype=int)
##d7=np.arange(20,dtype=float)
##print(d6)
##print(d6.itemsize)

##print(d7)
##print(d7.itemsize)

##d8=np.arange(10).reshape(2,5)
##print(d8)

##d9=np.arange(9).reshape(3,3)
##print(d9)

##d10=np.arange(8).reshape(4,2)
##print(d10)

##############################
#import numpy as np

##d=np.linspace(1,11,20)
##print(d)

##d2=np.logspace(0,3,4)
##print(d2)

##x=np.array([[1,2,3],[4,5,6]],np.int32)
##print(x)
##print(x.shape)
##print(x.dtype)

##x=np.array([[1,2,3],[4,5,6],[6,7,8]],np.int32)
##print(x.sum(0))
##print(x.sum(1))
##print(x.max())
##print(x.max(1))#min komutu ise tam tersi işlem yapar
##print(x.argmax())
##print(x.ptp())
##print(x.mean())


##x=np.array([[1,2,3],[4,5,6],[6,7,8]],np.int32)
##print(x[1,1])
##print(x[:2])

#x=np.zeros((15,7))
#print(x)
#a=np.ones((15,7))
#print(a)
#z=np.repeat(2,5)
#print(z)
#k=np.array([1,2,3,4,5,67,8,9,3,2,1])
#print(np.unique(k))
#t=np.arange(1,101)
#print(np.where(t%10==0))






