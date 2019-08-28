# -*- coding: utf-8 -*-
import os, sys
import argparse, json
import datetime
import numpy as np
from keras.datasets import mnist
from app.ai import AI
from app.utils import log
from app.utils.MnistImageManager import MnistImageManager

# modules
logger = log.get()
imageManager = MnistImageManager()

def main(args):
  test_save_mnist_to_png(args)


def test_save_mnist_to_png(args):
  (x_train, y_train), (x_test, y_test) = mnist.load_data()

  for x in range(args.start, args.end):
    one_data = x_train[x]

    imageManager.saveMnistToPng(
      data = one_data,
      file_name = 'test_' + str(x),
    )

if __name__ == '__main__':
  parser = argparse.ArgumentParser()

  parser.add_argument("-start"  , "-s", default=0,  type=int, help="")
  parser.add_argument("-end"    , "-e", default=10, type=int, help="")

  args = parser.parse_args()
  main(args)
