import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sb 
import tensorflow as tf 
from sklearn.model_selection import train_test_split as tts 
from keras.models import Sequential
from keras.layers import Dense 
from sklearn.preprocessing import MinMaxScaler


# import tensorflow as tf 
# from tensorflow import keras
# from tensorflow.python.keras.models import Sequential, load_model
# from tensorflow.python.keras.layers import LSTM, Dense



data_frame = pd.read_excel("bisiklet_fiyatlari.xlsx")
print(data_frame)     

# seaborn 
# sb.pairplot(data_frame)
# plt.show()


## Test/Train Data
#train_test_split

y = data_frame["Fiyat"].values
# print(y)
#x -> feature(özellik)
x = data_frame[["BisikletOzellik1","BisikletOzellik2"]].values

x_train, x_test, y_train, y_test = tts(x, y, test_size=0.45, random_state=15)
# print(x_train.shape)
# print(x_test.shape)
# print(y_train.shape)
# print(y_test.shape)

#scaling

scaler = MinMaxScaler()
scaler.fit(x_train)
x_train = scaler.transform(x_train)     #Fit ettiğimiz xtraini eşitledik
x_test = scaler.transform(x_test)       #""     ""       xtest  ""
# print(x_test)

model = Sequential()

model.add(Dense(4, activation="relu"))
model.add(Dense(4, activation="relu"))
model.add(Dense(4, activation="relu"))

model.add(Dense(1))

model.compile(optimizer="rmsprop", loss="mse")#mse regression 
model.fit(x_train, y_train, epochs=2)