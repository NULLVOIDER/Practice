import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix
print('TensorFlow version: ', tf.__version__)
data_train = pd.read_csv('../input/fashion-mnist_train.csv')
data_test = pd.read_csv('../input/fashion-mnist_test.csv')
data_train.head(3)
data_test.head(3)
print("Size of:")
print("- Training-set:\t\t{}".format(len(data_train)))
print("- Test-set:\t\t{}".format(len(data_test)))
IMAGE_CLASSES = {
    0: 'T-shirt/top',
    1: 'Trouser',
    2: 'Pullover',
    3: 'Dress',
    4: 'Coat',
    5: 'Sandal',
    6: 'Shirt',
    7: 'Sneaker',
    8: 'Bag',
    9: 'Ankle boot'
}
X_train = np.array(data_train.iloc[:, 1:])
y_train = np.array(data_train.iloc[:, 0])
X_test = np.array(data_test.iloc[:, 1:])
y_test = np.array(data_test.iloc[:, 0])
img_size = 28
img_size_flat = img_size * img_size
img_shape = (img_size, img_size)
num_channels = 1
num_classes = 10
images = X_train[0:9]
cls_true = y_train[0:9]
plot_images(images=images, cls_true=cls_true)
plot_images(images=images, cls_true=cls_true)
def new_conv_layer(input,
                   num_input_channels,
                   filter_size,
                   num_filters,
                   use_pooling=True):
                              shape = [filter_size, filter_size, num_input_channels, num_filters]
                              weights = new_weights(shape=shape)
                              biases = new_biases(length=num_filters)
                              layer = tf.nn.conv2d(input=input,
                              filter=weights,
                              strides=[1, 1, 1, 1],
                              padding='SAME')
                              layer += biases
                              if use_pooling:
                layer = tf.nn.max_pool(value=layer,
                               ksize=[1, 2, 2, 1],
                               strides=[1, 2, 2, 1],
                               padding='SAME')
                               layer = tf.nn.relu(layer)
                               return layer, weights
