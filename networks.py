# networks.py
from functools import partial

from keras.layers import Dense, Activation, Conv2D, Flatten, MaxPooling2D, GlobalAveragePooling2D, Dropout, BatchNormalization
from keras.models import Sequential
from keras.applications.vgg16 import VGG16
from keras.applications.resnet50 import ResNet50
from keras.applications.densenet import DenseNet121
from keras.regularizers import l2

def model_c(args):
	"""Model C from Striving for Simplicity: The All Convolutional Net """
	model = Sequential()
	model.add(Dropout(0.2, input_shape=args.input_shape))
	model.add(Conv2D(96, kernel_size=3, activation='relu', padding='same', kernel_regularizer=l2(0.0005), bias_regularizer=l2(0.0005)))
	model.add(Conv2D(96, kernel_size=3, activation='relu', padding='same', kernel_regularizer=l2(0.0005), bias_regularizer=l2(0.0005)))
	model.add(MaxPooling2D((3,3), strides=2))
	model.add(Dropout(0.5))
	model.add(Conv2D(192, kernel_size=3, activation='relu', padding='same', kernel_regularizer=l2(0.0005), bias_regularizer=l2(0.0005)))
	model.add(Conv2D(192, kernel_size=3, activation='relu', padding='same', kernel_regularizer=l2(0.0005), bias_regularizer=l2(0.0005)))
	model.add(MaxPooling2D((3,3), strides=2))
	model.add(Dropout(0.5))
	model.add(Conv2D(192, kernel_size=3, activation='relu', padding='same', kernel_regularizer=l2(0.0005), bias_regularizer=l2(0.0005)))
	model.add(Conv2D(192, kernel_size=1, activation='relu', padding='same', kernel_regularizer=l2(0.0005), bias_regularizer=l2(0.0005)))
	model.add(Conv2D(args.n_outputs, kernel_size=1, activation='relu', padding='same', kernel_regularizer=l2(0.0005), bias_regularizer=l2(0.0005)))
	model.add(GlobalAveragePooling2D())
	#model.add(Dropout(0.5))
	model.add(Activation('softmax'))
	return model

def model_all_cnn_c(args):
	"""Model All-CNN-C from Striving for Simplicity: The All Convolutional Net """
	model = Sequential()
	model.add(Dropout(0.2, input_shape=args.input_shape))
	model.add(Conv2D(96, kernel_size=3, activation='relu', padding='same', kernel_regularizer=l2(0.0005), bias_regularizer=l2(0.0005)))
	model.add(Conv2D(96, kernel_size=3, activation='relu', padding='same', kernel_regularizer=l2(0.0005), bias_regularizer=l2(0.0005)))
	model.add(Conv2D(96, kernel_size=3, activation='relu', padding='same', strides=2, kernel_regularizer=l2(0.0005), bias_regularizer=l2(0.0005)))
	model.add(Dropout(0.5))
	model.add(Conv2D(192, kernel_size=3, activation='relu', padding='same', kernel_regularizer=l2(0.0005), bias_regularizer=l2(0.0005)))
	model.add(Conv2D(192, kernel_size=3, activation='relu', padding='same', kernel_regularizer=l2(0.0005), bias_regularizer=l2(0.0005)))
	model.add(Conv2D(192, kernel_size=3, activation='relu', padding='same', strides=2, kernel_regularizer=l2(0.0005), bias_regularizer=l2(0.0005)))
	model.add(Dropout(0.5))
	model.add(Conv2D(192, kernel_size=3, activation='relu', padding='same', kernel_regularizer=l2(0.0005), bias_regularizer=l2(0.0005)))
	model.add(Conv2D(192, kernel_size=1, activation='relu', padding='same', kernel_regularizer=l2(0.0005), bias_regularizer=l2(0.0005)))
	model.add(Conv2D(args.n_outputs, kernel_size=1, activation='relu', padding='same', kernel_regularizer=l2(0.0005), bias_regularizer=l2(0.0005)))
	model.add(GlobalAveragePooling2D())
	model.add(Activation('softmax'))
	return model

def model_all_cnn_c_bn(args):
	"""	Model All-CNN-C from Striving for Simplicity: The All Convolutional Net 
		Added: Batch normalization
	"""
	model = Sequential()
	model.add(Dropout(0.2, input_shape=args.input_shape))
	model.add(Conv2D(96, kernel_size=3, activation='relu', padding='same', kernel_regularizer=l2(0.0005), bias_regularizer=l2(0.0005)))
	model.add(BatchNormalization())
	model.add(Conv2D(96, kernel_size=3, activation='relu', padding='same', kernel_regularizer=l2(0.0005), bias_regularizer=l2(0.0005)))
	model.add(BatchNormalization())
	model.add(Conv2D(96, kernel_size=3, activation='relu', padding='same', strides=2, kernel_regularizer=l2(0.0005), bias_regularizer=l2(0.0005)))
	model.add(BatchNormalization())
	model.add(Dropout(0.5))
	model.add(Conv2D(192, kernel_size=3, activation='relu', padding='same', kernel_regularizer=l2(0.0005), bias_regularizer=l2(0.0005)))
	model.add(BatchNormalization())
	model.add(Conv2D(192, kernel_size=3, activation='relu', padding='same', kernel_regularizer=l2(0.0005), bias_regularizer=l2(0.0005)))
	model.add(BatchNormalization())
	model.add(Conv2D(192, kernel_size=3, activation='relu', padding='same', strides=2, kernel_regularizer=l2(0.0005), bias_regularizer=l2(0.0005)))
	model.add(BatchNormalization())
	model.add(Dropout(0.5))
	model.add(Conv2D(192, kernel_size=3, activation='relu', padding='same', kernel_regularizer=l2(0.0005), bias_regularizer=l2(0.0005)))
	model.add(Conv2D(192, kernel_size=1, activation='relu', padding='same', kernel_regularizer=l2(0.0005), bias_regularizer=l2(0.0005)))
	model.add(Conv2D(args.n_outputs, kernel_size=1, activation='relu', padding='same', kernel_regularizer=l2(0.0005), bias_regularizer=l2(0.0005)))
	model.add(GlobalAveragePooling2D())
	model.add(Activation('softmax'))
	return model

def simple_conv_net(args):
	""" CNN from https://keras.io/examples/cifar10_cnn/ """
	model = Sequential()
	model.add(Conv2D(32, (3, 3), padding='same', input_shape=args.input_shape))
	model.add(Activation('relu'))
	model.add(Conv2D(32, (3, 3)))
	model.add(Activation('relu'))
	model.add(MaxPooling2D(pool_size=(2, 2)))
	model.add(Dropout(0.25))

	model.add(Conv2D(64, (3, 3), padding='same'))
	model.add(Activation('relu'))
	model.add(Conv2D(64, (3, 3)))
	model.add(Activation('relu'))
	model.add(MaxPooling2D(pool_size=(2, 2)))
	model.add(Dropout(0.25))

	model.add(Flatten())
	model.add(Dense(512))
	model.add(Activation('relu'))
	model.add(Dropout(0.5))
	model.add(Dense(args.n_outputs))
	model.add(Activation('softmax'))
	return model

def simple_bn_conv_net(args):
	model = Sequential()
	model.add(Conv2D(32, (3, 3), padding='same', input_shape=args.input_shape))
	model.add(Activation('relu'))
	model.add(Conv2D(32, (3, 3), use_bias=False))
	model.add(BatchNormalization())
	model.add(Activation('relu'))
	model.add(MaxPooling2D(pool_size=(2, 2)))

	model.add(Conv2D(64, (3, 3), padding='same'))
	model.add(Activation('relu'))
	model.add(Conv2D(64, (3, 3), use_bias=False))
	model.add(BatchNormalization())
	model.add(Activation('relu'))
	model.add(MaxPooling2D(pool_size=(2, 2)))

	model.add(Flatten())
	model.add(Dense(512, use_bias=False))
	model.add(BatchNormalization())
	model.add(Activation('relu'))
	model.add(Dense(args.n_outputs))
	model.add(Activation('softmax'))
	return model

def prebuilt_model(args, model):
	""" Any of the pre-built keras models """
	if args.pretrained:
		prebuilt = model(weights='imagenet', input_shape=args.input_shape, include_top=False)
		for layer in prebuilt.layers:
			layer.trainable = False
	else:
		prebuilt = model(weights=None, input_shape=args.input_shape, include_top=False)
	model = Sequential()
	model.add(prebuilt)
	model.add(Flatten())
	model.add(Activation('relu'))
	model.add(Dense(args.n_outputs))
	model.add(Activation('softmax'))

	return model    



def vgg16(args):
	if args.pretrained:
		prebuilt = VGG16(weights='imagenet', input_shape=args.input_shape, include_top=False)
		for layer in prebuilt.layers:
			layer.trainable = False
	else:
		prebuilt = VGG16(weights=None, input_shape=args.input_shape, include_top=False)
	model = Sequential()
	model.add(prebuilt)
	model.add(Flatten())
	model.add(Dense(4096))
	model.add(Activation('relu'))
	model.add(Dense(4096))
	model.add(Activation('relu'))
	model.add(Dense(args.n_outputs))
	model.add(Activation('softmax'))

	return model    



def lenet5(args):
        model = Sequential()
        # 1st Conv + ReLU + MaxPool
        model.add(Conv2D(10, kernel_size=(5,5), input_shape=args.input_shape))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        # 2nd Conv + ReLU + MaxPool
        model.add(Conv2D(32, kernel_size=(5,5)))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        # Flatten
        model.add(Flatten())
        # 3rd FC
        model.add(Dense(120))
        model.add(Activation('relu'))
        # 4th FC
        model.add(Dense(84))
        model.add(Activation('relu'))
        # Output
        model.add(Dense(args.n_outputs))
        model.add(Activation('softmax'))

        return model

def lenet5_bn(args):
        model = Sequential()
        # 1st Conv + ReLU + MaxPool
        model.add(Conv2D(10, kernel_size=(5,5), input_shape=args.input_shape, use_bias=False))
        model.add(BatchNormalization())
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        # 2nd Conv + ReLU + MaxPool
        model.add(Conv2D(32, kernel_size=(5,5), use_bias=False))
        model.add(BatchNormalization())
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        # Flatten
        model.add(Flatten())
        # 3rd FC
        model.add(Dense(120, use_bias=False))
        model.add(BatchNormalization())
        model.add(Activation('relu'))
        model.add(Dropout(0.5))
        # 4th FC
        model.add(Dense(84, use_bias=False))
        model.add(BatchNormalization())
        model.add(Activation('relu'))
        model.add(Dropout(0.5))
        # Output
        model.add(Dense(args.n_outputs))
        model.add(Activation('softmax'))

        return model

def lenet5_do(args):
        model = Sequential()
        # 1st Conv + ReLU + MaxPool
        model.add(Conv2D(10, kernel_size=(5,5), input_shape=args.input_shape))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Dropout(0.25))
        # 2nd Conv + ReLU + MaxPool
        model.add(Conv2D(32, kernel_size=(5,5)))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Dropout(0.25))
        # Flatten
        model.add(Flatten())
        # 3rd FC
        model.add(Dense(120))
        model.add(Activation('relu'))
        # 4th FC
        model.add(Dense(84))
        model.add(Activation('relu'))
        # Output
        model.add(Dense(args.n_outputs))
        model.add(Activation('softmax'))

        return model

MODELS = {
	'all_conv': model_all_cnn_c,
	'all_bn_conv': model_all_cnn_c_bn,
	'model_c': model_c,
	'simple_conv': simple_conv_net,
    'simple_bn_conv': simple_bn_conv_net,
	'lenet5': lenet5,
        'lenet5_do': lenet5_do,
        'lenet5_bn': lenet5_bn,
	'vgg16': partial(prebuilt_model, model=VGG16),
	'resnet50': partial(prebuilt_model, model=ResNet50),
	'densenet': partial(prebuilt_model, model=DenseNet121),
}
