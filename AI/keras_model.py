import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

df = pd.read_csv("AI_test.CSV")

x = df.drop("y",axis=1)
y = df["y"]

x_train, x_val, y_train, y_val = train_test_split(x,y,test_size=0.3)

x_val, x_test, y_val, y_test = train_test_split(x_val,y_val,test_size=0.2)

keras.backend.clear_session()

model = keras.models.Sequential()

model.add(keras.layers.InputLayer(input_shape = x_train.shape[1:]))

model.add(keras.layers.Dense(8,activation="linear"))
model.add(keras.layers.Dense(16,activation="linear"))
model.add(keras.layers.Dense(32,activation="linear"))

model.add(keras.layers.Dense(1,activation="linear"))

model.compile(loss = "mse" , optimizer="adam",metrics=[keras.metrics.RootMeanSquaredError()])

model.summary()

es = keras.callbacks.EarlyStopping(monitor="val_loss",min_delta=0,patience=5,verbose=1,restore_best_weights=True)

history = model.fit(x_train,y_train,epochs=100,verbose=1,callbacks=[es],validation_data=(x_val,y_val))

y_pred = model.predict(x_test)

print(mean_squared_error(y_test,y_pred))