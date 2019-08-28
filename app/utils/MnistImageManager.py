# -*- coding: utf-8 -*-
import numpy as np
from PIL import Image
import struct
import glob

class MnistImageManager:

  def getMnistImageFromPng(self, filename):
    """
    指定されたパスからpng画像を読み込み、mnist形式に変換する
    """
    # print("MnistImageManager getMnistDataFromPng")
    # print("filename = " + filename)

    image = Image.open(filename)
    img = self.getMnistImage(image)

    return img

  def getMnistImage(self, image, clear=20):
    """
    Imageオブジェクトをmnist形式に変換する
    """
    # convert and resize
    # image = image.convert('L').resize((28, 28), c)
    # image = image.convert('L').resize((28, 28))
    image = image.convert('L').resize((28, 28), Image.LANCZOS)

    img = np.asarray(image, dtype=float)
    img = np.floor(56 - 56 * (img / 256))

    # 反転
    # img = np.rot90(img)
    # img = np.flipud(img)

    img = img.flatten()
    #print(img)

    # リサイズすると手書き文字がボケるので、明暗をはっきりさせる
    if (clear is not None):
      for i in range(img.size):
        pixel = int(img[i])
        # print(pixel)
        if (pixel > 0):
          img[i] = pixel * clear

    return img

  def saveMnistToPng(self, data, file_name, base_directory='./handwrites/', predict=None):
    """
    mnist形式のデータをpng画像として保存する
    """
    img = Image.new('L', (28,28))
    pix = img.load()

    d = data.reshape(28, 28)
    for i in range(28):
      for j in range(28):
        pix[i, j] = int(d[j][i])

    # img = ImageOps.invert(img)
    # img = img.resize((224,224), Image.BICUBIC)

    if (predict is None):
      img.save(base_directory + file_name + '.png')
    else:
      img.save(base_directory + file_name + str(predict) + '.png')







# 未使用
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

