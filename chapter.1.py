#!/usr/bin/env python
# coding: utf-8

# ## 必要なライブラリのインポート

# In[1]:


from __future__ import print_function

import json
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import RMSprop


# ## 定数の設定

# In[2]:


batch_size = 128


# In[3]:


num_classes = 10


# In[4]:


epochs = 5


# In[5]:


weight_save_path = './weights/mnist_mlp_weights.h5'


# In[6]:


model_save_path = './weights/mnist_mlp_model.json'


# ## 学習データのダウンロード

# In[7]:


(x_train, y_train), (x_test, y_test) = mnist.load_data()


# In[8]:


x_train = x_train.reshape(60000, 784)


# In[9]:


x_test = x_test.reshape(10000, 784)


# In[10]:


x_train = x_train.astype('float32')


# In[11]:


x_test = x_test.astype('float32')


# In[12]:


x_train /= 255


# In[13]:


x_test /= 255


# In[14]:


print(x_train.shape[0], 'train samples')


# In[15]:


print(x_test.shape[0], 'test samples')


# In[16]:


y_train = keras.utils.to_categorical(y_train, num_classes)


# In[17]:


y_test = keras.utils.to_categorical(y_test, num_classes)


# ## モデルの作成

# In[18]:


model = Sequential()


# In[19]:


model.add(Dense(512, activation='relu', input_shape=(784,)))


# In[20]:


model.add(Dropout(0.2))


# In[21]:


model.add(Dense(512, activation='relu'))


# In[22]:


model.add(Dropout(0.2))


# In[23]:


model.add(Dense(num_classes, activation='softmax'))


# In[24]:


model.summary()


# In[25]:


model.compile(loss='categorical_crossentropy',
              optimizer=RMSprop(),
              metrics=['accuracy'])


# ## 学習

# In[26]:


history = model.fit(x_train, y_train,
                    batch_size=batch_size,
                    epochs=epochs,
                    verbose=1,
                    validation_data=(x_test, y_test))


# ## 学習結果の確認

# In[27]:


score = model.evaluate(x_test, y_test, verbose=0)


# In[28]:


print('Test loss:', score[0])


# In[29]:


print('Test accuracy:', score[1])


# ## 学習結果の保存

# In[30]:


model.save_weights(weight_save_path)


# In[31]:


model_json = model.to_json()
with open(model_save_path, "w") as json_file:
    json.dump(model_json, json_file)

