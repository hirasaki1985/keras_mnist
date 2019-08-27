# -*- coding: utf-8 -*-
from __future__ import print_function

import os
import keras
from keras.datasets import mnist
from keras.models import load_model, model_from_json
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import RMSprop
from PIL import Image
import json
from app.utils.MnistImageManager import MnistImageManager
from app.utils import log
logger = log.get()

class AI:
  def __init__(self,
      model_path = './weights/mnist_mlp_model.json',
      weight_path = './weights/mnist_mlp_weights.h5'):
    self.imageManager = MnistImageManager()
    self.model_path = model_path
    self.weight_path = weight_path

  def predict(self, x_test):
    # get model
    model = self.getModel()

    # create input
    # image = Image.open(BytesIO(base64.b64decode(img_file.value)))
    # input_x = self.getInputImage(image)

    # predict
    return model.predict(x_test, batch_size=1, verbose=0)

  def getModelFromJson(self):
    json_file = open(self.model_path, 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # if os.path.exists(self.model_path):
    #   with open(self.model_path ,'r') as f:
    #     model_json = json.load(f)
    # else:
    #   logger.error('model file read error.')

    # model = model_from_json(model_json)
    # model.load_weights(self.weight_path)

    return model

  def getModel(self):
    num_classes = 10

    model = Sequential()
    model.add(Dense(512, activation='relu', input_shape=(784,)))
    model.add(Dropout(0.2))
    model.add(Dense(512, activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(num_classes, activation='softmax'))

    model.summary()

    model.compile(loss='categorical_crossentropy',
                  optimizer=RMSprop(),
                  metrics=['accuracy'])

    return model

  def getInputImage(image):
    self.imageManager.getMnistImage(image)
