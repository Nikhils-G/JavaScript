import tensorflow as tf
from tensorflow import keras
from kerastuner.tuners import Hyperband

# Example: Define a model-building function
def build_model(hp):
    model = keras.Sequential()
    model.add(keras.layers.Flatten(input_shape=(28, 28)))  # Example for MNIST dataset
    
    # Tune the number of hidden layers and units
    for i in range(hp.Int('num_layers', 1, 3)):
        model.add(
            keras.layers.Dense(
                units=hp.Int(f'units_{i}', min_value=32, max_value=256, step=32),
                activation='relu'
            )
        )
    
    # Output layer
    model.add(keras.layers.Dense(10, activation='softmax'))
    
    # Compile the model
    model.compile(
        optimizer=keras.optimizers.Adam(
            learning_rate=hp.Choice('learning_rate', [1e-2, 1e-3, 1e-4])
        ),
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    
    return model

# Load dataset (e.g., MNIST)
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

# Define the Hyperband tuner
tuner = Hyperband(
    build_model,
    objective='val_accuracy',
    max_epochs=20,
    factor=3,
    directory='my_dir',
    project_name='hyperband_mnist'
)

# Callback for early stopping
stop_early = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=5)

# Run the Hyperband search
tuner.search(
    x_train, y_train,
    epochs=50,
    validation_split=0.2,
    callbacks=[stop_early]
)

# Retrieve the best model
best_hps = tuner.get_best_hyperparameters(num_trials=1)[0]
print(f"""
The optimal number of layers is {best_hps.get('num_layers')} 
with units per layer {[best_hps.get(f'units_{i}') for i in range(best_hps.get('num_layers'))]} 
and a learning rate of {best_hps.get('learning_rate')}.
""")

# Build and train the best model
model = tuner.hypermodel.build(best_hps)
history = model.fit(x_train, y_train, epochs=10, validation_split=0.2)

# Evaluate the model
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"Test accuracy: {test_acc}")
