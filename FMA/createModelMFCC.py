import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from joblib import dump

# Keras
from keras import models, layers, callbacks

# Read the dataset
data = pd.read_csv('data/fma_metadata/data.csv')
data.head()

# Dropping unnecessary columns
data = data.drop(['filename'], axis=1)
data.head()

# Extract genre labels and encode them
genre_list = data.iloc[:, -1]
encoder = LabelEncoder()
y = encoder.fit_transform(genre_list)
print(y)

# Normalizing the data
scaler = StandardScaler()
X = scaler.fit_transform(np.array(data.iloc[:, :-1], dtype=float))
dump(scaler, open('../scaler.bin', 'wb'), compress=True)  # Save scaler
print("Saved scaler to disk as .bin")

# Split dataset into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)

# Create a model
model = models.Sequential()
model.add(layers.Dense(256, activation='relu', input_shape=(X_train.shape[1],)))
model.add(layers.Dropout(rate=0.3))  # Apply 30% dropout to the next layer

model.add(layers.Dense(1028, activation='relu'))
model.add(layers.Dropout(rate=0.3))

model.add(layers.Dense(512, activation='relu'))
model.add(layers.Dropout(rate=0.3))

model.add(layers.Dense(512, activation='relu'))
model.add(layers.Dropout(rate=0.3))

model.add(layers.Dense(256, activation='relu'))
model.add(layers.Dropout(rate=0.3))

model.add(layers.Dense(128, activation='relu'))
model.add(layers.Dropout(rate=0.3))

model.add(layers.Dense(10, activation='softmax'))

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

early_stopping = callbacks.EarlyStopping(
    min_delta=0.002,
    patience=5,
    restore_best_weights=True,
)

# Train the model
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
model.save("fma_model.h5")
print("Saved model to disk as .h5")

# Show loss + val_loss
history_df = pd.DataFrame(history.history)
history_df.loc[0:, ['loss', 'val_loss']].plot()
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.title("Loss + Val_loss")
plt.savefig('loss_val_loss_with_earlystopping.png')
plt.show()

# Predictions
predictions = model.predict(X_test)
np.argmax(predictions[0])
