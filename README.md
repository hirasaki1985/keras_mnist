# keras-mnist
## 必要なライブラリ
* [homebrew](https://brew.sh/)
* pyenv

## プログラムのダウンロード
```
$ git clone https://github.com/hirasaki1985/keras_mnist.git
$ cd keras_mnist/
```

## 環境構築
```
$ brew install pyenv
$ brew install pyenv-virtualenv
```

~/.bash_profile
```
export PYENV_ROOT=/usr/local/var/pyenv
if which pyenv > /dev/null; then eval "$(pyenv init -)"; fi
```

```
$ source ~/.bash_profile
```

```
$ pyenv install anaconda3-5.3.1
$ pyenv virtualenv anaconda3-5.3.1 keras-mnist
$ pyenv local keras-mnist
$ pip install -r requirements.txt
```

### 確認
```
$ python -V
Python 3.7.0
$ jupyter --version
4.4.0
$ pyenv --version
pyenv 1.2.13
$ pyenv virtualenv --version
pyenv-virtualenv 1.1.3 (conda conda 4.5.11)
$ which python
/usr/local/var/pyenv/shims/python
$ which jupyter
/usr/local/var/pyenv/shims/jupyter
```

## Chapter.1
### 実行
```
$ jupyter notebook
```

### コマンドラインから学習させる場合
```
$ python chapter.1.py
```


## Chapter.2
### 実行
```
$ export FLASK_APP=server.py
$ flask run
```

[http://127.0.0.1:5000/](http://127.0.0.1:5000/)

### コマンドラインから推論させる場合
```
$ python predict.py
```

## トラブルシューティング
### インストール時権限でpyenv installができない場合
```
$ sudo chown -R $(whoami) $(brew --prefix)/*
```

## 参考
* [keras/examples/mnist_mlp.py](https://github.com/keras-team/keras/blob/master/examples/mnist_mlp.py)
* [Build the MNIST model with your own handwritten digits using TensorFlow, Keras, and Python](https://medium.com/@ashok.tankala/build-the-mnist-model-with-your-own-handwritten-digits-using-tensorflow-keras-and-python-f8ec9f871fd3)
* [Python NumPy Array Tutorial](https://likegeeks.com/numpy-array-tutorial/)
* [How to Save and Load Your Keras Deep Learning Model
](https://machinelearningmastery.com/save-load-keras-deep-learning-models/)
* [MNISTの画像をPNGに変換してみた](https://water2litter.net/rum/post/ai_mnist_convert/)
* [ゼロから作るDeep Learning ―Pythonで学ぶディープラーニングの理論と実装](https://amzn.to/2ZmqDWP)
* [PythonとKerasによるディープラーニング](https://amzn.to/2Ph6fm6)
