import numpy as np # linear algebra
import pandas as pd
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
import pickle
import maths


import warnings
df = pd.read_csv("datasheet_final.csv")

df= df.dropna(axis = 1, how = 'all')
new_df=df.drop(['weight','height','heart_pulse','muscle_mass','hydration','bone_mass','pulse_wave_velocity',,'systolic','diastolic','TEMP','SPO2'],axis=1)

df=new_df.values

X= df[:,0:4]
Y=df[:,4]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25)

model = Sequential()
model.add(Dense(32, input_dim=4, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

model.fit(X_train, Y_train, batch_size=32, epochs=150,)


pickle.dump(model,open('dumpfile.pkl','wb'))
model=pickle.load(open('dumpfile.pkl','rb'))


