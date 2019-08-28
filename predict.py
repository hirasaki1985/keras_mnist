# -*- coding: utf-8 -*-
import os, sys
import argparse, json
import datetime
import numpy as np
from app.ai import AI
from app.utils import log
from app.utils.MnistImageManager import MnistImageManager

# modules
logger = log.get()
imageManager = MnistImageManager()

def main(args):
  # create instance
  ai = AI(model_path=args.model, weight_path=args.weight)

  # get predict
  x_test = imageManager.getMnistImageFromPng(args.figure_images + args.target_image)
  logger.debug(x_test.shape)

  input_arr = np.array(x_test)
  input_arr = input_arr.reshape(1, 784)

  # logger.debug(x_test)
  logger.debug(input_arr.shape)

  predict_result = ai.predict(input_arr)
  logger.debug(predict_result.shape)
  logger.debug(predict_result)

  # result
  accuracy = json.dumps(predict_result[0].tolist())
  max = int(np.argmax(predict_result[0]))

  # make response data
  result = {
    "y":accuracy,
    "max": max
  }
  logger.info(result)

if __name__ == '__main__':
  parser = argparse.ArgumentParser()

  parser.add_argument("-model"        , "-m", default="./weights/mnist_mlp_weights.h5", help="")
  parser.add_argument("-weight"       , "-w", default="./weights/mnist_mlp_model.json", help="")
  parser.add_argument("-figure_images", "-f", default="./figure_images/", help="")
  parser.add_argument("-target_image" , "-s", default="sample.png", help="")

  args = parser.parse_args()
  main(args)
