import random


kullanıcıpuan=50
pcpuan=50

while True:
    gir=int(input("1) Taş mı? 2) Kağıt mı? 3) Makas mı?"))
    a=int(random.uniform(1,3+1))
    print("bilgisayar", a,"seçti")

    if kullanıcıpuan<5 or pcpuan<5:
        print("oyun sonucu kullanıc puan",kullanıcıpuan,"bilgisiyar puan",pcpuan)
        if(pcpuan>5):
            print("Pc Kazandı",pcpuan)
        elif(kullanıcıpuan>5):
            print("kullanııc kazamndı",kullanıcıpuan)
        break
    else:

        if gir==1:
            if 2==a:
                print("berabere")
                kullanıcıpuan-=5
                pcpuan-=5
            elif 1==a:
                print("kazandınız")
                kullanıcıpuan+=5
                pcpuan-=5
            elif 3==a:
                print("kaybettiniz")
                kullanıcıpuan-=5
                pcpuan+=5

        elif gir==2:
            if 1==a:
                print("berabere")
                kullanıcıpuan-=5
                pcpuan-=5
            elif 2==a:
                print("kaybettiniz")
                kullanıcıpuan-=5
                pcpuan+=5
            elif 3==a:
                print("kazandınız")
                kullanıcıpuan +=5
                pcpuan-=5

        elif gir==3:

            if 3==a:
                print("berabere")
                kullanıcıpuan-=5
                pcpuan-=5
            elif 1==a:
                print("kaybettiniz")
                kullanıcıpuan-=5
                pcpuan+=5
            elif 2==a:
                print("kazandınız")
                kullanıcıpuan+=5
                pcpuan-=5

    