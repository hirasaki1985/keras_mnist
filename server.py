# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, jsonify
from app import controller

app = Flask(__name__)

@app.route('/')
def web_page():
  return render_template('index.html')

@app.route('/api/evaluate', methods=['GET', 'POST'])
def evaluate():
  controller.evaluate
  return jsonify({"test":"test"})

if __name__ == '__main__':
  app.run()

