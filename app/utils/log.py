# -*- coding: utf-8 -*-
import os, sys

# from utils import env
from logging import getLogger, StreamHandler, INFO, DEBUG, ERROR

logger = getLogger(__name__)
handler = StreamHandler()

#log_level = env.get('LOG_LEVEL')
log_level = 'debug'

if log_level == "info":
  handler.setLevel(INFO)
  logger.setLevel(INFO)
elif log_level == "debug":
  handler.setLevel(DEBUG)
  logger.setLevel(DEBUG)
elif log_level == "error":
  handler.setLevel(ERROR)
  logger.setLevel(ERROR)

logger.addHandler(handler)

def get():
  """
  loggerオブジェクトを返す
  Returns
  -------
  logger : object
  """
  return logger
