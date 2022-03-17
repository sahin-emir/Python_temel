# sayi tqhmin / number prediction
import random

dogrucevap=int(random.uniform(1,100+1))

while True:
    sayi=int(input("1-100 arasındaki sayıyı tahmin et ==  "))
    #50
    if(dogrucevap == sayi):
        print("dogru bildiniz succes ")
        break
    elif (sayi<dogrucevap ):
        print("sayıyı büyütmeye ne dersin")
    elif(sayi > dogrucevap ):
        print("sayıyı küçültmeye ne dersin")
    else:
        print("1 - 100 arasında girmeyi deneyin")   
    
    