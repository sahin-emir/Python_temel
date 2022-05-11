import sqlite3 as sql

vt=sql.connect(r"C:\Users\Beykent\Desktop\dene")
im=vt.cursor


##  okul:
##  öğrenci,ders,öğretmen
sorgu1="CREATE TABLE ogrenci(ogrenciNo INT PRIMARY KEY, ögrenciAd NVARCHAR(100),öğrencisoyad NVARCHAR(100))"

sorgu2="CREATE TABLE ogretmen(sicilNo INT PRIMARY KEY, öğretmenad NVARCHAR(100),öğretmensoyad NVARCHAR(100))"

sorgu3="CREATE TABLE ders(derskodu INT PRIMARY KEY , dersad NVARCHAR(100))"

im.execute(sorgu1)
im.execute(sorgu2)
im.execute(sorgu3)
vt.commit()


s1="INSERT INTO  ogrenci(1,'AHMET','ALİ')"

s2="INSERT INTO ogretmen(222,'AHMET','aaaa')"

s3="INSERT INTO  ders(1,'bilgisiyar')"


im.execute(s1)
im.execute(s2)
im.execute(s3)
vt.commit()
