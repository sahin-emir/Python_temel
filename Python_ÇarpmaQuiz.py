
import random

dogrusay=0
yanlıssay=0
sonuc=0
sonucgir=0

while True:
    
    soru=int(random.uniform(1,4+1))
    birsay=int(random.uniform(30,60+1))
    ikisay=int(random.uniform(1,30+1))
    
    
    
    if(dogrusay >= 3 or yanlıssay>=3 ):
        print("oyun bitti")
        print("oyun dogru sayınız",dogrusay,"oyun yanlış sayınız ",yanlıssay)
        break
        
    if (soru==1):
        print(birsay ,"+", ikisay)
        sonuc=birsay+ikisay
        if(sonucgir==sonuc):
            dogrusay+=1
        else:
            yanlıssay+=1
    elif (soru==2):
        
        print(birsay ,"-", ikisay)
        
        sonuc=birsay-ikisay
        
        if(sonucgir==sonuc):
            dogrusay+=1
        else:
            yanlıssay+=1
        
    elif (soru==3):
        print(birsay ,"*", ikisay)
        sonuc=birsay*ikisay
        
        if(sonucgir==sonuc):
            dogrusay+=1
        else:
            yanlıssay+=1
        
        
    elif (soru==4):
        print(birsay ,"/", ikisay)
        sonuc=birsay/ikisay
        if(ikisay==0):
            birsay=int(random.uniform(1,30+1))
            ikisay=int(random.uniform(30,60+1))
        else:
          
            if(sonucgir==sonuc):
                dogrusay+=1
            else:
                yanlıssay+=1
        
    sonucgir=int(input("sonuc gir "))
        
        
    
    