# Defining parameters for performing GridSearch
# optimizer = ['sgd', 'rmsprop', 'adam']
# dropout_rate = [0.1, 0.2, 0.3, 0.4, 0.5]
# input_layer_nodes = [50, 107, 150, 200]
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import GridSearchCV

kernel_initializer = ['uniform', 'normal']

param_grid = dict(kernel_initializer = kernel_initializer)

model = KerasClassifier(build_fn = base_model, epochs = 10, batch_size = 128, verbose = 2)

grid = GridSearchCV(estimator = model, param_grid=param_grid, n_jobs = 1, cv = 5)
grid.fit(X_train, y_train)

# View hyperparameters of best neural network
print("\nBest Training Parameters: ", grid.best_params_)
print("Best Training Accuracy: ", grid.best_score_)