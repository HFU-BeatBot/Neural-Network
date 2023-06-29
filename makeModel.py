def makeModel(csvFilePath='data.csv'):
    import librosa
    import pandas as pd
    import numpy as np

    from joblib import dump
    from matplotlib import pyplot as plt

    # Preprocessing
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import LabelEncoder, StandardScaler

    # Keras
    from keras import models
    from keras import layers
    from keras import callbacks

    # Read the CSV file
    data = pd.read_csv(csvFilePath)
    data = data.iloc[:, 1:]
    data.head()

    # Extract the genre labels and encode them
    genre_list = data.iloc[:, -1]
    encoder = LabelEncoder()
    y = encoder.fit_transform(genre_list)
    print(y)

    # Normalize the data using StandardScaler
    scaler = StandardScaler()
    X = scaler.fit_transform(np.array(data.iloc[:, :-1], dtype=float))
    dump(scaler, open('scaler.bin', 'wb'), compress=True)  # Save the scaler
    print("Saved scaler to disk as .bin")

    # Split the dataset into train and test datasets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)

    # Create a model
    model = models.Sequential()

    model.add(layers.Dense(256, activation='relu', input_shape=(X_train.shape[1],)))
    layers.Dropout(rate=0.3),  # Apply 30% dropout to the next layer

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
        min_delta=0.002,  # Minimum amount of change to count as an improvement
        patience=5,  # How many epochs to wait before stopping
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

    model.save("model.h5")  # Export the model as .h5
    print("Saved model to disk as .h5")
    print('test_acc: ', test_acc)

    # Show loss + val_loss
    history_df = pd.DataFrame(history.history)
    history_df.loc[0:, ['loss', 'val_loss']].plot()
    plt.xlabel("epochs")
    plt.ylabel("loss")
    plt.title("loss + val_loss")
    plt.savefig('loss_val_loss_with_earlystopping.png')
    plt.show()

    # Make predictions
    predictions = model.predict(X_test)
    np.argmax(predictions[0])
