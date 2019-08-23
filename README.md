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
$ pyenv local anaconda3-5.3.1
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


## Chapter.2
### 環境構築
```
$ pyenv virtualenv anaconda3-5.3.1 keras-mnist
$ pyenv local keras-mnist
$ pip install -r requirements.txt
```

```

## トラブルシューティング
### インストール時権限でpyenv installができない場合
```
$ sudo chown -R $(whoami) $(brew --prefix)/*
```
