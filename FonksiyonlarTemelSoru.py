def tekdöndür(sayi):
    sayi=int(input(" sayı giriniz"))

    if(sayi%2==1):
        print("sayı tektir")
   
    return sayi
def sayiyazdir():

    for i in range(1,1001):
        print(i)

def ortalama(x,y):
    
    ort=(x+y)/2
    print("Ortalamanız: ",ort)
    return ort

def faktoriyelbul(f):
    a=1
    for i in range (1, f+1):
        a = a*i
    return a 

sayiyazdir()
x=int(input(" 1.sayıyı giriniz"))
y=int(input(" 2.sayıyı giriniz"))
print(ortalama(x,y))
f=5
print(faktoriyelbul(f))
