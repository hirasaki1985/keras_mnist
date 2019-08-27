# -*- coding: utf-8 -*-
import numpy as np
from PIL import Image
import struct
import glob

class MnistImageManager:
  def getInputDataFromPng(self, filename):
    print("MnistImageManager getInputDataFromPng")
    print("filename = " + filename)

    img = Image.open(filename).convert("L")
    img = np.resize(img, (28,28,1))
    # im2arr = np.array(img)
    # im2arr = im2arr.reshape(1,28,28,1)
    # features_data = np.append(features_data, im2arr, axis=0)
    # label_data = np.append(label_data, [image_label], axis=0)

    return img
    # return features_data, label_data

  #def __init__(self):
  def getMnistImageFromPng(self, filename):
    # print("MnistImageManager getMnistDataFromPng")
    # print("filename = " + filename)

    image = Image.open(filename)
    img = self.getMnistImage(image)

    return img

  def getMnistImage(self, image):
    #image = image.convert('L').resize((28, 28), c)
    #image = image.convert('L').resize(28, 28)
    image = image.convert('L').resize((28, 28), Image.ANTIALIAS)
    #image.show()
    img = np.asarray(image, dtype=float)
    img = np.floor(56 - 56 * (img / 256))
    img = img.flatten()
    #print(img)
    return img

  def getDataList(self, filter):
    # print("MnistImageManager getDataList")
    # print("filter = " + filter)
    data = []
    label = []
    files = glob.glob(filter)
    #print(files)
    files.sort()
    for one in files:
      data.append(self.getMnistDataFromPng(one))
      start = one.rfind('_')
      end = one.rfind('.')
      #print (str(start) + " : " + str(end))
      #print (one[start + 1:start - end -2])
      label.append(int(one[start + 1:start - end -2]))
    # print(label)
    return data, label

