import pandas as pd
import numpy as np
import tensorflow as tf
from joblib import dump
from matplotlib import pyplot as plt

# Preprocessing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Keras
from keras import models
from keras import layers
from keras import callbacks

tf.keras.utils.set_random_seed(
    1
)
data = pd.read_csv('data/data.csv')
data.head()

# Dropping unnecessary columns
data = data.drop(['filename'], axis=1)
data.head()

genre_list = data.iloc[:, -1]
encoder = LabelEncoder()
y = encoder.fit_transform(genre_list)
print(y)

# normalizing
scaler = StandardScaler()
X = scaler.fit_transform(np.array(data.iloc[:, :-1], dtype=float))
dump(scaler, open('gtzan_scaler.bin', 'wb'), compress=True)  # save scaler
print("Saved scaler to disk as .bin")

# splitting of dataset into train and test dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)

# creating a model
model = models.Sequential()

model.add(layers.Dense(256, activation='relu', input_shape=(X_train.shape[1],)))
layers.Dropout(rate=0.3),  # apply 30% dropout to the next layer

model.add(layers.Dense(1028, activation='relu'))
layers.Dropout(rate=0.3),

model.add(layers.Dense(512, activation='relu'))
layers.Dropout(rate=0.3),

model.add(layers.Dense(512, activation='relu'))
layers.Dropout(rate=0.3),

model.add(layers.Dense(256, activation='relu'))
layers.Dropout(rate=0.3),

model.add(layers.Dense(128, activation='relu'))
layers.Dropout(rate=0.3),

model.add(layers.Dense(10, activation='softmax'))

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

early_stopping = callbacks.EarlyStopping(
    min_delta=0.002,  # minimum amount of change to count as an improvement
    patience=5,  # how many epochs to wait before stopping
    restore_best_weights=True,
)

history = model.fit(X_train,
                    y_train,
                    validation_data=(X_test, y_test),
                    epochs=200,
                    callbacks=[early_stopping],
                    batch_size=60)

# Calculate accuracy
test_loss, test_acc = model.evaluate(X_test, y_test)
print("Test Accuracy:", test_acc)

# Calculate accuracy on the training dataset
_, train_accuracy = model.evaluate(X_train, y_train)
print("Train Accuracy:", train_accuracy)

# Save the model as .h5
model.save("gtzan_model.h5")
print("Saved model to disk as .h5")

# show loss + val_loss
history_df = pd.DataFrame(history.history)
history_df.loc[0:, ['loss', 'val_loss']].plot()
plt.xlabel("epochs")
plt.ylabel("loss")
plt.title("loss + val_loss")
plt.savefig('gtzan_loss_val_loss_with_earlystopping.png')
plt.show()

# predictions
predictions = model.predict(X_test)
np.argmax(predictions[0])
