import numpy as np 
##Numpy array
# my_list = [10,20,30,40]

# np.array(my_list)

# matrix_list = [[10,20,30],[30,40,50],[20,60,80]]
# print(np.array(matrix_list))

#arange
# print(np.arange(0,10))
# np.arange(0,20,2)



#zeros
# print(np.zeros((4,4)))  # 0 lardan 4e4 matris oluşturuyor.

#ones
# print(np.ones((6,6)))      #1 lerden 6ya6 "" "".

#linspace ! 
# print(np.linspace(0,100,5))  #ilk verilen değerden ikinci değere kadar 'girilen parametre' eşit aralıkla yaz.

#eye 
# print(np.eye(15))

# my_list = np.linspace(10,100,10)
# print(my_list)

# np random
# print(np.random.randint(0,100,8))
# print(np.random.randn(3,3))


# #NNumpy dizi methods
# my_numpy_list = np.arange(30)
# # print(my_numpy_list)

# my_random_list = np.random.randint(0,200,6)
# print(my_random_list)

# print(my_numpy_list.reshape(5,6))     #Girilen veya alınan değerleri istediğimiz şekilde şekillendirir.
# # print(my_numpy_list.min())## min = minimum değer max = maximum değer

# print(my_random_list.argmax()) ##Dizide en büyük değerin indeksi
# print(my_random_list.argmin()) ## Dizide en kücük değerin indeksi

# my_numpy_list.shape ## Dizinin hangi halde kullanildiğina erismek icin

# np_shape_list = my_numpy_list.reshape(5,6)
# print(np_shape_list.shape)

#numpydizi
# # my_array = np.arange(0,15)
# # print(my_array)

# # print(my_array[5])
# # print(my_array[3:5])

# # my_array[3:8] = -5 
# # print(my_array)       3.indeksten 8.indekse kadar -5 yapar.

# array = np.arange(0,24)
# slicin_array = array [4:9]
# print(slicin_array)

# slicin_array [:] = 1            #bütün elemanlari 1 yapar
# print(slicin_array)
# print(array)


# ornek = np.arange(0,24)
# ornek_kopya = ornek.copy()

# ornek_slicing = ornek_kopya[3:6]      Elemanların etkilenmemesi için copy atıp onun üzerinde islemleri gerceklestirdik.
# ornek_slicing [:] = 800
# print(ornek_slicing)
# print(ornek_kopya)
# print(ornek)

##Matrix

# my_list = [[10,20,30],[20,30,40],[40,50,60]]
# array_matrix = np.array(my_list)
# print(array_matrix)
# print(array_matrix[1,2])
# print(array_matrix[1:,2])

# my_list = [[0,1,2,3,4],[5,6,7,8,9],[10,11,12,13,14],[15,16,17,18,19],[20,21,22,23,24]]
# new_matrix = np.array(my_list)
# print(new_matrix[[0,2,4]])


##Numpy Operasyonlar

# new_list = np.random.randint(1,100,20)
# print(new_list)
# # print(new_list>24)  #24den büyük sayıları boolean olarak döndürür.Bunu bir degiskene de aktarabiliriz.
# result_array = new_list > 24
# print(new_list[result_array]) #  == new_list[new_list > 24 ]

# last_array = np.arange(0,24)
# print(last_array)
# # print(last_array + last_array)
# # print(last_array * last_array)
# # print(last_array - last_array)
# # print(last_array / last_array) # 0 = nan 
# print(np.sqrt(last_array))      #Karekökünü alma
# print(np.max(last_array))
# print(np.min(last_array))

# my_new_array = np.arange(0,100,9)
# print(my_new_array)
# print(my_new_array.reshape(4,3))

my_list = np.random.randint(0,100,9)
sonuc = my_list > 24 
print(sonuc)