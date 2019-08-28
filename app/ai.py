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

    # mnistデータの管理を行うクラス
    self.imageManager = MnistImageManager()

    # modelデータへのパス
    self.model_path = model_path

    # weightデータへのパス
    self.weight_path = weight_path

    # modelのロード
    self.model = self.getModel()

  def predict(self, x_test):
    """
    推論を行う

    Parameters
    ----------
    x_test : numpy.shape = (x, 784)　の推論したい画像データ
    """

    # predict
    return self.model.predict(x_test, batch_size=1, verbose=0)

  def getModelFromJson(self):
    """
    jsonファイルからmodelの読み込みを行う
    """
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
    """
    modelを作成して返す
    """
    num_classes = 10

    # create model
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

    # load weights
    model.load_weights(self.weight_path)
    model._make_predict_function()

    return model




# 未使用
  def getInputImage(image):
    self.imageManager.getMnistImage(image)
