# -*- coding: utf-8 -*-

from flask import Flask, render_template, make_response, request, jsonify
# import cgi
import base64
from app.ai import AI
from app.utils import log
logger = log.get()

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

  request_file = request.form[end_file_key_name]
  # logger.debug(request_file)
  # request_file = base64.b64decode(contentDataAscii)


  # content = request.data[end_file_key_name]
  # result = controller.predict(request.data[end_file_key_name])
  # logger.debug(result)

  # validate
  # if send_file_key_name not in request.files:
  #   make_response(jsonify({'result':'uploadFile is required.'}))
  #   return

  # get image
  # img_file = request.files[send_file_key_name]

  # save
  # request_file.save(os.path.join('predicts', 'image.png'))

  # predict
  result = ai.predict(request_file)

  # response
  return jsonify({"test":"test"})

if __name__ == '__main__':
  app.run()

