from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.layers import Embedding
from keras.layers import Conv1D, GlobalAveragePooling1D, MaxPooling1D
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
import numpy as np


#keras.layers.Conv1D(filters, kernel_size, strides=1, padding='valid', data_format='channels_last', dilation_rate=1, activation=None, use_bias=True, kernel_initializer='glorot_uniform', bias_initializer='zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)

#CNN network
model = Sequential()
model.add(Conv1D(32, 5, activation='relu', input_shape=(600,1)))
model.add(Conv1D(64, 1, activation='relu'))
model.add(MaxPooling1D(1))
model.add(Conv1D(128, 1, activation='relu'))
model.add(Conv1D(128, 1, activation='relu'))
model.add(GlobalAveragePooling1D())
model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy',optimizer='rmsprop',metrics=['accuracy'])
    
#Data Splitting
X_train, X_test, y_train, y_test = train_test_split(dataset, labels, test_size=0.1, random_state=0)

#training
model.fit(X_train, y_train, batch_size=20, epochs=1)

#evaluate
score = model.evaluate(X_test, y_test, batch_size=15)
#print(score)

#Prediction-No
a=np.expand_dims(dataset[23000], axis=0)
output=model.predict(a)
print(output)


#Prediction-Yes
a=np.expand_dims(dataset[100], axis=0)
output=model.predict(a)
print(output)

#Cross-Validation
#scores = cross_val_score(model, dataset, labels, cv=10, scoring='accuracy')  
#Does work with scikit because you need to wrap it in scikit wrapper
 