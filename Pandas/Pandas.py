import numpy as np
import pandas as pd
# #Series

# # my_dict = { "Samet" : 20, 
# #             "Mert" : 24,
# #             "Boran" : 25}

# # print(pd.Series(my_dict))
# # my_ages = [20,24,25]
# # my_names = ["Samet","Mert","Boran"]

# # # # # print(pd.Series(my_ages,my_names))
# # # # # print(pd.Series(data = my_ages, index=my_names))
# # array_of_nump = np.array(my_ages)
# # # print(array_of_nump)
# # print(pd.Series(array_of_nump))
# # print(pd.Series(array_of_nump,my_names))

# # #SeriesOzellikleri 

# print(pd.Series(["Samet","Mehmet","Osman","Ali"],[1,2,3,4]))

# # result_of_comp = pd.Series([10,15,20,24],["Samet","Mehmet","Osman","Ali"])
# # print(result_of_comp)

# # result_of_comp1 = pd.Series([8,9,4,6],["Samet","Mehmet","Osman","Ali"])
# # print(result_of_comp1)

# # print(result_of_comp1["Mehmet"])
# # last_result = result_of_comp + result_of_comp1
# # print(last_result)#
# # diff_series = pd.Series([30,25,40,50],["a","b","c","d"])
# # diff_series2 = pd.Series([10,5,3,1],["a","c","f","g"])      #Girilen iki dizide indeksler uyuşmuyorsa NAN değeri atar 


# # last_diff = pd.DataFrame(diff_series + diff_series2)
# # last_diff.fillna(25,inplace=True)
# # print(last_diff)


# # print(0.1+0.2)


# #DATAFRAME

# # data = np.random.randn(4,3)
# # # print(data)

# # data_frame = pd.DataFrame(data)
# # # print(data_frame)
# # # print(data_frame[0])

# # new_data_frame = pd.DataFrame(data,index = ["Samet","Boran","Mehmet","Osman"],columns=["Maas","Yas","Calisma Saati"])
# # # print(new_data_frame)
# # # print(new_data_frame["Yas"])
# # # print(new_data_frame[["Maas","Calisma Saati"]])
# # # # # print(new_data_frame.loc["Samet"])    Sadece Sametin satırı
# # # # # print(new_data_frame.loc["Mehmet"])   Sadece Mehmetin satırı 
# # # print(new_data_frame.iloc[2])
# # # # # print(new_data_frame["Maas"])
# # new_data_frame ["Emeklilik Yasi"] = [1,2,3,4]    #Yeni kolon ekleme
# # # print(new_data_frame)
# # print(new_data_frame.drop("Emeklilik Yasi",axis=1))     #Sütunu silme
# # # # print(new_data_frame.drop("Samet"))       #Hali hazırda bulunan data framei silmeye kalkarsak onu ayrıca belirtmemiz gerekiyor dropta bu olmaz.
# # new_data_frame.drop("Emeklilik Yasi",axis=1,inplace=True)    #inplace = True, gerçekten silmek için #Default değeri False
# # # #print(new_data_frame)
# # # # print(new_data_frame.loc["Samet"]["Yas"])   #Sametin yasi

# # # # print(new_data_frame.loc["Mehmet","Yas"])
# # deger = new_data_frame < 0
# # print(new_data_frame[deger])    #Tabloda 0dan kücük olan degerleri gösterir.
# # print(new_data_frame[new_data_frame < 0 ])      #Üst satır ile aynı anlama geliyor.

# #print(new_data_frame[new_data_frame["Yas"] > 0 ])       #Yası 0'dan büyük olan rowları getir

# # #Indeks islemleri 
# # print(new_data_frame.reset_index(inplace=True))     #İnplace kullanılmadıysa tekrardan aynı hale gelir.

# # new_index_list = ["Samet","Brn","Mht","Osmn"]
# # new_data_frame ["New Indeks"] = new_index_list  #Olusturulan listeyi new_data_framein icine indeks olarak aktarmak
# # # print(new_data_frame)
# # new_data_frame.set_index("New Indeks",inplace=True)     #Köklü degisim
# # print(new_data_frame)
# # print(new_data_frame.loc["Samet"])

# # firs_index = ["Simpson","Simpson","Simpson","South Park","South Park","South Park"]
# # inner_index = ["Homer", "Bart", "Marge", "Cartman","Kenney","Kyle"]

# # # #Dizileri olusturduktan sonra birlestirme
# # birlestirilmis_indeks = list(zip(firs_index,inner_index))
# # print(birlestirilmis_indeks)
# # birlestirilmis_indeks = pd.MultiIndex.from_tuples(birlestirilmis_indeks)
# # print(birlestirilmis_indeks)   #Birlestirme islemi yapildi Multi Index ile 

# # type(birlestirilmis_indeks)#pandas.core.multiindex

# # my_cartoon_list = [[40,"A"],[10,"B"],[30,"C"],[9,"D"],[10,"E"],[11,"F"]]
# # my_cartoon_list_np = np.array(my_cartoon_list)
# # my_cartoon_list_pd = pd.DataFrame(my_cartoon_list_np,index=birlestirilmis_indeks,columns=["Yas","Meslek"])

# # print(my_cartoon_list_pd)#Bütün verileri birleştirip tablo olusturduk
# # # #print(my_cartoon_list_pd.loc["Simpson"])#Sadece simpsonları getir
# # # #print(my_cartoon_list_pd["South Park"])# ""     southparkı  ""
# # # #print(my_cartoon_list_pd.loc["South Park"].loc["Kenney"])      Sadece Kenneyi getir
# # my_cartoon_list_pd.index.names = ["Film adi","İsim"]    #İsim ve film adi adli baslık olustur
# # print(my_cartoon_list_pd)

# #Pandas Operasyonlar(Eksik Veri)
# data_dict = {"Istanbul": [30,29,np.nan],
#              "Ankara": [20,np.nan,25],
#              "Izmir": [40,39,38]
#               }
# havaDurumuDataFrame = pd.DataFrame(data_dict)
# #print(havaDurumuDataFrame)
# #print(havaDurumuDataFrame.dropna(axis=1))   #Nan olmayan sütunu al getir
# new_data_dict = {"Istanbul": [30,29,np.nan],
#              "Ankara": [20,np.nan,25],
#              "Izmir": [40,39,38],
#              "Antalya": [45,np.nan,np.nan]
#               }
# new_data_frame = pd.DataFrame(new_data_dict)
# print(new_data_frame)
# print(new_data_frame.dropna(axis=1,thresh=1))#thresh= = limit 
# # new_data_frame.fillna(25,inplace=True)  #Eksik olan verileri kalıcı olarak 25 ile doldurur. 

# #print(new_data_frame)

# #Pandas Operasyonlar(groupby)
# dict_of_salary = {
#     "Department" : ["Yazilim","Yazilim","Pazarlama","Pazarlama",
#                     "Hukuk","Hukuk"],
#     "Calisan Ismi" : ["Ahmet","Mehmet","Atil","Burak","Zeynep","Fatma"],
#     "Maas"         : [100,150,200,300,400,500]
# }
# dict_of_salary_dataframe= pd.DataFrame(dict_of_salary)
# #print(dict_of_salary_dataframe)

# group_object = dict_of_salary_dataframe.groupby("Department")
# print(group_object.count())    #Hangi departmanda kaç kişi çalışıyor
# #print(group_object.mean("Maas"))     #Departmandaki maasların ortalaması
# #print(group_object.min("Maas")) #Minimum maası getir Max ile maximum da getirilir.

# #print(group_object.describe()) #Bütün istatistikleri getirir.(STD,MEAN,MAX,MİN,25,50,75)





#PandasOperationsDevamı     
#Farklı data frameleri birlestirme(Concat)
# dict1 =  {
#     "Isim" : ["Ahmet","Mehmet","Zeynep","Atil"],
#     "Spor" : ["Kosu","Yuzme","Kosu","Basketbol"],
#     "Kalori" : [100,200,150,300]
# }
# df1= pd.DataFrame(dict1,index=[0,1,2,3])

# dict2 =  {
#     "Isim" : ["Osman","Levent","Atlas","Fatma"],
#     "Spor" : ["Kosu","Yuzme","Kosu","Basketbol"],
#     "Kalori" : [200,400,250,300]
# }
# df2 = pd.DataFrame(dict2,index=[4,5,6,7])
# dict3 =  {
#     "Isim" : ["Ayşe","Mahmut","Duygu","Nur"],
#     "Spor" : ["Kosu","Yuzme","Badminton","Tenis"],
#     "Kalori" : [400,200,40,300]
# }
# df3 = pd.DataFrame(dict3,index=[8,9,10,11])
# #concatenation
# df_concat = pd.concat([df1,df2,df3])    #axis default = 0 (satır),1 girersek yan yana birlestirmeye çalışır
# print(df_concat)



#Merge(Birlestirmek(Kaynastırmak))

# merge_dict1 = {
#     "Isim" : ["Ahmet", "Mehmet", "Zeynep", "Atil"],
#     "Spor" : ["Kosu", "Yuzme", "Kosu", "Basketbol"]
# }
# merge_dict1_df1 = pd.DataFrame(merge_dict1)

# merge_dict2 = {
#     "Isim" : ["Ahmet", "Mehmet", "Zeynep", "Atil"],
#     "Kalori" : [100, 200, 150, 250]
# }
# merge_dict2_df2 = pd.DataFrame(merge_dict2)
# merge_df_all = pd.merge(merge_dict1_df1,merge_dict2_df2,on="Isim") #Hangi kolon üstünden ortak islem yapılacaksa on = üzerinde belirtilir.
# print(merge_df_all)


##PandasOperations

# salary_dict = {
#     "Isim" : ["Atil","Boran","Mehmet","Samet"],
#     "Department" : ["Yazilim","Satis","Pazarlama","Yazilim"],
#     "Maas" : [200,300,400,500]
# }
# salary_df =pd.DataFrame(salary_dict,index=[0,1,2,3])
# # print(salary_df["Department"].unique())     #Departmanda tekrarlanan verileri getirmez.unique()
# # print(salary_df["Department"].nunique())    #Number of unique sayisal olarak verir.
# # print(salary_df["Department"].value_counts())   #Hangi departmandan kaç tane insan var onu gösterir.

# def brut_to_net(maas):
#     return maas * 0.66

#print(salary_df["Maas"].apply(brut_to_net))     #Maas alanındaki sayilari 0.66 ile çarp. apply(fonksiyon) uygula.
#print(salary_df.isnull())   #DataFramede null değeri var mı onu kontrol et true false döndürür<<<.

# #new_data_dict = {
#     "Karakter Sinifi" : ["South Park", "South Park", "Simpson", "Simpson", "Simpson"],
#     "Karakter Ismi" : ["Cartman", "Kenny", "Homer", "Bart", "Bart"],
#     "Karakter Yas" : [9, 10, 50, 20, 10]
# }
#new_data_df = pd.DataFrame(new_data_dict)
#print(new_data_df.pivot_table(values="Karakter Yas", index= ["Karakter Sinifi", "Karakter Ismi"],aggfunc=np.sum))       #AGGFUNC İLE BART TEKRARLANAN VERİ OLDUGU İCİN DEĞERLERİNİ TOPLAYARAK EKRANA YAZDİR. 

#PandasExcel

# maas_df = pd.read_excel("maas.xlsx")
# doludegerler = maas_df.dropna()
# print(doludegerler)
# print(maas_df)
# doludegerler.to_excel("Yeni Maas.xlsx")     #Excele yaz
#read_csv to_csv        Eğer excel csv formatında gelirse.

