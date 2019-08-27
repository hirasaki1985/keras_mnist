# -*- coding: utf-8 -*-

import json
from flask import Flask, render_template, make_response, request, jsonify
from PIL import Image
import base64
from io import BytesIO
import numpy as np
from app.ai import AI
from app.utils import log
from app.utils.MnistImageManager import MnistImageManager

# modules
logger = log.get()
imageManager = MnistImageManager()

app = Flask(__name__)
ai = AI()

@app.route('/')
def web_page():
  return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
  # constant values
  end_file_key_name = 'file'

  # request print
  #logger.debug("body: %s" % request.get_data())
  # logger.debug(request.get_data())

  # get param
  # request_data = request.get_json()
  # logger.debug(request_data)
  if end_file_key_name not in request.form:
    return jsonify({"result":"error"})

  request_img_file = request.form[end_file_key_name]
  logger.debug(request_img_file)

  # get image
  image = Image.open(BytesIO(base64.b64decode(request_img_file)))

  # get mnist image
  x_test = imageManager.getMnistImage(image)
  logger.debug(x_test.shape)

  # reshape mnist image
  input_arr = np.array(x_test)
  input_arr = input_arr.reshape(1, 784)
  logger.debug(input_arr.shape)

  # save
  # request_file.save(os.path.join('predicts', 'image.png'))

  # predict
  predict_result = ai.predict(input_arr)
  logger.debug(predict_result.shape)
  logger.debug(predict_result)

  # result
  accuracy = json.dumps(predict_result[0].tolist())
  max = int(np.argmax(predict_result[0]))

  # make response
  result = {
    "y":accuracy,
    "max": max
  }

  # response
  return result

if __name__ == '__main__':
  app.run()

