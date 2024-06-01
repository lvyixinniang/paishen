from keras import layers
from keras.models import Sequential
from keras.datasets import mnist
from keras.utils import to_categorical

model = Sequential([
  layers.Conv2D(32, (3, 3), input_shape=(28, 28, 1)),
  layers.PReLU(),
  layers.MaxPool2D(pool_size=(2, 2)),
  layers.Flatten(),
  layers.Dense(32, activation='relu'),
  layers.Dense(10, activation='softmax')
])
model.summary()
model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])

(train_imgs, train_labels), (test_imgs, test_labels) = mnist.load_data()

train_imgs = train_imgs / 255.0
test_imgs = test_imgs / 255.0

train_imgs = train_imgs.reshape(-1, 28, 28, 1)
test_imgs = test_imgs.reshape(-1, 28, 28, 1)

train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

history = model.fit(train_imgs, train_labels, epochs=12, batch_size=64, validation_split=0.2)

evaluate_res = model.evaluate(test_imgs, test_labels, batch_size=64)
print(evaluate_res)

import matplotlib.pyplot as plt

history_dict = history.history
acc = history_dict['accuracy']
val_acc = history_dict['val_accuracy']
loss = history_dict['loss']
val_loss = history_dict['val_loss']
epochs = range(1, len(acc) + 1)

plt.plot(epochs, acc, 'b', label='Training acc')
plt.plot(epochs, val_acc, 'r', label='V acc')
plt.title('Training and validation accuracy')
plt.legend()
plt.figure()

plt.plot(epochs, loss, 'b', label='Training loss')
plt.plot(epochs, val_loss, 'r', label='Validation loss')
plt.title('Training and validation loss')
plt.legend()

plt.show()