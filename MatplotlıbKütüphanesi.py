## MATPLOTLIB
## VERİ GÖRSELLEŞTİRME
###

#import matplotlib.pyplot as plt
#import numpy as np

#plt.rcdefaults()

#x=np.linspace(0,4,360)
#y= np.sin(np.pi*x)


#fig,ax=plt.subplots()
#ax.fill(x,y)
#plt.show()

#import matplotlib.pyplot as plt
#import numpy as np
#plt.plot([[1,2,3,4,5,6],[1,2,3,44,55,12]])
#plt.ylabel("Numaralar")
#plt.xlabel("Data")

#plt.show()

#data=np.arange(0,5,0.2)
#plt.plot(data,data,'r--',data,data**2,'bs',data,data**3,'gs')
#plt.show()


import matplotlib.pyplot as plt
import numpy as np

isimler=['hazırlık','1.sınf','2.sınıf']
degerler=[1,10,100]

plt.figure(figsize=(9,3))
plt.subplot(131)
plt.bar(isimler,degerler)
plt.subplot(132)
plt.scatter(isimler,degerler)
plt.subplot(133)
plt.plot(isimler,degerler)
plt.show()
