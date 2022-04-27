import os 

#os.getcwd()
## dosyanın bulunduğu klassörde çalışacak 
  
#dosyagir=open("ilkdsosya.txt","w")

#def dosyaoku(isim):
#    oku=open(isim,"r")
#    return oku

#dosyaoku("ilkdsosya.txt")

## dosya=open("C:\\Users\\Beykent\\Desktop\\deneme\\a1.docx","w")farklı dosyada açma

os.getcwd()

    # listedeki elemanları yazdırma
#dosya=open("beykenty2.txt","w")
#liste=["ayva\n","elma\n"]

#dosya.writelines(liste)
##for i in liste:
##    dosya.write(i)


        # dosyaya yazı yazma 
#dosya=open("beykent.txt","w")
#dosya.write("Gerekli yazılar buyraya yazılcak ")
#dosya.write("\ Gerekli yazılar buyrayaiii yazılcak ")

os.remove("ilkdsosya.txt")
try:
    dosya=open("beykenty2.txt")
    print(dosya.read())
    print(dosya)
except:
    print("dosya bulunamadı")
