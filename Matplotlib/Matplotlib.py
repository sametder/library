# MatplotlibGiris 
#Kilo'nun Yasa Göre Degisimini gösteren grafik
import numpy as np
import matplotlib.pyplot as plt

# age_list = [10, 20, 31, 28, 30, 41, 50, 9, 8, 7]
# kilo_list = [20, 61, 75, 66, 68, 72, 83, 14, 13, 14]

# # Listeleri numpy ile array'e aktarma
# age_list_numpy = np.array(age_list)
# kilo_list_numpy = np.array(kilo_list)

# # Çizgi grafiğini oluştur
# plt.plot(age_list_numpy, kilo_list_numpy, "b")
# plt.xlabel("Yas")       #X ekseninin ismi
# plt.ylabel("Kilo")      #Y ekseninin ismi
# plt.title("Kilo'nun Yasa Göre Degisimi")

# # Çizimi ekranda göster
# plt.show()

#matplotlib devami
np_array1 = np.linspace(0,10,20)
np_array2 = np_array1**3
# plt.plot(np_array1,np_array2,"g--") #g-- deki kesik çizgilerin anlami grafikteki çizginin kesik kesik olması için örn = g*-
# plt.xlabel("Numpy1")
# plt.ylabel("Numpy2")
# plt.title("Numpy Calismalari")
# plt.show()

#iki grafik yapma
# plt.subplot(1,2,1)
# plt.plot(np_array1,np_array2,"r*-")
# plt.subplot(1,2,2)#1 Sıra olacak, 2kolon olacak, şu an 2.grafigi ciziyorum
# plt.plot(np_array2,np_array1,"b--")
# plt.show()
#Figure
# my_figure = plt.figure()
# #x ve y ekseni ekleyip boyut belirtelim.

# figureAxes = my_figure.add_axes([0.2,0.2,0.7,0.7])  #x ekseni başlangıç noktası, y ekseni başlangıç noktası, genişlik, uzunluk
# figureAxes.plot(np_array1,np_array2,"g--")
# figureAxes.set_xlabel("X Ekseni Veri Ismi")
# figureAxes.set_ylabel("Y Ekseni Veri Ismi")
# figureAxes.set_title("Grafik Basligi")
# plt.show()

# my_figure2 = plt.figure()

# eksen1 = my_figure2.add_axes([0.1,0.1,0.9,0.9])
# eksen2 = my_figure2.add_axes([0.3,0.6,0.3,0.3])
# eksen1.plot(np_array1,np_array2,"g")
# eksen1.set_xlabel("X Ekseni")
# eksen1.set_ylabel("Y Ekseni")
# eksen1.set_title("Ana Grafik Baslik")

# eksen2.plot(np_array2,np_array1,"b")
# eksen2.set_xlabel("X Ekseni")
# eksen2.set_ylabel("Y Ekseni")
# eksen2.set_title("Kucuk Grafik Baslik")
# plt.show()


# (benimFigure, benimEksenler) = plt.subplot(nrows = 1, ncols = 2 )

# for eksen in benimEksenler:
#     eksen.plot(np_array1, np_array2,"g")
#     eksen.set_xlabel("X Ekseni")
# plt.tight_layout()      # İki grafik arasındaki boslugu düzeltir.
# plt.show(benimEksenler)




# newFigure = plt.figure(figsize=(7,4),dpi=115)       #figsize = (7,3) boyutunu ayarlamak için        dpi= çözünürlük ayarlamak için 

# new_eksen = newFigure.add_axes([0.1,0.1,0.9,0.9])
# new_eksen.plot(np_array1,np_array2,"r--",label = " Numpy Dizisi ** 3")     #label = etiket
# new_eksen.plot(np_array1,np_array1 ** 4,"b*-", label = " Numpy Dizi ** 4")
# new_eksen.legend(loc = 1)       #Loc = etiketin nerede bulunmasini istiyorsak bu komutla ayarlıyoruz.
# plt.show()
# newFigure.savefig("Benim Figürüm.png",dpi = 115)    #Figürün kaydedilmesi için

##Matplotlib Gelişmiş Seviye

# (benim_figur, benimEksen) = plt.subplots()
# benimEksen.plot(np_array1,np_array2,color = "#3A95A8",alpha = 0 .7)    # color = rgb hex code ile istediğimiz renkleri kullanabiliriz. Alpha komutu ile saydamlığıda değiştirebiliriz.
# benimEksen.plot(np_array2,np_array1,color = "#C96F23")

# (yeniFigur, yeniEksen) = plt.subplots()

# yeniEksen.plot(np_array1, np_array1 + 2, color = "black", linewidth=4.5)    #linewidth ile çizgi kalınlığını ayarlayabiliriz
# yeniEksen.plot(np_array1, np_array1 + 3, color = "gray", linewidth=3)
# yeniEksen.plot(np_array1, np_array1 + 4, color = "pink", linestyle = "dashed", linewidth=2.0, alpha=1)  #linestyle ile çizgi şeklini değiştirebiliriz.
# yeniEksen.plot(np_array1, np_array1 + 5, color = "yellow", linestyle="-.", alpha=1)
# yeniEksen.plot(np_array1, np_array1 + 6, color = "brown", linestyle=":",alpha=1)
# yeniEksen.plot(np_array1, np_array1 + 7, color = "purple", linestyle="--", marker="o", markersize = 4, markerfacecolor="red")   #markersize ile markerın büyüklüğünü facecolor ile de içini boyayabiliriz.
# yeniEksen.plot(np_array1, np_array1 + 8, color = "green", linestyle = ":", marker="+",markersize = 7, markerfacecolor="blue")


#Scatter

# plt.scatter(np_array1,np_array2) # araları bosluklu daireler gösterir
# plt.show()

#Histogram

new_array = np.random.randint(0, 100, 50)   #düz bloklar halinde gösterir
# plt.hist(new_array)
# plt.show()

#boxplot    Bir kutu olusturup onun etrafında dağılımı gösterir.
plt.boxplot(new_array)
plt.show()