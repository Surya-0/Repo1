import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf

dataset = pd.read_csv('../Datasets/train.csv')
dataset = dataset.iloc[:,3:].values

X = dataset[:1826,:]

from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler(feature_range=(0, 1))
training_set_scaled = sc.fit_transform(X)

X_train_seq = []
y_train_seq = []
for i in range(60, 1826):
    X_train_seq.append(training_set_scaled[i-60:i, 0])
    y_train_seq.append(training_set_scaled[i, 0])
X_train_seq, y_train_seq = np.array(X_train_seq), np.array(y_train_seq)

X_train_seq = np.reshape(X_train_seq, (X_train_seq.shape[0], X_train_seq.shape[1], 1))

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout

regressor = Sequential()
regressor.add(LSTM(units = 50, return_sequences = True, input_shape = (X_train_seq.shape[1], 1)))
regressor.add(Dropout(0.2))
regressor.add(LSTM(units = 50, return_sequences = True, input_shape = (X_train_seq.shape[1], 1)))
regressor.add(Dropout(0.2))
regressor.add(LSTM(units = 50, return_sequences = True, input_shape = (X_train_seq.shape[1], 1)))
regressor.add(Dropout(0.2))
regressor.add(LSTM(units = 50))
regressor.add(Dropout(0.2))
regressor.add(Dense(units = 1))
regressor.compile(optimizer = 'adam', loss = 'mean_squared_error')

regressor.fit(X_train_seq, y_train_seq, epochs = 100, batch_size = 32)

y_pred = regressor.predict(X_train_seq)

from sklearn.metrics import mean_squared_error

mse = mean_squared_error(y_train_seq, y_pred)
print("Mean Squared Error:", mse)


y_pred = sc.inverse_transform(y_pred)
plt.plot(y_pred,color ='blue')
plt.show()

