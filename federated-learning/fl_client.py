# FL Client
import flwr as fl
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train.reshape((-1, 784)).astype("float32") / 255.0, x_test.reshape((-1, 784)).astype("float32") / 255.0

model = models.Sequential([
    layers.Dense(128, activation='relu', input_shape=(784,)),
    layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

def train(model, x, y, epochs=1, batch_size=32):
    model.fit(x, y, epochs=epochs, batch_size=batch_size, verbose=1)

def evaluate(model, x, y):
    loss, accuracy = model.evaluate(x, y, verbose=0)
    return loss, accuracy

class FLClient(fl.client.NumPyClient):
    def get_parameters(self, config):
        return model.get_weights()

    def fit(self, parameters, config):
        model.set_weights(parameters)
        train(model, x_train, y_train)
        return model.get_weights(), len(x_train), {}

    def evaluate(self, parameters, config):
        model.set_weights(parameters)
        loss, accuracy = evaluate(model, x_test, y_test)
        return loss, len(x_test), {"accuracy": accuracy}

fl.client.start_numpy_client(server_address="localhost:8080", client=FLClient())