# -*- coding: utf-8 -*-

import json
from flask import Flask, render_template, make_response, request, jsonify
from PIL import Image
import base64
from io import BytesIO
import numpy as np
from datetime import datetime
from app.ai import AI
from app.utils import log
from app.utils.MnistImageManager import MnistImageManager

# consts
## 手書き文字を保存するかしないか
IS_SAVE_HANDWRITES=False

# modules
logger = log.get()
imageManager = MnistImageManager()
ai = AI()

# flask
app = Flask(__name__)

@app.route('/')
def web_page():
  return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
  # constant values
  end_file_key_name = 'file'

  # get param
  if end_file_key_name not in request.form:
    return jsonify({"result":"error"})

  request_img_file = request.form[end_file_key_name]
  # logger.debug(request_img_file)

  # get image
  image = Image.open(BytesIO(base64.b64decode(request_img_file)))

  # get mnist image
  x_test = imageManager.getMnistImage(image)
  # logger.debug(x_test.shape)

  # reshape mnist image
  input_arr = np.array(x_test)
  input_arr = input_arr.reshape(1, 784)
  # logger.debug(input_arr.shape)

  # predict
  predict_result = ai.predict(input_arr)
  # logger.debug(predict_result.shape)
  # logger.debug(predict_result)

  # result
  accuracy = json.dumps(predict_result[0].tolist())
  max = int(np.argmax(predict_result[0]))

  # make response
  result = {
    "y":accuracy,
    "max": max
  }
  logger.info(result)

  now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

  # save handwrites
  if (IS_SAVE_HANDWRITES):
    imageManager.saveMnistToPng(
      data = x_test,
      file_name = now + '_mnist',
      predict = max
    )
    image.save('./handwrites/' + now + '_png.png')

  # response
  return result

if __name__ == '__main__':
  app.run()

