#demet=(1.2,2,4)
#a,b,c=demet

#print(a)
#print(b)
#print(c)


#list=[1,2,3,4]
#demet=zip(list)
#print(demet)
#print(type(demet))


#liste=["elma","elma","armut","ayva","nar","erik"]
#kume=set(liste)
#print(type(kume))
#kume.add("patates")
#kume.pop()
#print(kume)

#liste=["elma","elma","armut","ayva","nar","erik"]
#asd=set({"elma":5,"armut":5})
#print(type(asd))
#print(asd)

import random
hisse={
    
    "Abc":12,
    "asd":45
    }
if("aaa" in hisse):
    print(hisse["aaa"])
else:
    print("yok")

print(hisse.get("aaa","hisse bulanamadı"))

#def kabarcık(liste):
#    x=len(liste)
#    for i in range(0,x-1):
#        for j in range(0,x-i-1):
#                #takas yap
#                if(liste[j]>liste[j+1]):
#                    temp=liste[j]
#                    liste[j]=liste[j+1]
#                    liste[j+1]=temp
#    return liste

#liste=[9,8,5,6,2,3,4,5,6]
#print(kabarcık(liste))

def deneme():
    isim="beykent"
    yil=1997
    sonuc =True
    return isim,yil,sonuc
ad,sene,durum=deneme()
print(ad)
print(sene)
print(durum)
