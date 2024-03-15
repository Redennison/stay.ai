### Importing the libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, accuracy_score

### Importing the dataset

dataset = pd.read_csv('Churn_Modelling.csv')
x = dataset.iloc[:, 3:-1].values
y = dataset.iloc[:, -1].values

"""### Encoding categorical data

Label Encoding the "Gender" column
"""

le = LabelEncoder()
x[:,2] = le.fit_transform(x[:,2])

### One Hot Encoding the "Geography" column

ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [1])], remainder='passthrough')
x = np.array(ct.fit_transform(x))

### Splitting the dataset into the Training set and Test set

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

### Feature Scaling

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

### Initializing the ANN

ann = tf.keras.models.Sequential()

### Adding the input layer and the first hidden layer

ann.add(tf.keras.layers.Dense(units=6, activation='relu'))

### Adding the second hidden layer

ann.add(tf.keras.layers.Dense(units=6, activation='relu'))

### Adding the output layer

ann.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))

### Compiling the ANN

ann.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

### Training the ANN on the Training set"""

ann.fit(X_train, y_train, batch_size=32, epochs=100)

### Predicting the result of a single observation

print(ann.predict(sc.transform([[1, 0, 0, 600, 1, 40, 3, 60000, 2, 1, 1, 50000]])))

"""### Predicting the Test set results"""

y_pred = ann.predict(X_test)
y_pred = y_pred > 0.5
print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test), 1)), 1))

"""### Making the Confusion Matrix"""

cm = confusion_matrix(y_test, y_pred)
print(cm)
accuracy_score(y_test, y_pred)